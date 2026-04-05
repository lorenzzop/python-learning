class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual/100)
        print(f"Valor com desconto: {self.preco}")

def main():

    nome = input("Insira o nome do produto: ")
    preco = float(input("insira o preço do produto: "))
    quantidade = int(input("Insira a quantidade do produto: "))

    p1 = Produto(nome, preco, quantidade)

    total = p1.calcular_total()
    print("Valor total: {}".format(total))

    p1.aplicar_desconto(20)

if __name__ == "__main__":
    main()
    

    