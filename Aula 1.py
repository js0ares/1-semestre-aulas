
import math

x = float(input("insira o valor do salario: "))
z = float(input("insira a porcentagem: "))

final = (x * z / 100) + x 
novo_salario = x or z*(1 + porcentagem/100)

print(f"o seu novo salario é: {novo_salario: .2f}")