# -*- coding: UTF-8 -*-

def cadastrar(nomes):
    print 'Digite: o nome:'
    nome = raw_input()
    nomes.append(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):    
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 0 para terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)
        
        if(escolha == '3'):
            remover(nomes)
        
        if(escolha == '4'):
            alterar(nomes)  

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    rmMomes = raw_input()
    nomes.remove(rmMomes)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    reMomeia = raw_input()
    posicao = nomes.index(reMomeia)
    print 'Digite no novo nome? '
    nome = raw_input()
    nomes[posicao] == nome
    

menu()