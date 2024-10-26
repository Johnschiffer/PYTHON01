Nums = []

for i in range(8):
    Nums.append(int(input("Digite um numero: ")))

Nums.sort()
print(f'O maior é: {Nums[len(Nums)-1]} e o menor é: {Nums[0]}')