import sys
import math

from Strategy import Strategy
sys.path.append('../Indexation')
from Indexation import Indexation
from collections import Counter

class TfIdfStrategy(Strategy):
    def __init__(self,docTraite,indexationGeneraliste):
        """
        indexationGeneraliste : objet indexation d'un corpus generaliste pre-calculé
        """
        self.indexationGeneraliste = indexationGeneraliste
        self.index = indexationGeneraliste.getIndex()
        self.indexInv = indexationGeneraliste.getIndexInv()
        self.doc = docTraite

    def execute(self):
        listTermeScore = []
        nbdoc = len(self.index)
        tfDoc = dict(Counter(self.doc.content))
        for mot,tf in tfDoc.items():
            if (mot not in self.indexInv.keys()):
                val = 0
            else:
                val = len(self.indexInv[mot])
            #calcul tfidf
            idf = math.log((1+nbdoc)/(1+val))
            listTermeScore.append( (mot, tf*idf) )
        return sorted(listTermeScore, key=lambda t: t[1], reverse=True)
