from .objects import *

#game explanation
print("Welcome to project noble! This version of the project is a console run proof-of-concept.")
print("This verision features 4 players, all starting with 500 chips.")
print("Blinds are pre-set to 25 and 50.")
print("You have the pre-flop, post-flop, turn, and river betting rounds.")
print("After the betting rounds are complete, the dealer will input the winner.")
print("Enter 0 at any time to get the menu of options.")
print("Enjoy!\n\n--------------------NEW GAME--------------------\n")

def print_game_info():
    if game.round > 0 and game.round < 5:
        print("\n---Game Info---\n")
        if game.round == 1:
            print("Pre-flop:")
        elif game.round == 2:
            print("Post-flop:")
        elif game.round == 3:
            print("Turn:")
        elif game.round == 4:
            print("River:")


        for player in game.players:
            if player.id == game.dealer.id:
                print("Dealer - ", end="")
            if player.id == game.blindsID["small"]:
                print("Small Blind - ", end="")
            if player.id == game.blindsID["big"]:
                print("Big Blind - ", end="")
            print("Player ", player.id, ": ", player.stack, " chips")

        print("\nPot: ", game.pot)

        print("\nPlayer ", game.get_turn(), "'s turn")

game = Game(50)

p1 = Player(game, 1, 500)
p2 = Player(game, 2, 500)
p3 = Player(game, 3, 500)
p4 = Player(game, 4, 500)

game.new_hand()

while not game.gameOver:
    print_game_info()
    if game.round == 5:
        print("Betting Over\n\nPot: ", game.pot)
        winner = int(input("\nEnter winner of the hand: "))
        print("Player ", winner, " won ", game.pot," chips!")
        game.choose_winner(winner)
        while(True):
            if (len(game.players) == 1):
                continuance = input("Press enter to play another hand: ")
            else:
                continuance = input("Press enter to finish the game: ")
            
            game.new_hand()
            break
    else:
        while True:
            choice = int(input("Enter choice: "))
            if choice < 5 and choice > 0:
                break
            elif choice == 0:
                print("\nEnter 1 to go all-in (or call if you must go all-in)")
                print("Enter 2 to call (or check)")
                print("Enter 3 to raise")
                print("Enter 4 to fold\n")
            else:
                print("Please enter an integer between 0 and 4")
        if choice == 1:
            game.all_in()
        elif choice == 2:
            #validating they have enough chips
            if (game.playersStillInHand[0].stack <= game.roundBets[game.lastRaiseID]):
                game.all_in()
            elif (game.playersStillInHand[0].stack > game.roundBets[game.lastRaiseID]):
                game.call()
        elif choice == 3:
            while (True):
                print("You have ", game.playersStillInHand[0].stack," chips")
                amount = int(input("Enter bet amount: "))
                
                if (amount == -1):
                        break
                elif (amount % game.blinds["big"] != 0):
                    print("Please enter a multiple of ", game.blinds["big"])
                else:
                    if (amount <= 0):
                        print("\nPlease enter a positive, non-zero value\n")
                    elif (amount > game.playersStillInHand[0].stack):
                        print("\nPlease enter an amount less than your current chip amount.\n")
                    elif (amount == game.playersStillInHand[0].stack):
                        print("\nPlease enter 1 to from the main betting menu to go all in.\nEnter -1 to go back to the main betting menu\n")
                    elif (amount < game.roundBets[game.lastRaiseID]):
                        print("\nPlease enter a value greater than the current highest bet.\n")
                    else:
                        game.new_bet(amount)
                        break
        elif choice == 4:
            game.fold()

print("\nPlayer ", game.players[0].id, "wins the game!!!\n")