# Mostre 5 numeros que o usuario digitar em ordem crescente


Nums = []
for i in range(7):
    Nums.append(int(input("Digite um numero: ")))

    Nums.sort()

print(Nums)