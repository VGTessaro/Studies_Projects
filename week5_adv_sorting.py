print("Sorting a Dictionary's Keys\n")
'''Iterate through the dictionarie and sort it'''

print("\n2. Sort the following dictionary based on the keys so that they are sorted a to z.\nAssign the resulting value to the variable sorted_keys.\n")
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_keys = sorted(dictionary.keys())

print(sorted_keys)

print("\n3. Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to buy at the store.\nSort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.\n")

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3,
             'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}

grocery_keys_sorted = sorted(groceries.keys())

print(grocery_keys_sorted)

print("\n4. Sort the following dictionary’s keys based on the value from highest to lowest.\nAssign the resulting value to the variable sorted_values.\n")

dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}

sorted_values = sorted(dictionary,reverse = True , key = lambda v: dictionary[v])
print(sorted_values)



print("\n\nWEEK 5 ASSESSMENT\n")

print("__We have provided the dictionary groceries.\nYou should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as 'most_needed'.")

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries, key = lambda i: groceries[i], reverse = True)
print("\nAnswer: ",most_needed,"\n")

print("__Create a function called 'last_four' that takes in a single ID number and returns the last four digits.\nFor example, the number 17573005 should return 3005. Then, use the resulting function to sort the list of ids stored in the variable, ids, from lowest to highest.\nSave this sorted list in the variable, 'sorted_ids'. Hint: Remember that only strings can be indexed, so conversions may be needed.")

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
'''
def last_four(lis):
    num_list = []
    for n in lis:
        num = str(n)
        num_list.append(num[-4:])
    return num_list
'''
def last_four(x):
    num = str(x)
    return num[-4:]

sorted_ids = sorted(ids, key = last_four)

print("\nAnswer: ",sorted_ids)

