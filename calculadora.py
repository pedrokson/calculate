# Função para somar dois números
def add(x, y):
    return x + y

# Função para subtrair dois números
def subtract(x, y):
    return x - y

# Função para multiplicar dois números
def multiply(x, y):
    return x * y

# Função para dividir dois números
def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    # Recebe a escolha do usuário
    choice = input("Digite sua escolha (1/2/3/4): ")

    # Verifica se a escolha é uma das quatro opções
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        # Verifica se o usuário deseja realizar outra operação
        next_calculation = input("Deseja realizar outra operação? (sim/não): ")
        if next_calculation.lower() != 'sim':
            break

    else:
        print("Opção inválida. Tente novamente.")
