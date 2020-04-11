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
from CValueTfidfStrategy import CValueTfidfStrategy
from TraitementSimple import TraitementSimple
from TraitementNGrams import TraitementNGrams
from TraitementNGramsSpacy import TraitementNGramsSpacy
import Extractor
from ParserItem import ParserItem
from ParserCorpus import ParserCorpus
from statistics import mean
from collections import Counter

nomfichierPickle = "indexationSpacy7StemGroupmax_wikimed"
fichierExtration = "livre2clean.txt"
STEM=True
SEUIL=0
GROUPMAX=True
fichierres = 'res/reslivre2cvaluestemgroupmax.csv'

#traitement
trait = TraitementNGramsSpacy(1,7,'French',GROUPMAX)

#recup l'indexation
with open(nomfichierPickle, 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    ind = mon_depickler.load()

#recup le doc du quel on extrait les termes
corpus = ParserItem.parse(fichierExtration)
corpusTraite = utils.traiteCorpus(corpus,trait)
"""doc = list(corpusTraite.collection.values())[0]
freq = dict(Counter(doc.content))
freq = sorted(list(freq.items()),key=lambda e:e[1],reverse=True)
tmpres=''
for t,occ in freq:
    tmpres+= ' '.join(t)+';'+str(occ)+'\n'
with open('freqlivrePretcleangm.txt','w',encoding='utf-8') as f:
    f.write(tmpres)"""

#strat = CValueStrategy(ind,seuil=SEUIL)
strat = CValueTfidfStrategy(ind,  lambda tf,idf : (1+math.log(tf))*idf,  lambda iter : max(iter),seuil=SEUIL)
#strat = TfIdfStrategy(ind,  lambda tf,idf : (1+math.log(tf))*idf,  lambda iter : max(iter),seuil=SEUIL)
Extractor.Extractor.extract(corpusTraite,strat,-1,fichierres,stem=STEM)
