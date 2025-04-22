""" faça um algoritmo que leia o salario minimo e calcule quantos salarios são
e continue repetindo ate digitar 0, porem o salario minimo nao deve repetir"""
SalarioMinimo = float(input("Digite seu salario minimo: "))
while True:
    Salario = float(input("Digite seu salario e se for 0 o programa encerra : "))
    if Salario ==0:
        print("programa finalizado")
        break
    div= Salario/SalarioMinimo
    print(f" voce recebe {div} salarios minimos")

