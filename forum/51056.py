class Conta:

    def __init__(self, p_numero, p_titular, p_saldo, p_limite = 1000.0):
        print('Construindo o objeto... {}'.format(self))
        self.numero = p_numero
        self.titular = p_titular
        self.saldo = float(p_saldo)
        self.limite = float(p_limite)

    def depositar(self, p_valor):
        self.__saldo += p_valor

    def sacar(self, p_valor):
        self.__saldo -= p_valor

    def transferir(self, p_valor, p_destino):
        self.sacar(p_valor)
        p_destino.depositar(p_valor)

    def extrato(self):
        print("O Saldo do {} é {}".format(self.titular, self.saldo))

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property.setter
    def limite(self, p_limite):
        self.__limite = p_limite

