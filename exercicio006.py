n1 = float(input ("Digite a nota 1: "))
n2 = float(input ("Digite a nota 2: "))
n3 = float(input ("Digite a nota 3: "))

if ((n1 > 10) or (n2 >10) or (n2 > 10)):
    print("\nNota inválida! Insira a nota novamente.")
else:
    media = (n1 + n2 + n3) / 3
    print("\nA média das notas foi {:.2f}!".format(media))

if (media >= 7):
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")