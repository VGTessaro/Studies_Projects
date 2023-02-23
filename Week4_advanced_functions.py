## OPTIONAL PARAMETERS

'''
WHEN DEFINING A FUNCTIONS ITS POSSIBLE TO
ATRIBUTE A DEFAULT VALUE FOR THE PARAMETERS,
CAUSING THE FUNCTION TO WORK EVEN WITHOUT AN INPUT
'''

def funcao(x,y=3):
    resultado = x * y
    return resultado

print(funcao(3)) # the 3 passed in the function is positionally atached to the 1st positional argument

'''
keyword argument should always come after specified parameters
'''
