import random,sys

#Final Variables declaration
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS =  chr(9827)


#possible user moves
ACTIONS = ['a','s','d','c']

#Function that returning random card with random suite
def get_card() :
    cards = ['2','3','4','5','6','7','8','9','10',"Jack","Queen","King","Ace"]
    cards_suits = [HEARTS,DIAMONDS,SPADES,CLUBS]

    random_card_value_choice = random.choice(cards)
    random_card_suite_choice = random.choice(cards_suits)

    #Returning Tuple
    return random_card_value_choice,random_card_suite_choice


def get_points(current_user_deck:list):
    points = 0
    for i in range(len(current_user_deck)):
        #Ace situation
        if current_user_deck[i][0] == "Ace":
            if points + 11 > 21:
                points+=1
            else:
                points += 11

        #if card is a number
        elif current_user_deck[i][0].isdigit():
            points += int(current_user_deck[i][0])

        # if card is a 'jack' 'queen' 'king'
        else:
            points += 10
    return points

def check_win(user_points:int,croupier_points:int) :

    if user_points > 21:
        return False

    elif user_points == 21:
        if croupier_points == 21:
            return "draw"

        return True

    elif croupier_points > 21:
        return True



#Main Function
def main():
    user_deck = []
    croupier_deck = []

    #Welcome message
    print('''
    --- Welcome to my BlackJack Game ---\n
    'D'  -  Get Another Card 
    'C'  -  Check Your Cards
    'S'  -  Check Croupier Cards 
    'A'  -  Double Bet Money
    'H'  - Stop Game\n
    ''')

    #User bet money
    try:
        user_money = int(input("Your Bet: "))
    except ValueError:
        user_money = 0
        print("Enter a Integer")

    #Game
    while True:

        #Getting user Move
        user_action = input("Your Move: ")
        user_action = user_action.lower()


        if user_action == "d":

            #User move
            user_picked_card = get_card()
            user_deck.append(user_picked_card)
            print(f"Dobrales {user_picked_card[0]} {user_picked_card[1]} Punkty: {get_points(user_deck)}")

            #Croupier Move
            croupier_picked_card = get_card()
            croupier_deck.append(croupier_picked_card)
            print( f"Krupier Pokazuje {croupier_picked_card[0]}  {croupier_picked_card[1]} Punkty: {get_points(croupier_deck)}")

            #Showing current bet
            print("\nPostawione pieniadze: ",user_money)

            #Getting Current points to use 'check_win' function
            user_points = get_points(user_deck)
            crupier_points = get_points(croupier_deck)
            #Checking Win
            if check_win(user_points, crupier_points) == True:
                print("WYGRANA!",user_money)
                break

            elif  check_win(user_points,crupier_points) == False:
                print("PRZEGRANA",user_money)
                break

            elif check_win(user_points, crupier_points) == "draw":
                print("Remis postawione pienadze zostana ci zwrocone")
                break
            else:
                pass


        #Checking user deck
        if user_action == "c":
            print("\nTWOJE KARTY:")
            for i in range(len(user_deck)):
                print(" "*i,f"[{user_deck[i][0]}  {user_deck[i][1]}]")
            user_points = get_points(user_deck)
            print("Twoje punkty: ",user_points)

        #Checking croupier deck
        if user_action == "s":
            print("\nKARTY KRUPIERA:")
            for i in range(len(croupier_deck)):
                print(" " * i, f"[{croupier_deck[i][0]}  {croupier_deck[i][1]}]")
            crupier_points = get_points(croupier_deck)
            print("Punkty Krupiera: ",crupier_points)

        #Double money
        if user_action ==  'a':
            user_money *= 2
            print("Podwoiles swoje pieniadze aktualnie masz: ",user_money)

        #Stop playing
        if user_action == 'h':
            print(f"Zatrzymuje gre odchodzisz z {user_money} ")
            break


#Calling main function
main()