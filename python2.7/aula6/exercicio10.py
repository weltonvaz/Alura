# -*- coding: UTF-8 -*-
import os
os.system('clear')

def cadastrar(nomes):
    print 'Digite: o nome:'
    nome = raw_input()
    nomes.append(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            alterar(nomes)

        if(escolha == '5'):
            procurar(nomes)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome você gostaria de remover? '
    rmNomes = raw_input()
    nomes.remove(rmNomes)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar? '
    alNomes = raw_input()
    if alNomes in nomes:
        x = nomes.index(alNomes)
        alNomes = raw_input('Digite novo nome: ')
        nomes[x] = alNomes

def procurar(nomes):
    print 'Digite nome a procurar:'
    y = nome_a_procurar = raw_input()
    if y in nomes:
        achei = nomes.index(y)
        print 'Nome achado na posição: ',achei
    else:
        print 'Nome não encontrado'




menu()
