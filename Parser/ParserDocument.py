import sys
import re
sys.path.append("../Document")
from Document import Document
from Parser import Parser

class ParserDocument(Parser):
    @staticmethod
    def parse(path):
        regex=r'<article title=\"(.*?)\">\n(.*?)</article>'

        file = open(path, "r", encoding="utf-8")
        reader = file.read()
        title,content = re.findall(regex, reader, re.DOTALL)[0]
        
        return Document(title, content)
