import sys
sys.path.insert(0, 'Application')
import json
import sqlite3
from logger.log import MyLogging


super_logger = MyLogging().setup_logger('preparing_db_logger',
                                        'Application/logger/logfile.log')


class ConnectionDB:
    """Class for connect to DB."""
    def __init__(self):
        self.dbname = self.get_config_db()[0]
        self.conn = sqlite3.connect(self.dbname, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_config_db(self) -> tuple:
        """The method getting informations of configuration file."""
        with open('Application/config.json') as config:
            json_str = config.read()
            json_str = json.loads(json_str)
        dbname = str(json_str['data_Base']['dbname'])
        return (dbname, )


class PreparDb:
    """The class for creating tables in a database."""
    def __init__(self):
        self.connect_db = ConnectionDB().conn

    def foreign_keys_on(self):
        """Allows you to use linked keys."""
        try:
            with self.connect_db:
                request = """PRAGMA foreign_keys=on"""
                self.connect_db.execute(request)
        except Exception:
            super_logger.error('Error foreign_keys_on', exc_info=True)

    def create_user(self):
        """This method creates the 'user' table."""
        try:
            with self.connect_db:
                request = """CREATE TABLE IF NOT EXISTS User(
                             id_user INTEGER PRIMARY KEY
                             AUTOINCREMENT NOT NULL,
                             name TEXT NOT NULL,
                             surname TEXT NOT NULL,
                             fathers_name TEXT NOT NULL,
                             email TEXT NOT NULL,
                             UNIQUE(email)
                             )"""
                self.connect_db.execute(request)
                self.connect_db.commit()
        except Exception:
            super_logger.error('Error create_user', exc_info=True)

    def add_user(self):
        """This method fills in the 'user' table. """
        try:
            with self.connect_db:
                request = """INSERT INTO User
                             (name, surname, fathers_name, email)
                             VALUES
                             ('Bob', 'Smith', 'Viktorovich', 'bo@ya.ru'),
                             ('Kop', 'Johnson', 'Alexandrovich', 'ko@ya.ru'),
                             ('Rob', 'Miller', 'Yurievich', 'ro@ya.ru')
                          """

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error add_user', exc_info=True)

    def create_book(self):
        """This method creates the 'Book' table."""
        try:
            with self.connect_db:
                request = """CREATE TABLE IF NOT EXISTS Book
                             (id_book INTEGER PRIMARY KEY
                             AUTOINCREMENT NOT NULL,
                             name TEXT NOT NULL,
                             author TEXT NOT NULL,
                             isbn TEXT NOT NULL
                             )"""

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error create_book', exc_info=True)

    def add_book(self):
        """This method fills in the 'book' table. """
        try:
            with self.connect_db:
                request = """
                          INSERT INTO Book
                          (name, author, isbn)
                          VALUES
                          ('Идиот', 'Достоевский Ф.М.', '700-5-699-12014-7'),

                          ('Мастер и Маргарита', 'Булгаков М.А.',
                          '800-5-699-12014-7'),

                          ('Доктор Живаго', 'Пастернак Б.Л.',
                          '900-5-699-12014-7')
                          """

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error add_book', exc_info=True)

    def create_shop(self):
        """This method creates the 'shop' table."""
        try:
            with self.connect_db:
                request = """CREATE TABLE IF NOT EXISTS Shop
                             (id_shop INTEGER PRIMARY KEY
                             AUTOINCREMENT NOT NULL,
                             name TEXT NOT NULL,
                             address TEXT NOT NULL,
                             post_code TEXT NOT NULL,
                             UNIQUE(name)
                             )"""

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error create_shop', exc_info=True)

    def add_shop(self):
        """This method fills in the 'shop' table. """
        try:
            with self.connect_db:
                request = """
                          INSERT INTO Shop
                          (name, address, post_code)
                          VALUES
                          ('Beru', 'Пыжевская., 7, стр. 2, Москва', '140130'),
                          ('Ozon', 'ул. Ленина, 26, стр. 5, Москва', '150120'),
                          ('AliExpress', 'Топовая., 1Б, 1, Москва', '130110')
                          """

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error add_shop', exc_info=True)

    def create_assortiment(self):
        """This method creates the 'Assortiment' table."""
        try:
            with self.connect_db:
                request = """CREATE TABLE IF NOT EXISTS Assortiment
                             (id_assortiment INTEGER PRIMARY KEY
                             AUTOINCREMENT NOT NULL,
                             id_book INTEGER NOT NULL,
                             id_shop INTEGER NOT NULL,
                             FOREIGN KEY (id_book)
                             REFERENCES Book(id_book),
                             FOREIGN KEY (id_shop)
                             REFERENCES Shop(id_shop)
                             )"""

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error create_assortiment', exc_info=True)

    def add_assortiment(self):
        """This method fills in the 'Assortiment' table. """
        try:
            with self.connect_db:
                request = """
                          INSERT INTO Assortiment
                          (id_book, id_shop)
                          VALUES
                          (1, 1),
                          (1, 2),
                          (1, 3),
                          (2, 2),
                          (2, 3),
                          (3, 1)
                          """

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error add_assortiment', exc_info=True)

    def create_order_all(self):
        """This method creates the 'OrderAll' table."""
        try:
            with self.connect_db:
                request = """CREATE TABLE IF NOT EXISTS OrderAll(
                             id_order_all INTEGER PRIMARY KEY
                             AUTOINCREMENT NOT NULL,
                             reg_data TEXT NOT NULL,
                             id_user INTEGER NOT NULL,
                             FOREIGN KEY (id_user)
                             REFERENCES User(id_user)
                             ON DELETE CASCADE
                             )"""

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error create_order_all', exc_info=True)

    def create_orderitem(self):
        """This method creates the 'OrderItem' table."""
        try:
            with self.connect_db:
                request = """CREATE TABLE IF NOT EXISTS OrderItem(
                             id_OrderItem INTEGER PRIMARY KEY
                             AUTOINCREMENT NOT NULL,

                             book_quantity INTEGER NOT NULL,
                             id_order_all INTEGER NOT NULL,
                             id_book INTEGER NOT NULL,
                             id_shop INTEGER NOT NULL,

                             FOREIGN KEY (id_order_all)
                             REFERENCES OrderAll(id_order_all)

                             FOREIGN KEY (id_book)
                             REFERENCES Book(id_book),

                             FOREIGN KEY (id_shop)
                             REFERENCES Shop(id_shop)
                             )"""

                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error create_orderitem', exc_info=True)


def main():
    db = PreparDb()
    db.create_user()
    db.add_user()
    db.create_book()
    db.add_book()
    db.create_shop()
    db.add_shop()
    db.create_assortiment()
    db.add_assortiment()
    db.create_order_all()
    db.create_orderitem()


if __name__ == "__main__":
    main()
