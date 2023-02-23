#filetest = open("arquivo_teste.txt","w")
#
#lines = filetest.write("Aqui esta uma linha de texto\nMais um texto novo adicionado")
#
#
#print(lines)
#
#
#
#filetest.close()




'''
use relative paths to make programs more portable
as absolute paths may cause problems finding files in diferent systems.

RELATIVE = "file_var = open('../foldername/filename.txt')"

ABSOLUTE = "file_var = open('/computerfolder/folder/folder/filename.txt')"

'''

## writing on a file

file_obj = open("squares.txt", "w")        #using 'w' to create/write on a file

for number in range(13):
    square = number * number
    file_obj.write(str(square))
    file_obj.write("\n")             # when writing on a file its important to decide when to put the new line character
file_obj.close()

## using  'with' for files - shorthanded solution for files


with open('squares.txt', 'r') as md:
    for line in md:
        print(int(line) * 256)

        

'''
Steps for reading and processing files in Python
#1. Open the file using with and open.

#2. Use .readlines() to get a list of the lines of text in the file.

#3. Use a for loop to iterate through the strings in the list, each being one line from the file. On each iteration, process that line of text

#4. When you are done extracting data from the file, continue writing your code outside of the indentation. Using with will automatically close the file once the program exits the with block.
'''
