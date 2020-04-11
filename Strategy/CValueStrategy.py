import sys
import math
sys.path.append("../Document")

from Strategy import Strategy
from collections import Counter
from Document import Document

class CValueStrategy(Strategy):
    def __init__(self,indexation,seuil):
        self.indexation= indexation
        self.indexInv = indexation.getIndexInv()
        self.index = indexation.getIndex()
        self.seuil = seuil
        
    def execute(self,corpusTraite):
        docTraite = Document('',[])
        for doc in corpusTraite:
            docTraite.content += doc.content
        freq = dict(Counter(docTraite.content))
        
        #seuil
        if(self.seuil>0):
            termSeuil = {t for t,occ in freq.items() if occ>=self.seuil}
            docTraite.content = [t for t in docTraite.content if t in termSeuil]
        
        dictTermeScore = dict()
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
            score *=  math.log2(nbmot+1)#+1 pour les single-word
            #idf = self.indexation.getIDFTerme(terme)
            #score*=idf
            dictTermeScore[terme] = score
        return dictTermeScore

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
