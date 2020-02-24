# -*- coding: utf-8 -*-
import sys
sys.path.append("../Parser")
sys.path.append("../Traitement")
from ParserCorpus import ParserCorpus
from Indexation import Indexation
from TraitementSimple import TraitementSimple
from utils import traiteCorpus

corpus = ParserCorpus.parse("../corpus_short.fr")
trait = TraitementSimple('French')
corpusTraite = traiteCorpus(corpus,trait)
ind = Indexation(corpusTraite)

index = ind.getIndex()
indexinv = ind.getIndexInv()
