#!python
# coding: utf-8

"""
xkcd-wrapper related exceptions
"""


class XkcdWrapperException(Exception):
    """Base exception class"""


class HttpError(XkcdWrapperException):
    """
    HTTP status code received was not 200 OK

    Attributes
    ----------
    status_code : int
        http status code
    message : str
        http text corresponding to status code
    """
    def __init__(self, status_code, message):
        super().__init__()
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return 'Received HTTP status code {}: {}. Expected 200: OK'.format(self.status_code,
                                                                           self.message)


class BadResponseField(XkcdWrapperException):
    """
    API response field could not be converted to int
    """
    def __init__(self, wrapper_field, api_field, original_error):
        super().__init__()
        self.wrapper_field = wrapper_field
        self.api_field = api_field
        # select the string causing the problem from the ValueError error message
        self.wrong_field = str(original_error).split(':', maxsplit=1)[1][2:-1]

    def __str__(self):
        return 'Xkcd API returned a non int value on the "{}" field (for wrapper "{}" field): ' \
               '"{}". Please report this issue on GitHub: ' \
               'https://github.com/Kronopt/xkcd-wrapper'.format(
                   self.api_field, self.wrapper_field, self.wrong_field)
