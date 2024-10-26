def fibonacci(num):
    a, b = 0, 1

    if num == 0 or num == 1:
        return f"{num} pertence à sequencia "

    while b < num:
        a, b = b, a + b

    if b == num:
        return f"O número {num} pertence à sequencia de Fibonacci"
    else:
        return f"O número {num} não pertence à sequencia de Fibonacci"

def main():
    while True:
        print("Menu")
        print("1. Verificar se um número pertence à sequencia de Fibonacci")
        print("0. Sair")
        opcao = int (input("Escolha uma opção: "))

        if opcao == 1:
            num = int(input("Insira um número: "))
            resultado = fibonacci(num)
            print(resultado)
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
    