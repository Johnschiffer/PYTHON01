
#COM FOR

num = int(input("Digite um número: "))

for i in range(num, 101):
    if i %2 == 0:
        print(i)

else:
    print("Fim do for! \n")


# COM WHILE
    
num2 = int(input("Digite um número: "))
while num2 <= 100:
    if num2 %2 == 0:
        print(num2)
        
    num2 += 1

else:
    print("Fim do while!")