
primo = []
k = 0
def  éPrimo(k):
    for n in range(1, k+1):
        for i in range(2, n):
            if n % i == 0:
                break
            else:
                primo.append(n)
                break
def maior_primo(k):
    éPrimo(k)
    if primo[-1] == k:
        return primo[-1]
    else:
        return primo[-2]

