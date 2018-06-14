# -*- coding: utf-8 -*-
class A:
    def __init__(self, nome):
        self.nome = nome

class B(A):
    def metodo_de_b():
        super().__init__()
        return "não faço nada"
