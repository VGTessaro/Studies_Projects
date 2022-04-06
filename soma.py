num = int(input("Digiteo o valor de n: "))
soma = 0
while num < 0:
    div_rest1 = num % 10
    soma = div_rest1 + soma
    num = num // 10
print(soma)