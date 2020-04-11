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
from TraitementNGramsSpacy import TraitementNGramsSpacy
from ParserCorpus import ParserCorpus

nomfichier = "indexationSpacy7StemGroupmax_wikimed"
fichierCorpus = "wikimed.txt"
STEM=True
GROUPMAX=True

corpus = ParserCorpus.parse(fichierCorpus)
print('taille du corpus :',len(corpus.collection))
trait = TraitementNGramsSpacy(1,7,'French',GROUPMAX)
corpusTraite = utils.traiteCorpus(corpus,trait)
ind = Indexation(corpusTraite,stem=STEM)

with open(nomfichier, 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(ind)
