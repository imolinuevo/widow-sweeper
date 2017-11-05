import validators, requests
from models.HttpHeaderReport import HttpHeaderReport

allowed_methods = ['GET', 'POST']

class SecurityRequest(object):

    def __init__(self, url, method):
        self.url = url
        self.method = str(method).upper()
        self.is_valid = self.validate_params()
        if self.is_valid:
            self.request_result = self.execute_request()
            if self.request_result:
                self.header_report = HttpHeaderReport(self.request_result.headers)
            else:
                self.header_report = None
        else:
            self.request_result = None

    def validate_params(self):
        return validators.url(self.url) and self.method in allowed_methods

    def execute_request(self):
        switcher = {
            "GET": requests.get(self.url),
            "POST": requests.post(self.url)
        }
        return switcher.get(self.method, None)

    def __str__(self):
        if self.is_valid:
            return "=> Security Request \n" + "\t- Url: " + self.url + "\n\t- Method: " + self.method + str(self.header_report)
        else:
            return "Malformed HTTP request."
