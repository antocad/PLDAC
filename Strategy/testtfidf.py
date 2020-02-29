# -*- coding: utf-8 -*-
import sys
sys.path.append("../Parser")
sys.path.append("../Traitement")
sys.path.append("../Indexation")
from ParserDocument import ParserDocument
from ParserCorpus import ParserCorpus
from Indexation import Indexation
from TraitementSimple import TraitementSimple
from TraitementNGrams import TraitementNGrams
from TfIdfStrategy import TfIdfStrategy
from Document import Document
import utils

corpusGene = ParserCorpus.parse("../wikimed.txt")
trait = TraitementNGrams(3,'French')
corpusGeneTraite = utils.traiteCorpus(corpusGene,trait)
ind = Indexation(corpusGeneTraite)

text=''
with open("../livrePret.txt",'r',encoding="utf-8") as f :
	text = f.read()
doc = Document('livre',text)
docTraite = utils.traiteDocument(doc,trait)

strat = TfIdfStrategy(docTraite,ind)
res = strat.execute()
with open('restfidf.txt','w',encoding='utf-8') as f :
    for i,t in enumerate(res):
        f.write(str(i)+';'+' '.join(list(t[0]))+';'+str(t[1])+'\n')
