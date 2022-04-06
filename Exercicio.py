# checar se numeros sao primo
def lista_primos(x):
    y = 2
    cont = 0
    primo = True
    while seq_num[0] <= 1:

        while y <= seq_num[0] // 2:
            if seq_num[0] % y == 0:
                cont = cont + 1
                break
            y += 1
    seq_num.index[]

# salvar numeros em uma lista
seq_num = []
stop = False
while stop == False:
    entra = int(input("Enter the set of numbers for analysis, enter ""0"" to stop: "))
    seq_num.append(entra)
    if entra == 0:
        stop = True
        print(seq_num[:-1])
        # chamar funcao de calcular primos na lista
        lista_primos(seq_num)


# imprimir quais numeros da lista sao primos

# imprimir quais nao sao primos