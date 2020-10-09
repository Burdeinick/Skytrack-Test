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


    def req_get_user(self, id_user):
        """The request that returns the user and their "id"."""
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


class StatusResponse:
    """The class contains some statuses
    response, which server will return
    to users.

    """
    def __init__(self):
        """The constructor create the statuses."""
        self.invalid_data = {"Error": "Invalid data accepted"}
        self.user_not_exit = {"Error": "The user does not exist"}


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
        """The method handle 'get_user' of server."""
        try:
            expected_keys = ("id_user",)
            data_valid = self.checker.valid_data(self.data, expected_keys)
            if data_valid:
                id_user = int(self.data[expected_keys[0]])
                user_exist = self.reqest_db.req_get_user(id_user)
                if user_exist:
                    return user_exist
                else:
                    return self.stat_resp.user_not_exit
            else:
                return self.stat_resp.invalid_data

        except Exception:
            super_logger.error('Error hand_get_user', exc_info=True)


