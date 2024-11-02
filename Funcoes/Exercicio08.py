lista = []

def Pessoas():
    for i in range(2):
        Nome = input('Digite seu nome: ')
        Cidade = input('Digite sua cidade: ')
        lista.append({"Nome":Nome, "Cidade":Cidade})
        
    listaTemp = sorted(lista, key=lambda d : d ["Nome"])
    print(listaTemp)


Pessoas()