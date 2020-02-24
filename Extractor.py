class Extractor:
    @staticmethod
    def extract(corpus,Strategy,n):
        """
        param corpus : corpus
        param strategy : la strategy utilisé pour l'extraction de termes
        param n : renvoie les n permiers plus pertinent

        Renvoie les n premiers candidats-termes du corpus dans l'ordre de
        pertinence calculé par la strategie
        """

        
