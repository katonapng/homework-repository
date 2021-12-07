import sqlite3
from collections import defaultdict, namedtuple


class TableData:
    def __init__(self, database_name, table_name) -> None:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        setattr(self, 'db_name', database_name)
        setattr(self, 'tb_name', table_name)
        setattr(self, 'conn', conn)
        setattr(self, 'cursor', cursor)

        try:
            cursor.execute(f'SELECT * from {table_name} ORDER BY name')
        except sqlite3.OperationalError:
            raise sqlite3.OperationalError(f"no table named {table_name}")

        cell = namedtuple('cell', ['name', 'info'])
        self.custom_dict = defaultdict(str)
        while row := cursor.fetchone():
            president = cell(row[0], row[1:])
            self.custom_dict[president.name] = list(president.info)

    def __getitem__(self, key):
        self.update_database()
        return self.custom_dict[key]

    def __iter__(self):
        self.update_database()
        for elem in self.custom_dict:
            yield elem

    def __len__(self):
        self.update_database()
        return len(self.custom_dict)

    def update_database(self):
        try:
            self.cursor.execute(f'SELECT * from {self.tb_name} ORDER BY name')
        except sqlite3.OperationalError:
            raise sqlite3.OperationalError(f"no table named {self.tb_name}")

        cell = namedtuple('cell', ['name', 'info'])
        self.custom_dict = defaultdict(str)
        while row := self.cursor.fetchone():
            president = cell(row[0], row[1:])
            self.custom_dict[president.name] = list(president.info)
