
"""
This is essentially an interface for other converter classes,
these methods MUST be present!
"""

class BaseConverter:
    def get_file(self):
        raise NotImplementedError()

    def get_filename(self):
        raise NotImplementedError()

    def is_inline(self):
        raise NotImplementedError()

    def get_content_id(self):
        raise NotImplementedError()