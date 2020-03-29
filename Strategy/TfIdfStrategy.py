import sys
import math

from Strategy import Strategy
sys.path.append('../Indexation')
from Indexation import Indexation
from collections import Counter

class TfIdfStrategy(Strategy):
    def __init__(self,indexationGeneraliste,formuletfifd,formuleAgregation):
        """
        indexationGeneraliste : objet indexation d'un corpus generaliste pre-calculé
        formule est une fonction à 2 argument qui prend tf et idf qui renvoie le score
        formuleAgregation : prend un iterable en params
        """
        self.formuletfifd = formuletfifd
        self.formuleAgregation = formuleAgregation
        self.indexation = indexationGeneraliste
        self.index = indexationGeneraliste.getIndex()
        self.indexInv = indexationGeneraliste.getIndexInv()

    def execute(self,corpusTraite):
        dictTermeScore = dict()
        indexerCorpus = Indexation(corpusTraite)
        index = indexerCorpus.getIndex()
        tfidfindex = dict()
        for doc,term_occ in index.items():
            tmp = dict()
            for term, tf in term_occ.items():
                idf = self.indexation.getIDFTerme(term)
                tfidf = self.formuletfifd(tf,idf)
                tmp[term]=tfidf
            tfidfindex[doc] = tmp
        normaliseIndex(tfidfindex)
        tfidfindexinv = inverseIndex(tfidfindex)
        for term,doc_tfidf in tfidfindexinv.items():
            dictTermeScore[term] = self.formuleAgregation(doc_tfidf.values())
        return dictTermeScore

def normaliseIndex(index):
    for doc,term_tfidf in index.items():
        tot = sum(term_tfidf.values())
        for term in term_tfidf.keys():
            index[doc][term]/=tot

def inverseIndex(index):
    res = dict()
    for doc,mots in index.items():
        for mot,occ in mots.items():
            if mot not in res:
                res[mot]={doc:occ}
            else:
                res[mot][doc] = occ
    return res
