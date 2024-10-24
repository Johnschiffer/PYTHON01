num1 = int (input("Digite o primeiro numero: "))
num2 = int (input("Digite o segundo numero: "))
num3 = int (input("Digite o terceiro numero: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} é maior!")

    else:
        print(f"{num3} é o maior!")

elif num2 > num3:
        print(f"{num2} é maior!")

else:
    if  num1 == num2 == num3:
        print(f"Eles são iguais!")
    else:
         print(f"{num3} É o maior")
