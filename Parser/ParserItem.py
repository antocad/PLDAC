import sys
import re
sys.path.append("../Document")
from Corpus import Corpus
from Document import Document
from Parser import Parser

class ParserItem(Parser):
    @staticmethod
    def parse(path):
        """
        """
        corpus = Corpus()

        with open(path,'r',encoding='utf-8') as f :
            txt = f.read()
        listedoc = [txt]
        #re.split('^Items? .* \.',txt,flags=re.MULTILINE)
        for content in listedoc:
            corpus.addDocument(Document('', content))
        return corpus
