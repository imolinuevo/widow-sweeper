class HttpHeaderReport(object):

    def __init__(self, headers):
        self.x_frame_options = headers.get("X-Frame-Options", "None")
        self.x_xss_protection = headers.get("X-XSS-Protection", "None")
        self.x_content_type_options = headers.get("X-Content-Type-Options", "None")
        self.content_type = headers.get("Content-Type", "None")
        self.validate_headers()

    def validate_headers(self):
        self.validated_x_frame_options = self.validate_header(self.x_frame_options, "sameorigin")
        self.validated_x_xss_protection = self.validate_header(self.x_xss_protection, "1;mode=block")
        self.validated_x_content_type_options = self.validate_header(self.x_content_type_options, "nosniff")
        self.validated_content_type = self.validate_header(self.content_type, "text/html;charset=utf-8")

    def validate_header(self, actual, expected):
        if actual:
            if str(actual).lower().replace(" ", "") == expected:
                return "Safe header"
            else:
                return "Invalid header, should be: " + expected
        else:
            return "Header is missing"

    def __str__(self):
        return """
        - Security headers status:
            :: X-Frame-Options: """ + self.validated_x_frame_options + """
            :: X-XSS-Protection: """ + self.validated_x_xss_protection + """
            :: X-Content-Type-Options: """ + self.validated_x_content_type_options + """
            :: Content-Type: """ + self.validated_content_type + """"""
