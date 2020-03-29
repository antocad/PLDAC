# -*- coding: utf-8 -*-
import sys
sys.path.append("../Parser")
sys.path.append("../Traitement")
sys.path.append("../Indexation")
from ParserDocument import ParserDocument
from ParserCorpus import ParserCorpus
from Indexation import Indexation
from TraitementNGrams import TraitementNGrams
from CValueStrategy import CValueStrategy
from Document import Document
import utils


corpusGene = ParserCorpus.parse("../wikimed.txt")
#print(corpusGene.size())
trait = TraitementNGrams(3,'French')
corpusGeneTraite = utils.traiteCorpus(corpusGene,trait)
ind = Indexation(corpusGeneTraite)
text=''
with open("../livrePret.txt",'r',encoding="utf-8") as f :
	text = f.read()
doc = Document('livre',text)
docTraite = utils.traiteDocument(doc,trait)

strat = CValueStrategy(docTraite,ind)
res = strat.execute()
with open('rescvalue.txt','w',encoding='utf-8') as f :
    for i,t in enumerate(res):
        f.write(str(i)+';'+' '.join(list(t[0]))+';'+str(t[1])+'\n')
#res = strat.calculTermesImbriques()
#print(res)
#print('-'*100)
#print(res[('programmation',)])
