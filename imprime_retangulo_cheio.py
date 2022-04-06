x = int(input("digite a largura: \n"))
y = int(input("digite a altura:  \n"))

simbolo = "#"
l = 0 # loop do contador de linhas
while l < y:
    c = 0 # loop do contador de colunas
    while c < x:
        print(simbolo, end="")
        c += 1
    l += 1
    print()

## Simple answer
#num_linha = int(input("digite a altura: \n"))
#num_coluna = int(input("digite a largura:  \n"))
#for l in range(num_linha):
    #for c in range(num_coluna):
        #print('#', end=' ')
    #print()