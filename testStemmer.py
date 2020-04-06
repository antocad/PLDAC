# -*- coding: utf-8 -*-
import sys
sys.path.append("./Parser")
sys.path.append("./Traitement")
sys.path.append("./Indexation")
sys.path.append("./Document")
sys.path.append("./Strategy")
import utils
from TraitementSimple import TraitementSimple
from TraitementNGrams import TraitementNGrams
from TraitementNGramsSpacy import TraitementNGramsSpacy
from ParserItem import ParserItem
from Stemmer import Stemmer


fichierExtration = "livrePretclean.txt"
trait = TraitementNGramsSpacy(1,5,'French')

#recup le doc du quel on extrait les termes
corpus = ParserItem.parse(fichierExtration)
corpusTraite = utils.traiteCorpus(corpus,trait)

s=Stemmer()
memStem,corpusStem = s.stem(corpusTraite)
