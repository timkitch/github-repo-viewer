import base64

class CodeFormatter:
    @staticmethod
    def decode_content(content, encoding):
        return content.decode(encoding)