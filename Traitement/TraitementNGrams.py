# -*- coding: utf-8 -*-
from Traitement import Traitement
from TraitementSimple import TraitementSimple
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
#from nltk import ngrams
import utils
import string

def ngrams(liste,k):
    stop_words = utils.stopwordsSet().union({chr(97+l)+"'" for l in range(26)})
    if(k+1>len(liste)):
        return []
    res = []
    #premier
    tmp = liste[0:k+1]
    if(tmp[-1] in stop_words or tmp[-1] in string.punctuation):
        tmp = tmp[0:-1]
        if(tmp[0] not in stop_words and tmp[-1] not in stop_words):
            ok=True
            for mot in tmp:
                if(mot in string.punctuation):
                    ok = False
                    break
            if(ok and len(tmp)==1 and (len(tmp[0])==1 or tmp[0].isdigit())):
                ok = False
            if(ok):
                res.append(tuple(tmp))
    #suite
    for i in range(1,len(liste)-k):
        tmp = liste[i-1:i+k+1]
        if(tmp[0] not in stop_words and tmp[0] not in string.punctuation):
            continue
        if(tmp[-1] not in stop_words and tmp[-1] not in string.punctuation):
            continue
        tmp = tmp[1:-1]
        if(tmp[0] not in stop_words and tmp[-1] not in stop_words):
            ok=True
            for mot in tmp:
                if(mot in string.punctuation):
                   ok = False
                   break
            if(ok and len(tmp)==1 and (len(tmp[0])==1 or tmp[0].isdigit())):
                ok = False
            if(ok):
                res.append(tuple(tmp))
    return res

class TraitementNGrams(Traitement):
    def __init__(self, k,n, lang):
        self.k = k
        self.n = n
        self.lang=lang
        self.stop_words = set(stopwords.words(self.lang))

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
        #retire les mots vides
        #words = utils.removeStopWords(words, self.lang)
        txtsplit =  word_tokenize(txt,self.lang)
        tmp = []
        for m in txtsplit:
            if("'" not in m):
                tmp.append(m)
            else:
                mots = m.split("'")
                tmp.append(mots[0]+"'")
                tmp.append(mots[1])
        txtsplit = tmp
        txtsplit = [mot for mot in txtsplit if mot not in {'--','––'}]
        words = []
        for k in range(self.k,self.n+1):
            words += ngrams(txtsplit, k)

        return words#[gram for gram in words if gram[0] not in stop_words and gram[-1] not in stop_words]#on retire les ngram qui commence ou fini par un stop words
