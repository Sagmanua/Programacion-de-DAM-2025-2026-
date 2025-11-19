class Cliente():
    def __init__(self):
        self.nonmbreCompleto = None
        self.email = None
    def setNomreCompleto(self,nuvonombre):
        self.nonmbreCompleto = nuvonombre
    def setEmail(self,nueboemail):
        self.email = nueboemail
    def getNOmbreCopmlrto(self):
        return self.nonmbreCompleto
    def getEmail(self):
        return self.email