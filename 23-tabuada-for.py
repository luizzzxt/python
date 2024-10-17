
# Algoritmo para exibir a tabuada de um número fornecido pelo usuário
numero = int(input("Digite um número para ver sua tabuada: "))  # Solicita ao usuário um número e converte para inteiro
for i in range(1, 11):  # O laço vai de 1 até 10
    # Imprime a multiplicação do número pelo valor atual do laço (i)
    print(numero, "x", i, "=", numero * i)