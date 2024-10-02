def exibirMensagem(nome):
    print(f"olá, {nome} com {idade} anos!")
    
def soma(a,b):
    return a + b
    
    
  nome = input("Digite o seu nome: ")
  idade = input("Digite a sua idade: ")
  exibirMensagem(nome, idade)
  
  valorA = int(input("Digite o primeiro número"))
  valorB = int(input("Digite o segundo número "))
  resultado = somar(valorA,valorB)
  print(f"o resultado da soma = {resultado}")