"""
The exceptions module contains Exception subclasses where instances might be
raised by Wren.
"""

class WrenException(Exception):

    """An error during your request occurred.
    Super class for all Wren errors
    """

    def __init__(self, message, error_type=None):
        self.type = error_type
        self.message = message
        if error_type is not None:
            self.message = '%s: %s' % (error_type, message)

        super(WrenException, self).__init__(self.message)


class ArticleException(WrenException):
    pass

class PodcastException(WrenException):
    pass

class VideoException(WrenException):
    pass