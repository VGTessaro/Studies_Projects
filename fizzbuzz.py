x = float(input("digite um numero: "))

fizz_in = float(x % 3)
buzz_in = float(x % 5)

if fizz_in == 0 and buzz_in == 0:
    print("FizzBuzz")
else:
    print(int(x))