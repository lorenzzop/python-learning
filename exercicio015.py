class Aluno:

    def __init__ (self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if len(self.notas) < 3:
            self.notas.append(nota)
        else:
            print("Todas as notas foram inseridas!")

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
            print ("Notas insuficientes")
        return sum(self.notas) / len(self.notas)
    
    def aprovado(self):
        return self.calcular_media() >= 7 #retorna true ou false
    
def main():
    nome = input("Insira o nome do aluno: ")

    a1 = Aluno(nome)

    a1.adicionar_nota(int(input("Adicione a primeira nota: ")))
    a1.adicionar_nota(int(input("Adicione a segunda nota: ")))
    a1.adicionar_nota(int(input("Adicione a terceira nota: ")))
    a1.adicionar_nota(int(input("Adicione a quarta nota: ")))

    media = a1.calcular_media()

    print("Média do aluno: {}".format(media))

    if a1.aprovado():
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")


if __name__ == "__main__":
    main()

    
    

    

        