print("programa para calculo de IMC")
peso = float(input("digite o seu peso(em kg): "))
altura = float(input("digite a sua altura (em metros) "))
imc = peso / (altura**2)

print(f"seu IMC é {imc:.2f}") # .2f é usado
# para mostrar apenas duas casas decimais

if (imc < 18.5):
    print ("abaixo do peso")
elif (18.5 <= imc < 25):
    print("peso normal")
elif (25 <= imc < 35):
    print("sobrepeso.")
else:
    print("obesidade.")