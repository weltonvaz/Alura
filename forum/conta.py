class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero 
        self.__titular = titulae
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} de titular{}".format.saldo, self._titular)

    def deposita(self):
        print("Saldo de {} do titular {}".format(self._saldo, self._titular))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self._saldo

    def get_titular(self):
        return self._limite  

    def get_limite(self):
        return self._limite

    def set_limite(self, limite):
        self._limite = limite