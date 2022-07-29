# Bagles Game
import random

# n-digit number
MAX_DIGITNUMBER = 3

# Getting Random 3-digit number without any repeating
def get_secretNUm():
    numbers = [1,2,3,4,5,6,7,8,9,0]
    random.shuffle(numbers)
    secretNumber = ''
    for i in range(MAX_DIGITNUMBER):
        secretNumber += str(numbers[i])
    return secretNumber

def get_clues(guess,secret_number):
    clues = []
    if guess == secret_number:
        clues.append("You_WON")

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Femi")

        elif guess[i] in secret_number:
            clues.append("Piko")

    if len(clues) == 0:
        clues.append("Bagles")

    return ' '.join(clues)

def main():
    # User Attempts
    LIVES = 10
    print("Hello Welcome to my Bagles Game")
    print(" Rules:")
    print("     1) Digits Cannot Repeat!")
    print("     2) Piko: Digit is correct but in the wrong place")
    print("     3) Femi: Digit is coorect in the correct place")
    print("     4) Bagles: Nothing is correct")
    print("\nYou have 10 Attempts Good Luck!")
    secret_number = get_secretNUm()
    lives  = 10
    while True:
        try:
            user_guess = input(">>")
            output = get_clues(user_guess,secret_number)

            if  "You_WON" in output:
                print("You WON!")
                break

            LIVES -= 1
            if LIVES == 0:
                print("YOU LOST")
                print(f"SECRET NUMBER WAS: {secret_number}")
                break

            print(f"Attempts left: {LIVES}")
            print(output)

        except ValueError:
            print("You Didn't Enter a Digit")

main()



