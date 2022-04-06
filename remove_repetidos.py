#funcao recebe lista de numeros inteiros
lista = [1,2,3,4,5,6,7,7,8,8,9,9,0,20]
def remove_repetidos(lista):
    copia_lista = []
    for num in lista:       ## confere se ha elementos repetidos
        if num not in copia_lista:      ###  remove elementos repetidos
            copia_lista.append(num)
            copia_lista.sort()      #### return lista correspondente a primeira sem elemento repetidos e ORDENADA
    return copia_lista

# dica de usar lista.sort() ou sorted(lista)




