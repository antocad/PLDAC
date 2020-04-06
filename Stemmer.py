# -*- coding: utf-8 -*-
import sys
sys.path.append("./Document")
from nltk.stem import SnowballStemmer
from Corpus import Corpus
from Document import Document

class Stemmer:
    def __init__(self):
        self.stemmer = SnowballStemmer('french')
    
    def stem(self,corpusTraite):
        mem = dict()
        corpusStem = Corpus()
        for doc in corpusTraite:
            content = []
            for term in doc.content:
                termStem = []
                for mot in term:
                    termStem.append(self.stemmer.stem(mot))
                termStem = tuple(termStem)
                content.append(termStem)
                if termStem not in mem:
                    mem[termStem]={term:1}
                else:
                    if term not in mem[termStem]:
                        mem[termStem][term]=1
                    else:
                        mem[termStem][term]+=1
            corpusStem.addDocument(Document(doc.title,content))
        return mem,corpusStem