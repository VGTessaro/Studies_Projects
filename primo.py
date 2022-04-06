## PRIMOS numeros somente divisiveis por eles mesmos e 1
num = 1
n_primo = True
while num <= 1:
    y = 2
    cont = 0
    x = int(input("Digite um numero inteiro: "))
    num = x
    while y <= num // 2:
        if num % y == 0:
            cont = cont + 1
            break
        y += 1
    if cont == 0 and num!= 1:
        print("primo")
    else:
        print("não primo")
    num = num + 1



"""
num = 1
while(num <= 30):
    count = 0
    i = 2
    while(i <= num//2):
        if(num % i == 0):
            count = count + 1
            break
        i = i + 1
    if (count == 0 and num!= 1):
        print(" %d" %num, end = '  ')
    num = num + 1
    
    
  #calculo para checar primalidade
    while y < x:
        divis = (x % y)
    if divis == 0:
        n_primo = True
    else:
        n_primo = False## nao sei escrever o calculo para filtrar numeros primos
        if n_primo:
                print("primo")
        else:
                print("nao primo") ## nao esta dando a resposta correta
    
    """