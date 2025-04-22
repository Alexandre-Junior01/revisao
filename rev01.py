""" receber 3 numeros A,B e C, e dizer  se a soma entre A+B e menor ou maior que C"""
a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))
d = a + b
print(d)
if d < c:
    print(f"C é {c}, é maior que a soma entre A e B")

