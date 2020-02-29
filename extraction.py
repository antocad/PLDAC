import sys
sys.path.append("./Parser")
sys.path.append("./Traitement")
sys.path.append("./Indexation")
sys.path.append("./Document")
sys.path.append("./Strategy")
import pickle
from Indexation import Indexation
from Document import Document
import utils
import math
from TfIdfStrategy import TfIdfStrategy
from CValueStrategy import CValueStrategy
from TraitementSimple import TraitementSimple
from TraitementNGrams import TraitementNGrams
import Extractor
from ParserItem import ParserItem
from statistics import mean

nomfichierPickle = "indexationSimple_wikimed"
fichierExtration = "LivrePret.txt"
fichierres = 'res/restfidfsimple_newavg.csv'
trait = TraitementSimple('French')

#recup l'indexation
with open(nomfichierPickle, 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    ind = mon_depickler.load()

#recup le doc du quel on extrait les termes
corpus = ParserItem.parse(fichierExtration)
corpusTraite = utils.traiteCorpus(corpus,trait)


strat = TfIdfStrategy(ind,  lambda tf,idf : tf*idf,  lambda iter : mean(iter))
Extractor.Extractor.extract(corpusTraite,strat,-1,fichierres)
