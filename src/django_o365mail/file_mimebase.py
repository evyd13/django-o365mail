from .file_base import BaseConverter
from email.mime.base import MIMEBase
import base64
import re
import io


def get_charset(content_type):
    """
    Function to get charset from content-type string such as
    'text/plain; charset="utf-8"', else it returns ascii
    """
    type = re.search(r'charset=.([A-Za-z0-9-./]+).', content_type)
    return type.group(1) if type else 'ascii'


class MIMEObjectToFileObject(BaseConverter):
    def __init__(self, obj):
        assert isinstance(obj, MIMEBase) == True, "Object must be an instance of MIMEBase!"
        self.obj = obj

    def get_file(self):
        """Returns a file-like object, in this case a BytesIO object."""
        content_type = self.obj.get('Content-Type') # 'text/plain; charset="utf-8"' or 'application/octet-stream' etc

        self.mimetype = re.search(r'^([A-Za-z0-9-./]+)', content_type).group(0)
        self.charset = get_charset(content_type)
        self.encoding = self.obj.get('Content-Transfer-Encoding') # 'base64' or '7bit' etc
        self.content = self.decode_content(self.obj.get_payload())
        self.filename = self.obj.get_filename() or 'untitled'
        
        return io.BytesIO(self.content)

    def decode_content(self, content):
        """Returns a byte object"""
        if self.encoding == 'base64':
            return self.decode_base64(content)
        else:
            return content.encode(self.charset)

    def decode_base64(self, content):
        return base64.b64decode(content.encode(self.charset))

    def get_filename(self):
        return self.filename

    def is_inline(self):
        return (self.get_content_id() is not None)

    def get_content_id(self):
        return self.obj.get('Content-ID')