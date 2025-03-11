while True:
    numero = int(input("Digite um número para ver sua tabuada: "))
    i = 1

    print(f"Tabuada do {numero}:")
    while i <= 10: 
        print(f"{numero} x {i} = {numero * i}")
        i += 1   
    
    sair = input("Você deseja sair do programa? (sim/não) ")
    if sair.lower() == "sim":  # Corrigido para verificar a variável 'sair'
        break