class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
       
    def formatada(self):
        print("%s/%s/%s" %(self.dia, self.mes, self.ano))
        
from datas import Data

d = Data(21,11,2007)

d.formatada()