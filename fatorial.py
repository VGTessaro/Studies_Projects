## Solucao factorial

num = int(input("Digiteo o valor de n: "))
mult = 1
while num > 0:
    num_a = num
    mult = num_a * mult
    num = num - 1
print(mult)

## EASY MODE FACTORIAL
"""import math

n = int(input("Digite o valor de n: "))
n_fat = math.factorial(n)

print(n_fat)"""

