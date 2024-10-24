salario = int(input("Digite seu salário: "))

desc_trans = salario * 0.06
desc_saude = salario * 0.03

print(f"Será descontado referente ao vale-transporte: R${desc_trans}\n"
      f"Será descontado referente ao vale-saude200: R${desc_saude}\n"
      f"Seu novo salário será: R${ salario - (desc_trans + desc_saude)}")