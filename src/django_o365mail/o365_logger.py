import logging


class SimpleErrorHandler(logging.Handler):
    level = logging.ERROR
    exceptions = None
    
    def __init__(self):
        self.exceptions = []
        super().__init__()
    
    def handle(self, record):
        self.exceptions.append(record.getMessage())
        self.exceptions = self.exceptions[:5]

    def get_message(self):
        message = None
        if self.exceptions:
            message = self.exceptions[-1]
            self.exceptions.remove(message)
        return message
    
    def flush(self):
        self.exceptions = []
