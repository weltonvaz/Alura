def ordena():
    soma = []

    arquivo = open("produto_vendas_visitas.txt", "r")

    for linha in arquivo:
        valores = linha.split(";")
        soma.append((valores[0], (int(valores[1])*2) + int(valores[2])))

    arquivo.close()

    # Ordenando a lista
    soma.sort(key=lambda x: x[1], reverse=True)

    # Imprimindo a lista
    for s in soma:
        print(s)


if __name__ == '__main__':
    ordena()
