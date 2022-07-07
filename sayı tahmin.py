secrt_number = 2
guess_number =""
guess_count = 0
guess_limit = 3
out_of_guess = False
while secrt_number != guess_number and not(out_of_guess):
    if guess_count < guess_limit:
        guess_number = input("Typee your guess")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You win!")
else:
    print("You lose")