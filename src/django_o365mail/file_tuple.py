from .file_base import BaseConverter
import io


class TupleToFileObject(BaseConverter):
    def __init__(self, obj):
        assert isinstance(obj, tuple) == True, "Object must be an instance of tuple!"
        self.obj = obj

    def get_file(self):
        """Returns a file-like object, in this case a BytesIO object."""

        # A tuple instance has three parts: filename, byte-encoded contents, mimetype
        self.filename = self.obj[0]
        self.content = self.obj[1].encode() if isinstance(self.obj[1], str) else self.obj[1]
        self.mimetype = self.obj[2]

        return io.BytesIO(self.content)
    
    def get_filename(self):
        return self.filename

    def is_inline(self):
        return False

    def get_content_id(self):
        return None