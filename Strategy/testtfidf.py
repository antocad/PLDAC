# -*- coding: utf-8 -*-
import sys
sys.path.append("../Parser")
sys.path.append("../Traitement")
sys.path.append("../Indexation")
from ParserArticle import ParserArticle
from Indexation import Indexation
from TraitementSimple import TraitementSimple
from TfIdfStrategy import TfIdfStrategy
import utils

corpusGene = ParserArticle.parse("../corpus_short.fr")
trait = TraitementSimple('French')
corpusGeneTraite = utils.traiteCorpus(corpusGene,trait)
ind = Indexation(corpusGeneTraite)

corpus = ParserArticle.parse("../testExtract.fr")
docTraite = utils.traiteDocument(corpus.collection[list(corpus.collection.keys())[0]],trait)

strat = TfIdfStrategy(docTraite,ind)
termes = strat.execute()
for t in termes:
	print(t[0])
