def pesquisa(nomes): #pesquisar nome por expressão regular
    print('Digite a expressão regular')
    regex = raw_input()
    concatena = ' '.join(nomes) 
    resultado = re.findall(regex, concatena)
    print (resultado)

A = ['Pedro', 'Arthur', 'Tarcisio']
print(pesquisa(A))