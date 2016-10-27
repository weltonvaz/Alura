def cadastrar(nomes):
	cad = raw_input("Digite um nome ")
	nomes.append(cad)
	return nomes

def remover(nomes):
	print 'Qual nome você gostaria de remover?'
	rmve = raw_input()
	nomes.remove(rmve)
	return nomes	

nomes = []

