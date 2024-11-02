lista = []
def Informacoes():
    for i in range(2):
        Nome = input('Digite seu nome: ')
        Idade = int(input('Digite sua idade: '))
        Cidade = input('Digite sua cidade: ')
        lista.append({"Nome":Nome, "Idade":Idade, "Cidade":Cidade})

    return


def Buscar():   
    i = 0
    while (i < len(lista)):
        
        if(lista[i]["Cidade"] == "Campo Grande"):
            print(lista[i])
            
        i += 1
    return


        


Informacoes()
Buscar()
#print(f'{lista[Buscar()]}')