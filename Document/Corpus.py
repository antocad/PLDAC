# -*- coding: utf-8 -*-
from Document import *

class Corpus():
    """
    Objet Corpus qui stocke une collection de documents
    offre des fonctionnalités d'accès aux documents, à la collection et à sa
    taille.
    """
    def __init__(self):
        self.collection = dict()

    def __iter__(self):
        return self.collection.values().__iter__()

    def addDocument(self,doc):
        self.collection[doc.getId()]=doc

    def getDocumentById(self, id):
        """
        INT -> DOCUMENT
        param id : l'id du document à rechercher dans le corpus

        renvoie le document du corpus correspondant à l'id, None s'il n'est
        pas présent.
        """
        if(id in self.collection):
            return self.collection[id]
        return None

    def size(self):
        """
        renvoie la taille du corpus (nombre de documents)
        """
        return len(self.collection)

    def getCollection(self):
        """
        renvoie la collection des documents
        """
        return self.collection
