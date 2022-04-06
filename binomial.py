
def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n,k):
    if n < k:
        print("Primeiro valor deve ser maior que o segundo, tente novamente")
    else:
        return fatorial(n) // (fatorial(k) * fatorial(n - k))



def testa_fatorial():
    if fatorial(1) == 1:
        print("Func para 1")
    else:
        print("N func para 2")
    if fatorial(2) == 2:
        print("Fun para 2")
    else:
        print("N F para 2")
    if fatorial(0) == 1:
        print("Funciona para 0")
    if fatorial(5) == 120:
        print("F PARA 5")
    else:
        print("N F PARA 5")