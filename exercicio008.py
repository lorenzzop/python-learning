nome = None
soma = 0

nomes = []
idades= []

while True:

    nome = input("Insira o nome (ou 'Sair' para finalizar): ").strip().capitalize()
    if nome == "Sair": break

    idade = int(input("Insira a idade: "))

    nomes.append(nome)
    idades.append(idade)

#for idade in idades:
#    soma = soma + idade

#media = soma / len(idades)

media = sum(idades) / len(idades)

for nome in nomes:
    print(f"{nome}")

print ("A média das idades é {:.2f}".format(media))