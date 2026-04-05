class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Oi, eu sou o {self.nome} e tenho {self.idade} anos")

    def fazer_aniversario(self):
        self.idade += 1


def main():
    nome = input("Insira o nome: ")
    idade = int(input("Insira a idade: "))
    p1 = Pessoa(nome, idade)
    p1.apresentar()

    p1.fazer_aniversario()

    p1.apresentar()


if __name__ == "__main__":
    main()
