## inoirt from json files
# work with deeper nested data

### NESTED LISTS ###

'''Outter List'''

lis = [["a","b","c"],["d","e"],["F"]]

y = lis[0].append("y")
print(lis)
'''python interpreter can identify when to create a new list or look into the indexes nested inside
and look into the correct position inside the nested lists, as below'''
print(lis[0][2])

##HOW DO WE LOOK INTO A 3rd LEVEL NESTED LIST??##
lis[2].append([0,1,"car",3])
''' a good approach is to extract values incrementally using variables, as below'''

extr = lis[2][1][2]
print(extr)

### NESTED DICTIONARIES ###

'''the complex objects inside a list don't need to be lists 
they can be tuples or dictionaries'''

'''to assign or pick from nested dictionaries you have
to use the 'key' related to the value you wish to return, as below'''


info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }

color = info["personal_data"]["physical_features"]["color"]
print(color)
print("\n")

info = [["Tina","Turner", 1939],["Matt","Dameon",1975],["Luke","Cage",1983]]

lastnames = []
'''
for ppl in info:
    lastnames.append(ppl[1])
    print(lastnames)
'''
'''
for ppl in info:
    for val in ppl:
        print(val)
'''
'''
for val in info[1]:
    print(val)
'''
'''
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings = []

for lis in L:
    for fruit in lis:
        if "b" in fruit:
            b_strings.append(fruit)

print(b_strings)
'''

'''
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]
last_names = []
for person in info:
    last_names.append(person[1])
print(last_names)
'''

'''If you have different types of data inside a list you can add some
if-then logical statements to check what is the tye of data and act accordingly'''
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)

## SHALLOW COPIES are copies of lists that can be mutated with the original list if the later is mutated


## DEEP COPIES a deep copy of a list not only makes a copy of the outer list, but also makes copies of all the inner lists. And their inner list all the way down. A deep copy is completely decoupled from the original. You can make a deep copy with your own code if the structure is simple enough, or use the built in deep copy function in the copy module.

'''
import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)

'''

big_list = [[['one'],['two','one'],['Three','two'],['four','one','two'],['five'],['six','three']]]

word_counts = {}
for il1 in big_list:
    for il2 in il1:
        for word in il2:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
print("\n", word_counts,"\n")


lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = ""
for lista in lst:
    for word in lista:
        if word != 'yellow':
            continue
        else:
            yellow += word
print(yellow)


nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = False
print(nested.keys())
for itm in nested:
    print(itm)
    if itm == "data":
        data = True
print(itm)
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
print("\n== twenty 4 ==")
twentyfour = False
if 24 in nested['data']:
    twentyfour = True
    print(twentyfour)
else:
    twentyfour = False
    print(twentyfour)