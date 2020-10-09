from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from logger.log import MyLogging


super_logger = MyLogging().setup_logger('logic',
                                        'Application/logger/logfile.log')


class ConnectDB:
    """Class for connecting the database."""
    def __init__(self):
        """ """
        db_connection_str = 'sqlite:///trad_plat.db'
        self.engine = create_engine(db_connection_str, echo = True)
        self._cur_ = self.engine
        Session = sessionmaker(bind=self._cur_)
        self.session = Session()


class RequestDB:
    """The class for executing queries
    in the database using ORM.

    """
    def __init__(self):
        """Preset tables from the database
        for further use with ORM,
        connecting the engine from the ConnectDB class,
        creating a session of the ConnectDB class.

        """
        self.engine = ConnectDB().engine
        self.session = ConnectDB().session
        metadata = MetaData()
        metadata.reflect(self.engine, only=['User',
                                            'Book', 
                                            'Shop', 
                                            'Assortiment', 
                                            'OrderAll', 
                                            'OrderItem'])

        Base = automap_base(metadata=metadata)
        Base.prepare()
        self.User = Base.classes.User
        self.Book = Base.classes.Book
        self.Shop = Base.classes.Shop
        self.Assortiment = Base.classes.Assortiment
        self.OrderAll = Base.classes.OrderAll
        self.OrderItem = Base.classes.OrderItem


    def req_get_user(self, id_user: str):
        """The request that returns the user or 'False'."""
        try:
            request_user = self.session.query(self.User).filter(self.User.id_user==id_user)
            for user in request_user:
                resp_user = {"name": user.name, 
                            "surname": user.surname, 
                            "fathers_name": user.fathers_name, 
                            "email": user.email}
                return resp_user
            return False

        except Exception:
            super_logger.error('Error req_get_user', exc_info=True)

    def req_get_order_user(self, id_user: str) -> dict:
        """The request returns the user's orders."""
        try:
            query = self.session.query(self.User, 
                                       self.OrderAll, 
                                       self.Book, 
                                       self.OrderItem, 
                                       self.Shop).filter(self.User.id_user==id_user)

            query = query.join(self.User, self.OrderAll.id_user==self.User.id_user)
            query = query.join(self.OrderItem, self.OrderAll.id_order_all==self.OrderItem.id_order_all)
            query = query.join(self.Shop, self.OrderItem.id_shop==self.Shop.id_shop)
            query = query.join(self.Book, self.OrderItem.id_book==self.Book.id_book)             

            orders = {"orders": []}

            for self.User, self.OrderAll, self.Book, self.OrderItem, self.Shop in query:
                orders["orders"].append({"user_name": self.User.name, 
                                        "reg_data": self.OrderAll.reg_data, 
                                        "book_name": self.Book.name,
                                        "book_quantity": self.OrderItem.book_quantity,
                                        "shop_name": self.Shop.name})
            return orders

        except Exception:
            super_logger.error('Error req_get_order_user', exc_info=True)


    def req_get_shop(self, id_shop: str):
        """The request that returns the shop or 'False'."""
        try:
            request_shop = self.session.query(self.Shop).filter(self.Shop.id_shop==id_shop)
            for shop in request_shop:
                resp_shop = {"shop_name": shop.name, 
                             "shop_address":shop.address, 
                             "shop_post_code": shop.post_code}
                return resp_shop
            return False

        except Exception:
            super_logger.error('Error req_get_shop', exc_info=True)

    def req_get_assortiment(self, id_shop):
        """The request returns the shop's assortiments."""
        try:
            query= self.session.query(self.Book,
                                      self.Assortiment,
                                      self.Shop).filter(self.Shop.id_shop==id_shop)

            query = query.join(self.Assortiment, self.Book.id_book==self.Assortiment.id_book)
            query = query.join(self.Shop, self.Shop.id_shop==self.Assortiment.id_shop)

            assortiment = {"assortiment":[]}

            for self.Book, self.Assortiment, self.Shop in query:
                assortiment["assortiment"].append({"shop_name": self.Shop.name,
                                                    "book_name": self.Book.name,
                                                    "book_author": self.Book.author,
                                                    "isbn": self.Book.isbn})
            return assortiment

        except Exception:
            super_logger.error('Error req_get_assortiment', exc_info=True)


class StatusResponse:
    """The class contains some statuses
    response, which server will return
    to users.

    """
    def __init__(self):
        """The constructor create the statuses."""
        self.invalid_data = {"Error": "Invalid data accepted"}
        self.user_not_exist = {"Info": "The user does not exist"}
        self.no_orders = {"Info": "The user has no orders"}
        self.no_books = {"Info": "There are no books in this store"}
        self.shop_not_exist = {"Info" : "The store does not exist"}


class Checker:
    """The class for checking necessary
    information.

    """
    def __init__(self):
        """ """
        pass

    def valid_data(self, data: dict, keys: tuple) -> bool:
        """The method checks validity data of request
        get_user if it valid return True else False.

        """
        try:
            for key in keys:
                id_user = str(data.get(key)) if key in data else None 
                if id_user and id_user.isalnum():
                    continue
                else:
                    return False
            return True

        except Exception:
            super_logger.error('Error valid_data', exc_info=True)


class HandlerServer:
    """The class can to process requests of server."""
    def __init__(self, data: dict):
        """ """
        self.reqest_db = RequestDB()
        self.stat_resp = StatusResponse()
        self.checker = Checker()
        self.data = data

    async def hand_get_user(self):
        """The method is handler 'get_user' of server."""
        try:
            expected_keys = ("id_user",)
            data_valid = self.checker.valid_data(self.data, expected_keys)
            if data_valid:
                id_user = str(self.data[expected_keys[0]])
                user_exist = self.reqest_db.req_get_user(id_user)
                if user_exist:
                    return user_exist
                else:
                    return self.stat_resp.user_not_exist
            else:
                return self.stat_resp.invalid_data

        except Exception:
            super_logger.error('Error hand_get_user', exc_info=True)

    async def hand_get_order_user(self):
        """The method is handler 'get_order_user' 
        of server.
        
        """
        try:
            expected_keys = ("id_user",)
            data_valid = self.checker.valid_data(self.data, expected_keys)
            if data_valid:
                id_user = str(self.data[expected_keys[0]])
                user_exist = self.reqest_db.req_get_user(id_user)
                if user_exist:
                    orders = self.reqest_db.req_get_order_user(id_user)
                    if orders.get("orders"):
                        return orders
                    else:
                        return self.stat_resp.no_orders
                else:
                    return self.stat_resp.user_not_exist
            else:
                return self.stat_resp.invalid_data

        except Exception:
            super_logger.error('Error hand_get_order_user', exc_info=True)      


    async def hand_get_shop(self):
        """The method is handler 'get_shop' 
        of server.
        
        """
        try:
            expected_keys = ("id_shop",)
            data_valid = self.checker.valid_data(self.data, expected_keys)
            if data_valid:
                id_shop = str(self.data[expected_keys[0]])
                shop_exist =self.reqest_db.req_get_shop(id_shop)
                if shop_exist:
                    assortiment = self.reqest_db.req_get_assortiment(id_shop)
                    if assortiment:
                        return assortiment
                    else:
                        return self.stat_resp.no_books
                else:
                    return self.stat_resp.shop_not_exist
            else:
                return self.stat_resp.invalid_data

        except Exception:
            super_logger.error('Error hand_get_shop', exc_info=True)      
