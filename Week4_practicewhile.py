def info(name,age,height,weight,perims):

    # coletar nome
    name = ""
    file = open(get_name(name) + ".csv", "w")
    # coletar idade, altura, peso
    # coletar perimetros


    get_pers_info(age,height,weight)
    get_measure(perims)

    # save all information from the input into a database (.csv)
    # show organized date and calculations based in the data

def get_name(nam):
    while True:
        nam = input("write your name: ")
        if nam == "":
            print("Please write your name:")
            continue
        else:
            return nam

print(get_name(name))