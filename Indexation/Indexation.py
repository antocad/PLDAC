# -*- coding: utf-8 -*-
from collections import Counter
import math
import sys
sys.path.append("..")
from Stemmer import Stemmer

class Indexation:
    def __init__(self,corpusTraite,stem=True):
        if(stem):
            s=Stemmer()
            _,self.corpus = s.stem(corpusTraite)
        else:
            self.corpus = corpusTraite
        self.index = None
        self.indexInv = None
        self.calculIndex()

    def getIndex(self):
        return self.index

    def getIndexInv(self):
        return self.indexInv

    def getIDFTerme(self,terme):
        nbdoc = self.corpus.size()
        if (terme not in self.indexInv.keys()):
            val = 0
        else:
            val = len(self.indexInv[terme])
        return math.log((1+nbdoc)/(1+val))

    def calculIndex(self):
        self.index = dict()
        self.indexInv = dict()

        #calcul index
        for doc in self.corpus :
            words = doc.getContent()
            self.index[doc.getId()] = dict(Counter(words))

        #calcul index inverse
        for doc, occs in self.index.items():
            for mot, occ in occs.items():
                if(mot not in self.indexInv):
                    self.indexInv[mot]={doc:occ}
                else:
                    self.indexInv[mot][doc] = occ
