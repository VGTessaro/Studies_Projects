count = int(input("Digiteo o valor de n: "))
num = 0
imp_c = 0
while imp_c < count:      ##contador de impares
    num += 1
    if (num % 2 != 0):
        print(num)
        imp_c += 1