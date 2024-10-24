# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

Nome = ''
Idade = 0
Salario = 0
Sexo = ''
Estado_Civil = ''


nome = str(input("Digite um nome maior que 3 letras:"))
while len(nome) <= 3:
      nome = str(input("Você não digitou um nome maior que 3 letras:"))
      

      
Idade = int(input("Digie sua idade (0 ~ 120): "))
while Idade < 0 or  Idade > 120:
       Idade = int(input("Você não digtou uma idade valida(0 ~ 120): "))


Salario = int(input("Digite seu salario: "))
while Salario <= 0:
      Salario = int(input("Seu salario tem que ser maior que R$0: "))

else:
     print('Cadastrado')

