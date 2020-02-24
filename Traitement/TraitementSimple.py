# -*- coding: utf-8 -*-
import utils
from nltk.tokenize import word_tokenize
from Traitement import Traitement
import string

class TraitementSimple(Traitement):
    def __init__(self,lang):
        self.lang=lang

    def preprocessing(self,texte):
        """
        param texte : le texte non traité
        param lang : la langue dans laquelle le texte est écrit

        Renvoie une liste des mots traités

        Le traitement consiste à mettre tout les mots en minuscule,
        retirer les mots vides et la ponctuation.
        """
        #on met tout en minuscule
        txt = texte.lower()

        #segmentation des mots
        words = word_tokenize(txt, self.lang)

        #retire les mots vides
        words = utils.removeStopWords(words, self.lang)

        #retire la ponctuation
        #words = utils.removePunctuation(words)

        words = utils.removeNoWord(words)

        return [(word,) for word in words]
