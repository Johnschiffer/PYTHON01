num1 = int (input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero: "))
num3 = int (input("Digite o terceiro numero: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} é maior!")

    else:
        print(f"{num3} é maior!")

else:
    if num2 > num3:
        print(f"{num2} é o maior!")
    
    else:
        print(f"{num3} é o maior!")

