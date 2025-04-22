""" IMC, peso e altura"""
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura**2
if imc < 18.6:
    print("Abaixo do Peso")
elif 18.6 < imc < 24.9:
    print("Peso Ideal")
elif 25.0 < imc < 29.9:
    print("Levemente Acima do Peso")
elif 30.0 < imc < 34.9:
    print("Obesidade Grau 1 ")
elif 35.0 < imc < 39.9:
    print("Obesidade Grau 2 (Severa)")
else:
    print("Obesidade Grau 3 (Mórbida)")

