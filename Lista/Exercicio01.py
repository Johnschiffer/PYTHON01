# Costrua um programa onde o usuario digitara seis numeros em um vetor e,
# depois, esses numeros devem er exibidos na tela na ordem digitada.

Nums = []

for i in range(6):
    Nums.append(int(input("Digite um numero: ")))
    #Nums += Nums
    
print(Nums)
