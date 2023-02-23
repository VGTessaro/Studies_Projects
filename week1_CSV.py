## Using .CSV in Python

## create or read a cvs file
# the use of .join() and .split()

'''Reading CSV'''

newf = open('testecsv.csv','w')

newf.write(
    
"Name,Score,Grade,Age\n"
"Jamal,98,A+,18\n"
"Eloise,87,B+,16\n"
"Madeline,99,A+,17\n"
"Wei,94,A,17\n"
           
           )
print(newf)
newf.close()

bulletin = open("testecsv.csv", 'r')
lines = bulletin.readlines()
header = lines[0]
header_sep = header.strip().split(",")
print(header_sep)
for row in lines[1:]:
    values = row.strip().split(",")   ##this combined method is useful to get info from a csv file
    if values[2] == "A+":
        print("{}|{}|{}".format(values[0], values[2], values[3]))

bulletin.close()


'''Writing in .CSV'''

'''Start with the information to parse into the file'''

athletes = [("Carla","24","F","Speed Skates"),("Juuta","22","F","Speed Skates"),("Dude","28","M","Swimming"),("Dude 2","26","M","Jumping")]
# output the header row
header_row = 'Name,Age,Sex,Sport'
endfile = open("athletes.csv", "w")
endfile.write(header_row)
endfile.write("\n")

for athlete in athletes:
    ##row_string = ",".join(athlete) #better used if all values are strings

    row_string = "{},{},{},{}".format(athlete[0], athlete[1], athlete[2], athlete[3])
    #the method above requires that all velues are present in the tuples otherwise returns an error
    endfile.write(row_string)
    endfile.write("\n")
endfile.close()


