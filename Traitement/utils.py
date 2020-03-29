from nltk.corpus import stopwords
import string

def removeStopWords(words, lang='French'):
    """
    param words : liste de mots
    param lang : la langue des mots de la liste

    Renvoie une liste de mots sans les mots vides.
    """
    res = []
    stop_words = stopwordsSet
    for w in words:
        if(w not in stop_words):
            res.append(w)
    return res

def removePunctuation(words):
    """
    param words : liste de mots

    Renvoie la liste de mots privée de la ponctuation.
    """
    res = []
    for w in words :
        if(w not in string.punctuation):
            res.append(w)
    return res

def traiteDocument(doc, traitement):
    """
    Renvoie le document traité à l'aide de l'objet traitement passé en paramétre
    """
    doc.content = traitement.preprocessing(doc.content)
    return doc

def traiteCorpus(corpus, traitement):
    """
    Renvoie le corpus traité à l'aide de l'objet traitement passé en paramétre
    """
    for doc in corpus:
        traiteDocument(doc,traitement)
    return corpus

def removeNoWord(words):
    """
    Retire tout les non mots c'est à dire tout les mots qui ne sont composés
    d'aucune lettre
    """
    res=[]
    for word in words:
        if(not noWord(word)):
            res.append(word)
    return res

def noWord(word):
    """
    Renvoie True si le mot est un non mot c'est à dire composé
    d'aucune lettre
    """
    for l in word:
        if(l>='a' and l<='z' or l=='à'):
            return False
    return True

def stopwordsSet():
    with open('stopwords.fr','r', encoding='utf-8') as f:
        return set(f.read().split('\n'))
