from .objects import *

#----------------------TESTING-------------------------#

game = Game(50)

p1 = Player(game, 1, 500)
p2 = Player(game, 2, 500)
p3 = Player(game, 3, 500)
p4 = Player(game, 4, 500)

#print all info before game begins
print("Player 1: \nStack: ", p1.stack, "\n")
print("Player 2: \nStack: ", p2.stack, "\n")
print("Player 3: \nStack: ", p3.stack, "\n")
print("Player 4: \nStack: ", p4.stack, "\n")

#sample game

game.new_hand()

#player 1 dealer, no action
#player 2 sm blind, 25 into pot
#player 3 big blind, 50 into pot

print("Called new hand function: \n")
print("Player 1 Stack: ", p1.stack)
print("Player 2 Stack: ", p2.stack)
print("Player 3 Stack: ", p3.stack)
print("Player 4 Stack: ", p4.stack)
print("Pot value: ", game.pot, "\n")

#player 4 calls
game.call()

print("Player 4 calls \n")
print("Player 1 Stack: ", p1.stack)
print("Player 2 Stack: ", p2.stack)
print("Player 3 Stack: ", p3.stack)
print("Player 4 Stack: ", p4.stack)
print("Pot value: ", game.pot, "\n")

#player 1 folds
game.fold()

print("Player 1 folds \n")
print("Player 1 Stack: ", p1.stack)
print("Player 2 Stack: ", p2.stack)
print("Player 3 Stack: ", p3.stack)
print("Player 4 Stack: ", p4.stack)
print("Pot value: ", game.pot, "\n")

#player 2 calls
game.call()

print("Player 2 calls \n")
print("Player 1 Stack: ", p1.stack)
print("Player 2 Stack: ", p2.stack)
print("Player 3 Stack: ", p3.stack)
print("Player 4 Stack: ", p4.stack)
print("Pot value: ", game.pot, "\n")

#player 3 checks
game.call()

print("Player 3 checks \n")
print("Player 1 Stack: ", p1.stack)
print("Player 2 Stack: ", p2.stack)
print("Player 3 Stack: ", p3.stack)
print("Player 4 Stack: ", p4.stack)
print("Pot value: ", game.pot, "\n")

#should print round 2
print("New round\n\nRound: ", game.round)
#game loop

# while game.inProgress:
#   contChoice = input("Would you like to continue the game? Y/N: ")
#   if contChoice == 'N' or contChoice == 'n':
#     game.inProgress = False
#   else:
#     print("Continuing game...")
#     game.new_hand()
#     print(game.round, " round: \n")
    
#     print("Player ", game.get_turn().id,"'s turn to bet")
#     bet = input("Player", game.get_turn().id, "'s bet: ")
#     #if bet < last_bet
#       #try again

#     #elif bet > player.stack
#       #try again

#     #elif bet == player.stack
#       #all-in

#     #elif bet == last_bet
#       #game.call(amount)

#     #else
#       #game.new_bet(amount)