from Stemmer import Stemmer 

class Extractor:
    @staticmethod
    def extract(corpusTraite,strategie,n,resPath,stem):
        """
        param corpus : corpus
        param strategy : la strategy utilisé pour l'extraction de termes
        param n : renvoie les n permiers plus pertinent si -1 renvoie tout

        Renvoie les n premiers candidats-termes du corpus dans l'ordre de
        pertinence calculé par la strategie
        """
        if(stem):
            s=Stemmer()
            memStem,corpus = s.stem(corpusTraite)
        else:
            corpus = corpusTraite
        res = strategie.getScoreTrie(corpus)
        with open(resPath,'w',encoding='utf-8') as f :
            for i,t in enumerate(res[:n]):
                if(stem):
                    term = backtrackStem(memStem,t[0])
                else:
                    term = t[0]
                f.write(str(i+1)+';'+' '.join(list(term))+';'+str(t[1])+'\n')

def backtrackStem(memStem,stem):
    bmax ,freqmax = '',0
    for b,freq in memStem[stem].items():
        if(freq>=freqmax):
            freqmax=freq
            bmax=b
    return bmax
        
        