#!/usr/bin/python
# -*- coding: utf-8 -*-
# Função para remover parametros de uma lista
# dentro da função a lista chama: inf
# e o elemento dentro da função: id_remove
def remover(inf, id_remove):
    inf.remove(id_remove)
    return inf

# Lista com elementos
lista = ['red', 'yellow', 'green', 'black']

''' Como vc esta passando parametros para a função
    raw_input tem que ficar fora, e ele pega o que
    foi digitado como string'''

remove = raw_input('Digite um elemento a ser removido: ')

# Se for numero vc tem que converter par int
# quando vc chamar a função pode usar nomes diferentes
print(remover(lista, remove))