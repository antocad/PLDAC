import sys
import re
sys.path.append("../Document")
from Corpus import Corpus
from Document import Document
from Parser import Parser

class ParserCorpus(Parser):
    @staticmethod
    def parse(path):
        """
        """
        regex=r'<article title=\"(.*?)\">\n(.*?)</article>'
        corpus = Corpus()

        file = open(path, "r", encoding="utf-8")
        reader = file.read()
        parser = re.findall(regex, reader, re.DOTALL)
        for title,content in parser:
            corpus.addDocument(Document(title, content))
        return corpus
