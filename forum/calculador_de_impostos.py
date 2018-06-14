# -*- coding: UTF-8 -*-
# calculador_de_impostos.py

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, calcula_imposto):
        valor = calcula_imposto(orcamento)
        print(valor)

if (__name__ == '__main__'):
    from orcamento import Orcamento
    from impostos import ISS, ICMS

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, ICMS().calcula_ICMS) # imprime 50.0
    calculador_de_impostos.realiza_calculo(orcamento, ISS().calcula_ISS)  # imprime 30.0
