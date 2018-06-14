#-- coding: UTF-8 --
class Data:
    def __init__(self, p_dia, p_mes, p_ano):
        self.dia = p_dia
        self.mes = p_mes
        self.__ano = p_ano

    def formatada(self):
        print('{}{}{}'.format(self.dia, self.mes, self.__ano))

