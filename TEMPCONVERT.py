########## Temperature converter #########
import math
x = input("Whats the temperature(C°) now?:  ")
y = input("Whats the temperature(F°) now?:  ")
x1 = float(x)
y1 = float(y)
tempCelsius = (((x1 / 5) * 9) + 32)
tempFahrenheit = (((y1 - 32) * 5) / 9)
print("The Farenheit temperature is ",tempCelsius)
print("The Celsius temperature is ", tempFahrenheit)