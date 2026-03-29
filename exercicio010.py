import random

num = random.randint(1,10)
guess = 0
tentativas = 0

while (guess != num):
    guess = int(input("Adivinhe o número (de 1 a 10): "))
    tentativas += 1

    if (guess < num):
        print("Muito baixo!")
    elif (guess > num):
        print("Muito alto!")

    if (tentativas >= 5 and guess != num):
        print ("Game Over! O número era {}".format(num))

if (guess == num):
    print ("Parabéns! Você acertou!")
    
    pontos = max(0, 600 - tentativas * 100) #bem interessante, essa funcao pega o maior numero q sai de  dentro da expressao, entao impede numeros negativos (exemplo, se tiver 7 tentativas e eu colocasse só 600, ficaria -100. essa funcao faz ficar 0)
    print (f"Pontuação: {pontos}")


