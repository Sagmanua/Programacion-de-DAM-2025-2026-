limitadifreneciasaldo = 10000

class CuntaBancaria():
    def __init__(self):
        self.__saldo = 0
        self.__clinte = None

#Defino settees y gettre para el saldo
    def setSaldo(self,nuevosaldo):
        # Establesco una condichi de que valida se el  saldo es mayor de 1000 euros
        if nuevosaldo >self.__saldo + limitadifreneciasaldo:
            #Si salta la alarmi avisa y no cambia
            print("Voy a avisar a la entidad de un ingreso muy grande")
        else:
            #Si pasa el filtri solo entroces se cambia
            self.__saldo = nuevosaldo


    def getSaldo(self):
        return self.__saldo

cuentecliente = CuntaBancaria()
cuentecliente.setSaldo(10000000000)
print(cuentecliente.getSaldo())

