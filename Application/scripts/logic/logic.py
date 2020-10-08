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
        pass


class Checker:
    """The class for checking necessary
    information.

    """
    def __init__(self):
        """ """
        pass

    def valid_data(self):
        """The method checks validity data of request."""



class HandlerServer:
    """The class can to process requests of server."""
    def __init__(self):
        """ """
        self.stat_resp = StatusResponse()

    def hand_get_user(self):
        """The method handle 'get_user' of server.""""

