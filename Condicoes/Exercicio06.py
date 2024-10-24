peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc =   peso / (altura * altura)

if imc > 25:
    print(f"Você está acima do peso com {imc}Kg.")

else:
    print(f"Você está com peso OK com {imc}")