import asyncio
import datetime
import json
import time
from concurrent.futures.process import ProcessPoolExecutor
from copy import copy, deepcopy
from threading import Thread
from urllib.request import urlopen

import aiohttp
from bs4 import BeautifulSoup

special_characters = '\r\t\n,'


def get_soup(html_page):
    return BeautifulSoup(html_page, "html.parser")


def dollar_rate(url="http://www.cbr.ru/scripts/XML_daily.asp?date_req="):
    today_url = url + datetime.date.today().strftime("%d/%m/%Y")
    response = urlopen(today_url)
    soup = BeautifulSoup(response, "html.parser")
    return float(soup.find(id="R01235").value.text.replace(",", "."))


async def get_page(session, url) -> None:
    async with session.get(url) as response:
        return await response.text()


async def fetch_async(url):
    tasks = []
    async with aiohttp.ClientSession() as session:
        main_page = urlopen(url)
        soup = get_soup(main_page)

        pages = soup.find('div', {'class':
                          'finando_paging margin-top--small'})
        links = [link['href'] for link in pages.find_all('a')]
        page_links = list(dict.fromkeys(links))
        pages = [url + link for link in page_links]
        for page in pages:
            task = asyncio.ensure_future(get_page(session, page))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses


def get_pages_links(url):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(fetch_async(url))
    loop.run_until_complete(future)
    return future.result()


def get_rubles_value(page):
    table_info = []
    rate = dollar_rate()

    soup = get_soup(page)
    table = soup.find('table', {'class': "table table__layout--fixed"})

    for row in table.find_all('tr'):
        column = row.find_all('td')
        if column != []:
            value = column[1].text.strip()
            growth = column[7].text.strip()
            calculated_growth = float(
                growth[growth.index('\n') + 1:].replace('%', '')
                )
            calculated_rate = float(value[:value.index('\r')].replace(",", ""))
            table_info.append({'Year_growth':
                               calculated_growth,
                               'Rubles_value':
                               round(rate*calculated_rate, 2)})

    return table_info


def get_company_pages(page):
    url = "https://markets.businessinsider.com"
    soup = get_soup(page)
    table = soup.find('table', {'class': "table table__layout--fixed"})
    links = [url + link.get("href") for link in table.find_all("a")]
    return links


def get_pages_info(pages):
    table_info, company_pages = [], []
    for page in pages:
        table_info.append(get_rubles_value(page))
        company_pages.append(get_company_pages(page))

    return table_info, company_pages


def get_company_info(company_page_link):
    PE_ratio, weeks_high, weeks_low, profit = None, None, None, None

    company_page = urlopen(company_page_link)
    little_soup = BeautifulSoup(company_page, "html.parser")
    category = little_soup.find('span', {'class': 'price-section__category'})
    text = copy(category.text)
    for char in special_characters:
        text = text.replace(char, '')
    category = text

    snapshots = little_soup.find_all('div', {'class': 'snapshot__data-item'})
    for snap in snapshots:
        if 'P/E Ratio' in snap.text:
            text = copy(snap.text)
            for char in special_characters:
                text = text.replace(char, '')
            PE_ratio = float(text.replace('P/E Ratio', ''))

    low_all = little_soup.find_all('div',
                                   {'class':
                                    'snapshot__data-item'
                                    ' snapshot__data-item--small'})
    high_all = little_soup.find_all('div',
                                    {'class':
                                     'snapshot__data-item'
                                     ' snapshot__data-item--small'
                                     ' snapshot__data-item--right'})

    for low, high in zip(low_all, high_all):
        if 'Week Low' in low.text:
            weeks_low = low
        if 'Week High' in high.text:
            weeks_high = high

    if weeks_high is not None and weeks_low is not None:
        text1 = copy(weeks_high.text)
        text2 = copy(weeks_low.text)
        for char in special_characters:
            text1 = text1.replace(char, '')
            text2 = text2.replace(char, '')
        weeks_high_text = text1.replace('Week High', '')
        weeks_low_text = text2.replace('Week Low', '')
        profit = float(weeks_high_text) - float(weeks_low_text)

    return {"Category": category, "P/E Ratio": PE_ratio, "Profit": profit}


def top10_companies(table_info, key, PE=False):
    sorted_table_info = sorted(table_info,
                               key=lambda item:
                               (item[key] is not None, item[key]))
    if PE:
        temp = deepcopy(sorted_table_info)
        for item in temp:
            if item['P/E Ratio'] is None:
                sorted_table_info.pop(sorted_table_info.index(item))

    return sorted_table_info[-10:] if not PE else sorted_table_info[:10]


def flatten(t):
    return [item for sublist in t for item in sublist]


def write(db, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    url = 'https://markets.businessinsider.com/index/components/s&p_500'
    pages = get_pages_links(url)
    table_info, company_pages = get_pages_info(pages)
    company_pages = flatten(company_pages)
    table_info = flatten(table_info)

    start = time.time()
    with ProcessPoolExecutor() as pool:
        comp_info = pool.map(get_company_info, company_pages)
    end = time.time()
    print(f"time = {round(end - start)} sec")

    comp_info_list = list(comp_info)
    all_companies_info = [{**item1, **item2}
                          for item1, item2 in zip(table_info, comp_info_list)]

    keys = ['Rubles_value', 'Profit', 'Year_growth']
    top10 = []
    for key in keys:
        top10.append(top10_companies(all_companies_info, key))
    top10.append(top10_companies(all_companies_info, 'P/E Ratio', True))

    filenames = ['top10_rubles_value.json', 'top10_profit.json',
                 'top10_year_growth.json', 'top10_low_PE.json']
    for name, top in zip(filenames, top10):
        Thread(target=write(top, name)).start()
