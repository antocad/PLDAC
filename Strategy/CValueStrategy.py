import sys
import math

from Strategy import Strategy
from collections import Counter

class CValueStrategy(Strategy):
    def __init__(self,indexation):
        self.indexation= indexation
        self.indexInv = indexation.getIndexInv()
        self.index = indexation.getIndex()

    def execute(self,docTraite):
        freq = dict(Counter(docTraite.content))
        listTermeScore = []
        termesImb = self.calculTermesImbriques(docTraite)
        for terme,ensTermes in termesImb.items():
            nbmot = len(terme)
            if(len(ensTermes)==0):
                score = freq[terme]
            else:
                somme=0
                for t in ensTermes:
                    somme += freq[t]
                score = (freq[terme] - (1/len(ensTermes)) * somme )
            score *=  math.log(nbmot+1)
            idf = self.indexation.getIDFTerme(terme)
            score*=idf
            listTermeScore.append((terme,score))
        return sorted(listTermeScore, key=lambda t: t[1], reverse=True)

    def calculTermesImbriques(self,docTraite):
        ensTermes = set(docTraite.content)
        res = dict()
        for terme in ensTermes:
            if(terme not in res):
                res[terme] = set()
            nbmot = len(terme)
            for taille in range(1,nbmot):
                for i in range(0,nbmot-taille+1):
                    sousterme = terme[i:i+taille]
                    if(sousterme in ensTermes):
                        if(sousterme not in res):
                            res[sousterme] = {terme}
                        else:
                            res[sousterme].add(terme)
        return res
