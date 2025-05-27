class Game:
  def __init__(self, bigBlind):
    if bigBlind < 2:
      raise ValueError("Big blind cannot be less than 2")

    #player list where players are NOT REMOVED
    #dealer is the first player, then moves to the back of the order after the hand, then first player becomes dealer
    #this list is the order of betting
    #will start with dealer, then small blind, then big blind
    #assume everyone in list is still in game
    self.players = list()

    #tracking blinds
    self.blinds = {"small" : int(bigBlind / 2), "big" : bigBlind}
    self.blindsID = {"small" : 0, "big" : 0}

    #creating the pot, will be a value
    self.pot = 0

    #dictionary to hold the player id : current amount in pot for the hand
    self.roundBets = dict()

    #setting the betting round (1 = pre-flop, 2 = post-flop, 3 = turn, 4 = river)
    self.round = 1
    
    #tracking the last player to raise
    self.lastRaiseID = 0

    #to keep the order of the players, to remove players that folded/went all in
    #will add players that went all in back into the list after
    self.playersStillInHand = list()

    #tracks if game is over
    self.gameOver = False

  def next_round(self):
    self.reset_round_bets()
    for player in self.playersStillInHand:
      if player.stack == 0:
        self.advance_turn()
        continue
    self.lastRaiseID = self.playersStillInHand[0].id

  def add_to_pot(self, amount):
    self.pot += amount

  def move_dealer_to_end(self):
    self.dealer = self.players[0]
    self.players.append(self.players[0])
    self.players.pop(0)

  def new_hand(self):
    self.round = 1
    #reset the players still betting list
    self.playersStillInHand = list()

    #remove players with 0 chips in stack
    i = 0
    j = len(self.players)
    while i < j:
      if self.players[i].stack == 0:
        self.players.pop(i)
        j -= 1
      else:
        i += 1

    if len(self.players) == 1:
      self.gameOver = True
    else:
      #move dealer to end of players array
      self.move_dealer_to_end()

      for player in self.players:
        self.playersStillInHand.append(player)

      #resetting pot to 0
      self.pot = 0

      #resetting the dictionary that holds the bets per round
      self.reset_round_bets()

      #handle blinds
      self.blindsID["small"] = self.playersStillInHand[0].id
      self.new_bet(self.blinds["small"])
      self.blindsID["big"] = self.playersStillInHand[0].id
      self.new_bet(self.blinds["big"])
      self.lastRaiseID = self.playersStillInHand[0].id

  def reset_round_bets(self):
    self.roundBets = dict()
    for player in self.playersStillInHand:
      self.roundBets.update({player.id : 0})

  def track_bet(self, id, amount):
    currentAmount = self.roundBets[id]
    currentAmount += amount
    self.roundBets[id] = currentAmount

  def check_round_end(self):
    #if either 1 or 0 people still left in hand, skip to winner function
    if (not self.playersStillInHand) or (len(self.playersStillInHand) == 1):
      self.round = 5
    elif (self.lastRaiseID == self.playersStillInHand[0].id):
      self.round += 1
      self.next_round()

  def advance_turn(self):
    self.playersStillInHand.append(self.playersStillInHand[0])
    self.playersStillInHand.pop(0)
    self.check_round_end()
    if self.playersStillInHand[0].stack == 0:
      self.advance_turn()

  #write this function
  def find_player_by_id(self, id):
    return self.players[id - 2]

  #input the id of the winner of the game
  def choose_winner(self, id):
    winner = self.find_player_by_id(id)
    winner.add_chips(self.pot)

  #must override call function
  #handles all_in only if a raise
  def all_in(self):
    amount = self.playersStillInHand[0].stack
    if amount > self.find_largest_bet():
      self.new_bet(amount)
      self.check_round_end()
      self.playersStillInHand.pop(-1)
      
      #handles the case where going all in calls or is less than prev bet
    else:
      self.playersStillInHand[0].remove_chips(amount)
      self.pot += amount

      self.track_bet(self.playersStillInHand[0].id, amount)    
      
      self.check_round_end()
      self.playersStillInHand.pop(0)

  #adding a player to the game
  def add_to_game(self, player):
    #add the player to the game
    self.players.append(player)

  #might need to update to use lastRaiseID, more efficient
  def find_largest_bet(self):
    largest = 0
    for id in self.roundBets:
      if self.roundBets[id] > largest:
        largest = self.roundBets[id]
    return largest

  #all-in function overrides call function
  #need to go over if calling makes you go all-in
  def call(self):
    amount_to_call = self.find_largest_bet()
    amount_to_call -= self.roundBets[self.playersStillInHand[0].id]
    
    self.playersStillInHand[0].remove_chips(amount_to_call)
    self.pot += amount_to_call

    self.track_bet(self.playersStillInHand[0].id, amount_to_call)    

    self.advance_turn()

  def fold(self):
    if self.lastRaiseID == self.playersStillInHand[0].id:
      self.lastRaiseID = self.playersStillInHand[1].id
    self.playersStillInHand.pop(0)
    self.check_round_end()

  #will handle either new bets or raises
  def new_bet(self, amount):
    self.playersStillInHand[0].remove_chips(amount)
    self.pot += amount
    self.lastRaiseID = self.playersStillInHand[0].id

    #add bet to dictionary
    self.track_bet(self.playersStillInHand[0].id, amount)    

    self.advance_turn()

  #purely for debugging purposes
  def get_turn(self):
    return self.playersStillInHand[0].id

class Player:
  def __init__(self, game, id, startingAmount):
    #error checking
    if startingAmount < game.blinds["big"]:
        raise ValueError("Player starting amount cannot be less than big blind.")

    self.id = id
    self.stack = startingAmount
    game.add_to_game(self)

  def remove_chips(self, amount):
    self.stack -= amount

  def add_chips(self, amount):
    self.stack += amount