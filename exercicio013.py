class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Valor depositado em conta: {}".format(valor))
    
    def sacar(self, valor):
        if ((self.saldo - valor) >= 0):
            self.saldo -= valor
            print("Valor sacado: {}".format(valor))
        else:
            print("Saldo insuficiente")
    
    def mostrar_saldo(self):
        print(f"Saldo da conta: {self.saldo}")

def main():
    titular = input("Insira o nome do titular: ")
    saldo = float(input("Insira o saldo: "))

    c1 = ContaBancaria(titular, saldo)

    c1.mostrar_saldo()

    c1.depositar(1500)
    c1.sacar(2000)

    c1.mostrar_saldo()

if __name__ == "__main__":
    main()