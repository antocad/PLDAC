import sys
import math

from Strategy import Strategy
sys.path.append('../Indexation')
from Indexation import Indexation
from collections import Counter
from TfIdfStrategy import TfIdfStrategy
from CValueStrategy import CValueStrategy

class CValueTfidfStrategy(Strategy):
    def __init__(self,indexationGeneraliste,formuletfifd,formuleAgregation,seuil=0):
        """
        indexationGeneraliste : objet indexation d'un corpus generaliste pre-calculé
        formule est une fonction à 2 argument qui prend tf et idf qui renvoie le score
        formuleAgregation : prend un iterable en params
        """
        self.formuletfifd = formuletfifd
        self.formuleAgregation = formuleAgregation
        self.indexation = indexationGeneraliste
        self.seuil = seuil

    def execute(self,corpusTraite):
        strattfidf = TfIdfStrategy(self.indexation,self.formuletfifd,self.formuleAgregation,self.seuil)
        tfidf = strattfidf.execute(corpusTraite)
        stratcvalue = CValueStrategy(self.indexation,self.seuil)
        cvalue = stratcvalue.execute(corpusTraite)
        #normalise cvalue
        tot = sum(cvalue.values())
        for terme in cvalue.keys():
            cvalue[terme]/=tot

        dictTermeScore = dict()
        for terme,scoretfidf in tfidf.items():
            scorecvalue = cvalue[terme]
            score = (2*scoretfidf*scorecvalue)/(scoretfidf+scorecvalue)
            dictTermeScore[terme] = score
        return dictTermeScore
