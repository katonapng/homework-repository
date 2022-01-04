import csv

from polls.models import Teacher


def get_report():
    with open("report.csv", "w") as report:
        writer = csv.writer(report)
        for hw, values in Teacher.homework_done.items():
            for value in values:
                writer.writerow([value[0], hw.created, value[1]])
