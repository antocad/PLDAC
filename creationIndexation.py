import sys
sys.path.append("./Parser")
sys.path.append("./Traitement")
sys.path.append("./Indexation")
sys.path.append("./Document")
import pickle
from Indexation import Indexation
from Corpus import Corpus
import utils
from TraitementSimple import TraitementSimple
from TraitementNGrams import TraitementNGrams
#from TraitementNGramsSpacy import TraitementNGramsSpacy
from ParserCorpus import ParserCorpus

nomfichier = "indexation5Grams_wikimed"
fichierCorpus = "wikimed.txt"

corpus = ParserCorpus.parse(fichierCorpus)
trait = TraitementNGrams(1,5,'French')
corpusTraite = utils.traiteCorpus(corpus,trait)
ind = Indexation(corpusTraite)

with open(nomfichier, 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(ind)
