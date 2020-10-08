from logger.log import MyLogging


super_logger = MyLogging().setup_logger('logic',
                                        'Application/logger/logfile.log')


class StatusResponse:
    """The class contains some statuses
    response, which server will return
    to users.

    """
    def __init__(self):
        """The constructor create the statuses."""
        self.invalid_data = {"Error": "Invalid data accepted"}


class Checker:
    """The class for checking necessary
    information.

    """
    def __init__(self):
        """ """
        pass

    def valid_get_user(self, data: dict) -> bool:
        """The method checks validity data of request
        get_user if it valid return True else False.

        """
        try:
            id_user = str(data.get("id_user")) if "id_user" in data else None 
            if id_user and id_user.isalnum():
                return True

        except Exception:
            super_logger.error('Error valid_get_user', exc_info=True)


class HandlerServer:
    """The class can to process requests of server."""
    def __init__(self, data: dict):
        """ """
        self.stat_resp = StatusResponse()
        self.checker = Checker()
        self.data = data

    async def hand_get_user(self):
        """The method handle 'get_user' of server."""
        data_valid = self.checker.valid_get_user(self.data)
        if data_valid:
            pass
        else:
            return self.stat_resp.invalid_data


