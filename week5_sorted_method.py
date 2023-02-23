
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
'''
def second_let(st):
    char_lst = []
    for i in st:
        char_lst.append(i[1])
    return char_lst

sorted_by_second_let = sorted(second_let(ex_lst))
print(sorted_by_second_let)'''

def second_let(x):
    return x[1]

sorted_by_second_let= sorted(ex_lst, key= second_let)
print(sorted_by_second_let)
  ## just sorted the same list and saved in a diferent variable
   # and not create a new list with the sorted characters

print("\n2. Below, we have provided a list of strings called nums.\nWrite a function called last_char that takes a string as input, and returns only its last character.\nUse this function to sort the list nums by the last digit of each number, from highest to lowest, and save this as a new list called nums_sorted.\n")
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

def last_char(n):
    return n[-1]
nums_sorted = sorted(nums, reverse=True, key=last_char)
print("Answer: ", nums_sorted)
print(last_char("Jollene"))


print("\n3.Once again, sort the list nums based on the last digit of each number from highest to lowest.\nHowever, now you should do so by writing a lambda function. Save the new list as nums_sorted_lambda.\n")


nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']

nums_sorted_lambda = sorted(nums, reverse = True, key = lambda n: n[-1])

print("Answer: ", nums_sorted_lambda)