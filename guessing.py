secret_word = "bottle cap"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_limit >= guess_count:
        if guess_count != guess_limit:
            print("You have " + str(guess_limit) + " guess left!")
            guess = input("Enter a guess: ")
            guess_limit -= 1

        else:
            out_of_guesses = True
if out_of_guesses:
        print("WA WA WA YOU LOSE")

else:
    print("WELL DONE!")