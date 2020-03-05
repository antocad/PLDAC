class Strategy:
    """
    Definit une strategie pour extraction de terme
    """
    def execute(self,corpusTraite):
        raise NotImplementError

    def getScoreTrie(self,corpusTraite):
        dictTerme = self.execute(corpusTraite)
        return sorted(dictTerme.items(), key=lambda t: t[1], reverse=True)
