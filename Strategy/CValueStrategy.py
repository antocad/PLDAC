import sys
import math
import numpy as np

from Strategy import Strategy
from TfIdfStrategy import TfIdfStrategy
sys.path.append('../Indexation')
from Indexation import Indexation
from collections import Counter
sys.path.append('../Document')
from Corpus import Corpus

class CValueStrategy(Strategy):
    def __init__(self, docTraite, indexationGeneraliste):
        """
        indexationGeneraliste : objet indexation d'un corpus generaliste pre-calculé
        """
        self.doc = docTraite
        corpus_query = Corpus()
        corpus_query.addDocument(self.doc)
        self.indexation_query = Indexation(corpus_query)
        self.strategyTfIdf = TfIdfStrategy(docTraite, indexationGeneraliste)
        self.tfIdf = self.strategyTfIdf.execute()
        self.imbrications = self.calculTermesImbriques()
    
    def execute(self):
        listTermeScore = []
        for gram,tfidf in self.tfIdf:
            A = gram
            nA = len(gram)
            fA = list(self.indexation_query.getIndexInv()[A].values())[0]
            CValue = 0
            SA = self.imbrications[gram]
            nSA = len(SA)
            #si A n'est pas imbriqué
            if nSA == 0:
                CValue = np.log2(nA+1) * fA
            else:
                sumB = np.sum([list(self.indexation_query.getIndexInv()[b].values())[0] for b in SA]) 
                CValue = np.log2(nA+1) * (fA - 1/nSA * sumB)
                
            nbdoc = len(self.strategyTfIdf.index)
            if (gram not in self.strategyTfIdf.indexInv.keys()):
                val = 0
            else:
                val = len(self.strategyTfIdf.indexInv[gram])
            idf = math.log((1+nbdoc)/(1+val))
                
            listTermeScore.append( (gram, CValue*idf) )
            
        return sorted(listTermeScore, key=lambda t: t[1], reverse=True)

    def calculTermesImbriques(self):
        ensTermes = set(self.doc.content)
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