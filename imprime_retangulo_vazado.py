x = int(input("digite a largura: \n"))
y = int(input("digite a altura:  \n"))

simbolo = "#"
c = 0 # loop do contador de colunas
while c < y:
    l = 0 # loop do contador de linhas
    while l < x:
        if(l == 0 or l == x - 1 or c == 0 or c == y - 1):
            print(simbolo, end='')

        else:
            print(' ', end='')
        l += 1
    c += 1

    print()