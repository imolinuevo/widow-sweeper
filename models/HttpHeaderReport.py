class HttpHeaderReport(object):

    def __init__(self, headers):
        self.validated_x_frame_options = self.validate_header(headers.get("X-Frame-Options", None), "sameorigin")
        self.validated_x_xss_protection = self.validate_header(headers.get("X-XSS-Protection", None), "1;mode=block")
        self.validated_x_content_type_options = self.validate_header(headers.get("X-Content-Type-Options", None), "nosniff")
        self.validated_content_type = self.validate_header(headers.get("Content-Type", "None"), "text/html;charset=utf-8")

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
            :: X-Frame-Options: {}
            :: X-XSS-Protection: {}
            :: X-Content-Type-Options: {}
            :: Content-Type: {}""".format(
                self.validated_x_frame_options,
                self.validated_x_xss_protection,
                self.validated_x_content_type_options,
                self.validated_content_type
            )
