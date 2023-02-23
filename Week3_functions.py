# Functions and abstracions
''' Abstraction is the idea of creating functions to save time and avoid redundances and
erros, keeeping a standard within the program'''

'''def hello():
    name = input("What is your name?\n")
    print("Hello,",name)

    print("Glad to meet you")

hello()'''

#Positional Paramaters
'''functional parameter is where the input of arguments for the function
to return a value using those arguments'''

def funcao(a,b):
    resultado = a + b
    return resultado

print(funcao(3,6))


def longer_than_five(list_of_names):
    for name in list_of_names: # iterate over the list to look at each name
        if len(name) > 5: # as soon as you see a name longer than 5 letters,
            return True # then return True!
            # If Python executes that return statement, the function is over and the rest of the code will not run -- you already have your answer!
    return False # You will only get to this line if you
    # iterated over the whole list and did not get a name where
    # the if expression evaluated to True, so at this point, it's correct to return False!

# Here are a couple sample calls to the function with different lists of names. Try running this code in Codelens a few times and make sure you understand exactly what is happening.

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1))
print(longer_than_five(list2))


## LOCAL and GLOBAL variables
'''VARIABLE SCOPE'''
'''each invocation of a function creates a new NAMESPACE'''

'''local and global stack-frames'''

'''using a variable name inside a function register that name as a local
variable'''

'''if a variable is not defined inside a function python will look for
in the global-stack-frame for that variable'''

'''DON'T declare 'global' variables inside a function'''

# Function composition is calling a function inside another function to reduce the size of the program
# and compartmentalize the solutions for a problem

# TUPLES packing
'''tuples are information divided by commas ','. it can be done
like a list or without the parenthesis '''
print("\n\nEXERCICIO TUPLES\n")
print("GET EVERY 3rd item from the list of tuples")
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'),
            ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'),
            ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'),
            ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

t_check = []

for lis in lst_tups:
    t_check.append(lis[2])

print(t_check)

print("|\n\n|")
print("GET EVERY 3rd item from the list of tuples")
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2),
        ('squirrel', 'chipmunk')]

seconds = []

for i in tups:
    seconds.append(i[1])

print(seconds)



print("\n__The Pythonic Way to Enumerate Items in a Sequence__\n")
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']
for n in range(len(fruits)):
    print(n, fruits[n])

print("\n___ASSING MULTIPLE VARIABLES IN ONE LINE___\n")
(water,fire,electric,grass) = ("Squirtle","Charmander","Pikachu","Bulbasaur")
print(water,fire,electric,water)

v1,v2,v3,v4 = (1,2,3,4)

print("\n___USING .item() to create a tuple from a DIC")
print("and appending in different lists___\n")
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []

poketuple = pokemon.items()

for p in poketuple:
    p_names.append(p[0])
    p_number.append(p[1])

print(p_names, p_number)
print("\n")
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3,
                      'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0,
                      '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

track_events = []

tef = track_medal_counts.items()

for t in tef:
    track_events.append(t[0])

print(track_events)

print("\n___UNPACKING TUPLES___")
'''to unpack tuples you can use * notation before a variable that 
contains a tuple to tell Python to pass all parameters in a tuple'''

def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # this line will cause the values in z to be unpacked

print("\nASSESSMENT\n")
print("\nEXE 5")
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
medals = gold.items()
num_medals = []

for medal in medals:
    num_medals.append(medal[1])
print(num_medals)

print("\nEXE 4")
def info(name, gender, age, bday_month, hometown):
    return (name, gender, age, bday_month, hometown)

print("\nEXE 3")
olymp = ('Rio', 'Brazil', 2016)
city,country,year = olymp

print("\nEXE 2")

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []
for i in tuples_lst:
    country.append(i[1])

print("\nEXE 1")
olympics = "Beijing","London","Rio","Tokyo"

