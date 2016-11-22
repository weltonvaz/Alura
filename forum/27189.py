# -*- coding: UTF-8 -*-
def cadastrar(nomes):
    print 'digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def procurar(nome_procurado,nomes):
    if(nome_procurado in nomes):
        print '%s está na lista.'% nome_procurado
    else:
        print'%s não está na lista' % nome_procurado

def listar(nomes):
    for nome in nomes:
        print nome


def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite 1 para cadastrar, 2 para listar nomes, 3 para remover da lista, 4 para alterar um nome, 5 para procurar um nome, 0 para encerrar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            print 'Digite o nome para retira-lo'
            nome = raw_input()
            nomes.remove(nome)

        if(escolha == '4'):
            print 'Qual nome você quer alterar?'
            nome = raw_input()
            print'Coloque o nome novo:'
            nome_novo = raw_input()
            pos = nome.index(nome)
            nomes[pos] = nome_novo

        if(escolha == '5'):
            print 'Qual nome você procura?'
            nome_procurado = raw_input()
            procurar(nome_procurado, nomes)




menu()
