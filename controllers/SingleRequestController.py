from models.SecurityRequest import SecurityRequest

class SingleRequestController(object):

    def __init__(self, url, method):
        self.security_request = SecurityRequest(url, method)

    def __str__(self):
        return str(self.security_request)
