class SingleRequestController(object):

    def __init__(self, url, method):
        self.url = str(url)
        self.method = str(method)

    def __str__(self):
        return "Url: " + self.url + " Method: " + self.method
