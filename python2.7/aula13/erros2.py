# -*- coding: UTF-8 -*-

#erros.py
from models import *
arquivo = None
try:
        arquivo = open('perfis.csv','r')
        valores = arquivo.readline().split(',')
        Perfil(*valores)
finally:
        if(arquivo is not None):
                print('fechando arquivo')
                arquivo.close()
