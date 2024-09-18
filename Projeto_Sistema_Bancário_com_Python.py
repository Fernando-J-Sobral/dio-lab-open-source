class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if valor > 0:
            if valor > 500:
                print("O valor máximo para saque é R$ 500.00!")
            elif valor > self.saldo:
                print("Saldo insuficiente para realizar o saque!")
            elif self.saques_diarios >= 3:
                print("Limite diário de saques atingido!")
            else:
                self.saldo -= valor
                self.extrato.append(f"Saque: R$ {valor:.2f}")
                self.saques_diarios += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido!")

    def visualizar_extrato(self):
        print("\nExtrato:")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

# Exemplo de uso do sistema bancário
conta = ContaBancaria()

while True:
    print("1. Depositar")
    print("2. Sacar")
    print("3. Visualizar Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: "))
        conta.depositar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para saque: "))
        conta.sacar(valor)
    elif opcao == "3":
        conta.visualizar_extrato()
    elif opcao == "4":
        print("Obrigado por usar o sistema bancário!")
        break
    else:
        print("Opção inválida! Tente novamente.")
