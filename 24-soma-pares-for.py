#João Pinto, Diego Nonato, Luiz Neto

# Algoritmo para calcular a soma dos números pares entre 1 e 50
soma = 0  # Inicializa a variável soma com 0
for i in range(2, 51, 2):  # O laço inicia em 2, vai até 50, pulando de 2 em 2 (só números pares)
    soma += i  # Adiciona o número atual (i) à soma
# Imprime o resultado da soma dos números pares
print("A soma dos números pares entre 1 e 50 é:", soma)