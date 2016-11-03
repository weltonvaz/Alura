# -*- coding: UTF-8 -*-
class Perfil():
   'Classe padrão para perfis de usuários'
   def __init__(self, nome, telefone, empresa):
      self.nome = nome
      self.telefone = telefone
      self.empresa = empresa

   def imprimir(self):
      print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome, self.telefone, self.empresa)

class Data():
   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   def imprime(self):
      return '%s/%s/%s' %(self.dia,self.mes,self.ano)

class Pessoa():
   def __init__(self, nome, peso, altura):
      self.nome = nome
      self.peso = float(peso)
      self.altura = float(altura)

   def imprime_imc(self):
      imc = self.peso / (self.altura**2)
      return 'Imc de %s: %s' %(self.nome,imc)
