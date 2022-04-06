import math
primes = []
def findprimes(given_number):
    # Initialize a list
    for poss_prime in range (2, given_number + 1):
        if given_number <= 1:
            is_prime = False
        else:
            is_prime = True
            for num in range(2, int(math.sqrt(poss_prime)) + 1):
                if poss_prime % num == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(poss_prime)

    return (primes)
x = int(input("Search Primes up to: "))
findprimes(x)
print(primes)


#n=int(input())
#flag=0
#for i in range(2,int(n**0.5)+1):
    #if(n%i==0):
        #flag=1
        #break
#if flag==0 and n>1:
    #print("Prime")
#else:
    #print("Not Prime")


## USING SQUARE ROOT

#import math
#
#primes = []
#
#
#def is_prime(number):
    #if number <= 1:
        #return False
    #for i in range(2, int(math.sqrt(number)) + 1):
        #if number % i == 0:
            #return False
    #return True
#
#for i in range(1, 999):
    #if is_prime(i):
        #primes.append(i)
#
#print(primes)

