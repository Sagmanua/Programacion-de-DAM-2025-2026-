class CuntaBancaria():
    def __init__(self):
        self.__saldo = None
        self.__clinte = None

#Defino settees y gettre para el saldo
    def setSaldo(self,nuevosaldo):
        self.__saldo = nuevosaldo
    def getSaldo(self):
        return self.__saldo

cuentecliente = CuntaBancaria()
cuentecliente.setSaldo(1000000000)
print(cuentecliente.getSaldo())

