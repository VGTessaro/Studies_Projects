print("\nCARTOES\n")
card_id = int(input("Digite o numero do cartao: ""\n"))
card_read = 1
found_card = False

while card_read != 0 and not found_card:
    card_read = (int(input("Digite o proximo cartao: ")))
    if card_read == card_id:
        found_card = True

if found_card:
    print("FOUND!")
else:
    print("NO NO NOT FOUND")