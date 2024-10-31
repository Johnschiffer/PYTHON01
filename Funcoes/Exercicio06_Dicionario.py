Pessoa = []

for i in range(5):
    Nome = input('Digite seu nome: ')
    Idade = int(input('Digite sua idade: '))
    Pessoa.append({"Nome":Nome, "Idade":Idade})

def Buscar():   
    i = 0
    Menor = 0
    while (i < 4):
        
        if(Pessoa[i]["Idade"] < Pessoa[Menor]["Idade"]):
            Menor = i

        else:
            Menor = Menor
            
    return Menor

print(f'{Pessoa[Buscar()]}')
    