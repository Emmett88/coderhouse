def calcular_imc():
    # se
    peso = float(input("Tá preocupado com o peso? Manda aqui pra eu calcular um lance...: "))
    altura = float(input("Qual tua altura, mano? "))

    
    imc = peso / (altura ** 2)

  
    print(f"Seu IMC é: {imc:.2f}")
    print("Vai precisar treinar?")


calcular_imc()
