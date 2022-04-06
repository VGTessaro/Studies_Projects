
### REAL STATE BREAKEVEN POINT ######
h_value = int(input("What's the house value? "))  #189,950#
rent_pay = int(input("What's the rent price? "))

bke_point = ((h_value * 0.05) / 12)
print(round(bke_point,2))

if bke_point >= rent_pay:
    print("better off buying this or similar house")
else:
    print("rent this house")
