class Extractor:
    @staticmethod
    def extract(corpusTraite,strategie,n,resPath):
        """
        param corpus : corpus
        param strategy : la strategy utilisé pour l'extraction de termes
        param n : renvoie les n permiers plus pertinent si -1 renvoie tout

        Renvoie les n premiers candidats-termes du corpus dans l'ordre de
        pertinence calculé par la strategie
        """
        res = strategie.execute(corpusTraite)
        with open(resPath,'w',encoding='utf-8') as f :
            for i,t in enumerate(res[:n]):
                f.write(str(i+1)+';'+' '.join(list(t[0]))+';'+str(t[1])+'\n')
