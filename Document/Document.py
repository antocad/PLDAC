# -*- coding: utf-8 -*-
class Document():
    """
    Objet Document qui stocke son titre, son contenu et offre des
    fonctionnalités d'accès aux attributs et de visualisation du document.
    """
    cpt = 0
    def __init__(self, title, content):
        """
        param title : le titre du document
        param content : le contenu du document
        """
        self.id = Document.cpt
        Document.cpt+=1
        self.title = title
        self.content = content

    def getTitle(self):
        """
        renvoie le titre du document
        """
        return self.title

    def getId(self):
        """
        renvoie l'id du document
        """
        return self.id

    def getContent(self):
        """
        renvoie le contenu du document
        """
        return self.content

    def show(self):
        """
        affiche le document
        """
        print("Title: "+self.title)
        print(self.content)
