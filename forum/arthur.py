class Data:

    def __init__(self, dia, mes, ano):

        print("Recebendo data... ")

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime_data(self):

        print("A data atual é {}/{}/{}".format(self.dia, self.mes, self.ano))
