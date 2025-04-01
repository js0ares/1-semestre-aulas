def aumento_salarial(cargo, salario_atual):
    if cargo == "junior":
        return salario_atual * 1.10
    elif cargo == "pleno":
        return salario_atual * 1.15
    elif cargo == "senior":
        return salario_atual * 1.20

x = aumento_salarial("pleno", 4000)
y = aumento_salarial("senior", 4000)
print(x, y)