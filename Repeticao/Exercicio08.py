num1 = int(input("Digite um número: "))
num2 = num1
for i in range(num1, -1, -1):
    print(i)

else:
    print("-")


for i in range(0, num1 + 1):
    print(i)

else:
    print("-")

    
print("\n COM WHILE ")

while num1 >= 0:
    print(num1)
    num1 -= 1

print("----")
num1 = 0
while num1 <= num2:
    print(num1)
    num1 += 1