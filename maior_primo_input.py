n=int(input("Enter the number till you want to check: "))
primes = []
for k in range (2, n+1):
    for j in range(2, k):
        if k%j == 0:
            break
    else:
        primes.append(k)
maior_primo = primes[-1]
print(f"maior primo: {maior_primo}")






