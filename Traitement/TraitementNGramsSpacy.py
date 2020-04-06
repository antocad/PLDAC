import spacy
from Traitement import Traitement
import string
import utils


class TraitementNGramsSpacy(Traitement):
    def __init__(self, k,n, lang):
        self.k = k
        self.n = n
        self.lang=lang

    def preprocessing(self,texte):
        """
        param texte : le texte non traité
        param lang : la langue dans laquelle le texte est écrit

        Renvoie une liste des mots traités

        Le traitement consiste à mettre tout les mots en minuscule,
        retirer les mots vides et la ponctuation.
        """
        nlp = spacy.load("fr")
        nlp.max_length=len(texte)#attention on change la limite peut etre allocation errors 
        txt = texte.replace('\n',' ').lower()
        doc = nlp(txt)
        noms = [t for t in doc if t.pos_=='NOUN' and t.head.pos_!='NOUN']#on retire tous ceux qui depen d'un nom(groupe max)
        res = [[m for m in n.subtree] for n in noms]
        stop_words =  utils.stopwordsSet().union({chr(97+l)+"'" for l in range(26)})
        for term in res:
            while(len(term)>0 and (term[0].text in stop_words or term[0].text in string.punctuation+string.whitespace)):
                term.pop(0)
            while(len(term)>0 and (term[-1].text in stop_words or term[-1].text in string.punctuation+string.whitespace)):
                term.pop(-1)

        return [tuple([t.text for t in term]) for term in res if len(term)>=self.k and len(term)<=self.n and not (len(term)==1 and ( len(term[0].text) == 1 or term[0].text.isdigit() ) )]
