## DICTIONARIES ACCUMULATION

'''using a FOR loop to iterate through a text and
adding a new key in the dictionaire and count the values af that
key in there'''

text = "Any text that you want: using a FOR loop to iterate through a text and adding a new key in the dictionaire and count the values af that key in there"
words = text.split()
empty_dic = {}

for i in words:
    if i not in empty_dic:
        empty_dic[i] = 0
    empty_dic[i] = empty_dic[i] + 1

print(empty_dic)

'''accumulation patter can be done by creatin a var that
is going to receive the sum of each value from a key in the dictionarie'''
word_total = 0
for word in empty_dic:
    word_total = word_total + empty_dic[word]
print(word_total)

'''
Finding a MAX or MIN value in a dictionarie using
accumulation pattern

'''
print("\n BEST KEY in DICTIONARIE\n")


d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
# initialize variable best_key_so_far to be the first key in d
best_key_so_far = list(ks)[0]
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))

print("\n\n FINDING MIN VALUE KEY IN A DICTIONARIE \n")

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = {}                      # inicializa o dicionario
chars = list(placement)     # separa caracteres em uma list

for ch in chars:            # faz a primeira iteracao para criar o dicionario com valores de cada chave
    if ch not in d:
        d[ch] = 0
    d[ch] += 1

keys = d.keys()             # cria a lista somente com chaves
min_value = list(keys)[0]   # inicializa valor na variavel
for key in keys:            # faz a segunda iteracao onde [compara o valor de cada chave do dicionario com o valor na variavel]
    if d[key] < d[min_value]:
        min_value = key
print(d)
print(min_value)

print("\n\n Exercicio 5\n")
product = "iphone and android phones"
lett_d = {}                                 # inicializa o dicionario
chars = list(product)                       # separa caracteres em uma list
print(chars)

for ch in chars:                            # faz a primeira iteracao para criar o dicionario com valores de cada chave
    if ch not in lett_d:
        lett_d[ch] = 0
    lett_d[ch] = lett_d[ch] + 1
print(lett_d)

keys = lett_d.keys()                        # cria uma lista somente com as chaves
max_value = list(keys)[0]                   # inicializa valor inicial na variavel

for item in keys:
    if lett_d[item] > lett_d[max_value]:    # faz a segunda iteracao onde [compara o valor de cada chave do dicionario com o valor na variavel]
        max_value = item                    # retorna o valor para a variavel caso of if statement seja verdadeiro
print(max_value)




