"""Imprimir na tela se o numero é par ou impa, positivo ou negativo """
nub = int(input("Digite um numero: "))
if nub % 2 == 0 and nub > 0:
    print('numero par e é positivo')
elif nub % 2 == 0 and nub < 0:
    print('numero par e é negativo')
elif nub % 2 != 0 and nub >0:
    print("numero é impar e positivo")
else:
    print("numero é impar e negativo")
