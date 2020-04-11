import spacy
from Traitement import Traitement
import string
import utils


class TraitementNGramsSpacy(Traitement):
    def __init__(self, k,n, lang,groupmax):
        self.k = k
        self.n = n
        self.lang=lang
        self.nlp = spacy.load("fr")
        self.i = 0#debug
        self.groupmax = groupmax

    def preprocessing(self,texte):
        """
        param texte : le texte non traité
        param lang : la langue dans laquelle le texte est écrit

        Renvoie une liste des mots traités

        Le traitement consiste à mettre tout les mots en minuscule,
        retirer les mots vides et la ponctuation.
        """
        #pour le controle 
        #if(self.i%100==0):
        #    print(self.i)
        #self.i+=1
        
        txt = texte.replace('\n',' ').lower()
        if(self.nlp.max_length < len(txt)):
            self.nlp.max_length=len(txt)#attention on change la limite peut etre allocation errors 
        doc = self.nlp(txt)
        
        #soit sa tête c'est lui meme soit on prend pas le groupe max soit sa tete est un nom
        noms = set([t for t in doc if t.pos_=='NOUN' and  (not self.groupmax or t.head==t or t.head.pos_!='NOUN')])#on retire tous ceux qui dependent d'un nom(groupe max)
        if(self.groupmax):
            noms2 = noms.copy()
            noms2 = sorted(noms2,key=lambda n:len(list(n.subtree)))
            for n in noms2:
                elem = list(n.subtree)
                nomselem = [e for e in elem if e.pos_=='NOUN' and e!=n]
                for e in nomselem:
                    if e in noms:
                        noms.remove(e)
        
        res = [[m for m in n.subtree] for n in noms]#recup groupe nominaux
        
        """
        #############################################
        #coupe au niveau des conjonctions
        restmp=[]
        for term in res:
            icoupe=[]#contient toutes les coupures à faire
            for i,mot in enumerate(term):#car si au debut ou la fin le mot sera retiré plus tard et n'est pas une coupure
                if mot.pos_=='CCONJ' or mot.text in ',.':
                    icoupe.append(i)#ajout d'une coupure
            if len(icoupe)==0:#si aucune coupure
                restmp.append(term)
            else:
                tmpterms=[]
                for i in range(len(icoupe)):
                    if(i==0):
                        tmpterms.append(term[:icoupe[i]])
                    else:
                        tmpterms.append(term[icoupe[i-1]:icoupe[i]])
                tmpterms.append(term[icoupe[-1]:])
                restmp+=tmpterms
        res=restmp
        #####################################################
        """
        
    
        stop_words =  utils.stopwordsSet().union({chr(97+l)+"'" for l in range(26)})
        for term in res:
            while(len(term)>0 and (term[0].text in stop_words or term[0].text in string.punctuation+string.whitespace)):
                term.pop(0)
            while(len(term)>0 and (term[-1].text in stop_words or term[-1].text in string.punctuation+string.whitespace)):
                term.pop(-1)
                
        tmpres=[]
        #les poinst dans les mots n'ont pas de sens on retire le terme
        for i,term in enumerate(res):
            t=' '.join([m.text for m in term])
            if('.' not in t):
                tmpres.append(term)
        res=tmpres
        
        return [tuple(retirerParentheses([t.text for t in term])) for term in res \
                if len(term)>=min(1,self.k) and len(term)<=self.n and \
                not (len(term)==1 and ( len(term[0].text) == 1 or term[0].text.isdigit() ) )]
        #s'il n'y a qu'un mot et que ce mot est composé d'une lettre ou d'un nombre on ne garde pas 
        #len(term)>=self.k and len(term)<=self.n and
        
def retirerParentheses(l):
    if('(' in l):
        return l[:l.index('(')]
    return l
    