import sys
import sqlite3
sys.path.insert(0, 'Application')
from scripts.data_base.preparing import ConnectionDB
from logger.log import MyLogging


super_logger = MyLogging().setup_logger('drop_db_logger',
                                        'Application/logger/logfile.log')


class DropTableDb:
    """The class for deleting tables."""
    def __init__(self):
        self.connect_db = ConnectionDB().conn

    def drop_user(self):
        """Request to drop the 'User' table."""
        try:
            with self.connect_db:
                request = """DROP TABLE IF EXISTS User"""
                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error drop_user', exc_info=True)

    def drop_book(self):
        """Request to drop the 'Book' table."""
        try:
            with self.connect_db:
                request = """DROP TABLE IF EXISTS Book"""
                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error drop_user', exc_info=True)

    def drop_shop(self):
        """Request to drop the 'Shop' table."""
        try:
            with self.connect_db:
                request = """DROP TABLE IF EXISTS Shop"""
                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error drop_shop', exc_info=True)

    def drop_order_all(self):
        """Request to drop the 'Orderall' table."""
        try:
            with self.connect_db:
                request = """DROP TABLE IF EXISTS OrderAll"""
                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error drop_order_all', exc_info=True)

    def drop_orderitem(self):
        """Request to drop the 'OrderItem' table."""
        try:
            with self.connect_db:
                request = """DROP TABLE IF EXISTS OrderItem"""
                self.connect_db.execute(request)
                self.connect_db.commit()

        except Exception:
            super_logger.error('Error drop_orderitem', exc_info=True)


def main():
    db = DropTableDb()
    db.drop_user()
    db.drop_book()
    db.drop_shop()
    db.drop_order_all()
    db.drop_orderitem()


if __name__ == "__main__":
    main()
