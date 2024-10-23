import math

def is_prime(n):
    if n < 2:
        return False 
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:  
            return False  
    return True  

# Solicitar entrada do usuário
numero = int(input("Digite um número inteiro: "))
if is_prime(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")