alunos = []

while True:

    nome = input("Insira o nome do aluno (ou 'Sair' para finalizar): ").capitalize().strip()
    if nome == "Sair": break
    
    n1 = float(input("Insira a primeira nota: "))
    while (n1 < 0 or n1 >10):
        print("Nota inválida! Insira novamente!")
        n1 = float(input("Insira a primeira nota: "))

    n2 = float(input("Insira a segunda nota: "))
    while (n2 < 0 or n2 >10):
        print("Nota inválida! Insira novamente!")
        n2 = float(input("Insira a segunda nota: "))

    n3 = float(input("Insira a terceira nota: "))
    while (n3 < 0 or n3 >10):
        print("Nota inválida! Insira novamente!")
        n3 = float(input("Insira a terceira nota: "))

    media = (n1+n2+n3) / 3

    if (media >= 7):
        situacao = "Aprovado!"
    elif (media >= 5):
        situacao = "Recuperação!"
    else:
        situacao = "Reprovado!"

    alunos.append({
        "nome": nome,
        "media": media,
        "situacao": situacao
    })

# imprimindo tudo

for aluno in alunos:
    print(f"A média do aluno {aluno['nome']} foi de {aluno['media']:.2f}, colocando-o na situação de: {aluno['situacao']}")