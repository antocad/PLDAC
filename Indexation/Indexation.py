# -*- coding: utf-8 -*-
from collections import Counter

class Indexation:
    def __init__(self,corpusTraite):
        self.corpus = corpusTraite
        self.index = None
        self.indexInv = None

    def getIndex(self):
        if(self.index == None):
            self.calculIndex()
        return self.index

    def getIndexInv(self):
        if(self.indexInv == None):
            self.calculIndex()
        return self.indexInv

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
