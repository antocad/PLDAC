# -*- coding: utf-8 -*-
import sys
sys.path.append("../Parser")
sys.path.append("../Traitement")
sys.path.append("../Document")
from Corpus import Corpus
from Document import Document
from Indexation import Indexation
from TraitementNGrams import TraitementNGrams
from utils import traiteCorpus
import math

trait = TraitementNGrams(1,2,'French')
doc1 = 'Je fais une Phrase pour tester le prétraitement n-grams pour tester.'
doc2 = 'Je fais un test d\'indexation.'
corpus = Corpus()
corpus.addDocument(Document('doc1',doc1))
corpus.addDocument(Document('doc2',doc2))
corpusTraite = traiteCorpus(corpus,trait)
ind = Indexation(corpusTraite)

index = ind.getIndex()
indexinv = ind.getIndexInv()

print(index)
print("-"*100)
print(indexinv)
