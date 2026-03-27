nome = None

lista_nomes = []

while (nome != "Sair"):
    nome = input("Insira seu nome (ou 'Sair' para finalizar): ")
    lista_nomes.append(nome)
 
for i in range(len(lista_nomes)-1): #coloquei o -1 para o "Sair" não ser impresso junto com os outros nomes
    print(lista_nomes[i])