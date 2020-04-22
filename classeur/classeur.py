# -*- coding: utf-8 -*-
from statistics import mean
from config.config import FORMULES_AGREGATION

FONCTION_AGREGATION = {FORMULES_AGREGATION.MAX : lambda iter : max(iter), \
                       FORMULES_AGREGATION.SUM : lambda iter : sum(iter), \
                       FORMULES_AGREGATION.MEAN : lambda iter : mean(iter)}

class Classeur:
    """Cette classe permet d'attribuer un score aux les termes d'un corpus"""
    def __init__(self,config):
        """Constructeur de la classe Classeur
        
        Parameters
        ----------
        config : Config
            objet de configuration pour permettre de classer les termes en fonction
            da le configuration        
        """
        self.config=config
        self.formuleAgregation = FONCTION_AGREGATION[config.getFormuleAgregation()]
    
    def noter(self,indexCorpus):
        """Méthode qui attribut un score à chacun des termes du corpus
        
        Parameters
        ----------
        indexCorpus : Indexation
            L'index du corpus
            
        Returns
        -------
        dict[tuple[str*],float]
            Dictionnaire de terme en clé et score en valeur
            
        Raises
        ------
        NotImplementedError
            Lève toujours cette erreur car cette classe est abstraite
        """
        raise NotImplementedError

    def classer(self,indexCorpus):
        """Attribut un score aux termes du corpus puis les tri en fonction du
        score, puis par ordre alphabétique si égalité sur le score
        
        Parameters
        ----------
        indexCorpus : Indexation
            L'index du corpus
            
        Returns
        -------
        List[tuple[tuple[str*],float]]
            Liste trié par ordre décroissant des scores des termes 
        """
        #on récupére le dictionnaire terme/score
        dictTerme = self.noter(indexCorpus)
        #D'abord le tri par ordre alphabétique
        tmp = sorted(dictTerme.items(), key=lambda t: ' '.join(t[0]))
        #Puis tri par score
        return sorted(tmp, key=lambda t: t[1], reverse=True)
    
    def normaliserScoreClassement(self,dictTermesScores):
        """Normalise en place le score des termes du dictionnaire passé en paramètre.
        
        Recentre entre 0 et 1 le score des termes.
        
        Parameters
        ----------
        dictTermesScores : dict[tuples[str*],float]
            Dictionnaire du score pour un terme
        """
        scoremax = max(dictTermesScores.values())
        scoremin = min(dictTermesScores.values())
        for terme in dictTermesScores.keys():
            dictTermesScores[terme] = (dictTermesScores[terme]-scoremin) / (scoremax-scoremin)
        