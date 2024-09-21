import random
import os 
import card_to_val as ctv
os.system('cls')
    

def game_intro():
    intro_text = """
=======================================
      WELCOME TO BLACKJACK TERMINAL GAME
=======================================
    Rules:
    - Try to get as close to 21 as possible without going over.
    - Face cards are worth 10 points, and Aces can be worth 1 or 11.
    - You can choose to 'Hit' to draw a new card or 'Stand' to keep your current total.
    
    Commands:
    - Hit: 'h' or '+'
    - Stand: 'st' or '='
    - Surrender: 'sur' or '-'
    
    Good luck, and let's see who wins, you or the dealer!
=======================================
    """
    print(intro_text)    

def players_amount():
    amount = int(input('How many players will play? Choose 1 to 3 \n'))
    if amount == 1:
        user_1 = input('How can we call you?\n')
    else:
        print("Oops, looks like this amount is not available at the moment")
        return players_amount()


class BlackJack:
    def __init__(self, players_count = 1):
        self.players_count = players_count
        self.cards_list = []
        self.player_hand = []
        self.dealer_hand = []
        self.total_player = 0
        self.total_dealer = 0
        self.answer = ""
        game_intro()
    
    
    def get_answer(self):
        ans = input("-> ")
        if ans.lower() in ["h", "+"]:
            return True
        elif ans.lower() in ["st", "="]:
            return False
        elif ans.lower() in ["sur", "-"]:
            return False
        else:
            print("Oops, looks like we do not have this option. Please try again!")
            return self.get_answer()

    
    def make_a_card(self):
        self.cards_list = ['A', 'J', 'K', 'Q', 2, 3, 4, 5, 6, 7, 8, 9, 10]
        suits_list = ['♠', '♣', '♢', '♡']
        current_card = str(random.choice(self.cards_list)) + random.choice(suits_list)
        return current_card
    
    def new_game(self):
        new_game_answer = input("Start new game? (yes/no) ")
        if new_game_answer.lower() in ("yes", "y"):
            self.total_player = 0
            self.total_dealer = 0
            self.dealer_hand = []
            self.player_hand = []  # Reset player's hand
            game_intro()  # Call the intro function here
            return self.get_player_hand()  # Start a new game
        elif new_game_answer.lower() in ("no", "n"):
            return "Thank you!"

    def get_player_hand(self):
        # The dealer gives me a card
        self.player_hand.append(self.make_a_card())
        # Declaring a card
        card_value = self.player_hand[0][:-1]
        val_from_dict = ctv.card_to_val[card_value]
        # Here we evaluate our total_player
        #First we will ckeck whether our value is Int or tuple
        if isinstance(val_from_dict, int):
            self.total_player += val_from_dict
            print("The value from dict is int: "+ str(self.player_hand[0]))
        else:
            if self.total_player < 10:
                print("We are adding " + str(val_from_dict[0]) + "Player's total is "+ str(self.total_player))
                self.total_player += val_from_dict[0]  # Update total_player with first item in the tuple 
            elif self.total_player >= 10:
                print("We are adding " + str(val_from_dict[1]) + "Player's total is "+ str(self.total_player))
                self.total_player += val_from_dict[1]  # Update total_player with second item in the tuple 
            
        print("Your CARD is {0}. The TOTAL is {1}".format(self.player_hand[0], self.total_player))
        
        
        for card in self.player_hand:
            # Create a card only if the total_player < 21 or the answer is True
            while self.total_player < 21:
                if self.get_answer():
                    self.player_hand.append(self.make_a_card())
                    # Here we should make sure the A is calculated correctly
                    #First we will ckeck whether our value is Int or Tuple
                    if isinstance(val_from_dict, int):
                        self.total_player += val_from_dict
                        print("The value from dict is int: "+ str(self.player_hand[:-1]))
                    else:
                        if self.total_player < 10:
                            print("We are adding " + str(val_from_dict[0]) + "Player's total is "+ str(self.total_player))
                            self.total_player += val_from_dict[0]  # Update total_player with first item in the tuple 
                        elif self.total_player >= 10:
                            print("We are adding " + str(val_from_dict[1]) + "Player's total is "+ str(self.total_player))
                            self.total_player += val_from_dict[1]  # Update total_player with second item in the tuple 

                    print("Your new CARD is {0}. The TOTAL is {1}".format(self.player_hand[-1], self.total_player))
                elif not self.get_answer():
                    self.get_dealer_hand()
                
            if self.total_player == 21:
                return "You won!"
            elif self.total_player > 21:
                print("Sorry, your total is more than 21")
                return self.new_game() 
    
    def get_dealer_hand(self):
        # The dealer gives me a card
        self.dealer_hand.append(self.make_a_card())
        card_value = self.dealer_hand[0][:-1]
        val_from_dict = ctv.card_to_val[card_value]
        # Declaring a card
        #First we will ckeck whether our value is Int or Tuple
        if isinstance(val_from_dict, int):
            self.total_dealer += val_from_dict
            print("The dealer's card value is int: "+ str(self.dealer_hand[0]))
        else:
            if self.total_dealer < 10:
                print("We are adding " + str(val_from_dict[0]) + "Dealer's total is "+ str(self.total_dealer))
                self.total_dealer += val_from_dict[0]  # Update total_player with first item in the tuple 
            elif self.total_dealer >= 10:
                print("We are adding " + str(val_from_dict[1]) + "Dealer's total is "+ str(self.total_dealer))
                self.total_dealer += val_from_dict[1]  # Update total_player with second item in the tuple 
        print("Dealer's CARD is {0}. The TOTAL is {1}".format(card_value, self.total_dealer))
        
        
        for card in self.dealer_hand:
            # Create a card only if the total_player < 21 or the answer is True
            while self.total_dealer < 21:
                self.dealer_hand.append(self.make_a_card())
                # Here we should to make sure the A is calculated coorectly
                card_value = self.dealer_hand[-1][:-1]
                val_from_dict = ctv.card_to_val[card_value]
                if isinstance(val_from_dict, int):
                    self.total_dealer += val_from_dict
                    print("The dealer's new card value is int: "+ str(self.dealer_hand[:-1]))
                else:
                    if self.total_dealer < 10:
                        print("We are adding " + str(val_from_dict[0]) + "Dealer's total is "+ str(self.total_dealer))
                        self.total_dealer += val_from_dict[0]  # Update total_player with first item in the tuple 
                    elif self.total_dealer >= 10:
                        print("We are adding " + str(val_from_dict[1]) + "Dealer's total is "+ str(self.total_dealer))
                        self.total_dealer += val_from_dict[1]  # Update total_player with second item in the tuple 

                print("Dealer's new CARD is {0}. The TOTAL is {1}".format(self.player_hand[-1], self.total_dealer))
                               
            if self.total_dealer == 21:
                return "Dealer won!"
            elif self.total_dealer > 21:
                self.find_max_total(self.total_player, self.total_dealer)
            else:
                return "Dealer loose!"   
                
    def find_max_total(self, player_total=0, dealer_total=0):
        if player_total >= dealer_total:
            return "Congrats, your total is greater or equal.You won!"
        elif player_total < dealer_total:
            print("Sorry, your total is less then dealers one")
            return self.new_game()

    
        
        


    # def total_count(self):
    #     total_player = 0
    #     card = self.player_hand[0]
    #     card_val = card[:-1]
    #     while total_player <= 21:
    #         total_player += ctv.card_to_val[card_val]
    #     return card_val 
    
    
    def user_input(self, answer):
        user_answer = input("->")
        if user_answer == 'H' or '+':
            self.hit()

    def hit(self):
        print("Hit!")
    


        
    
    
    
    


    
# greet() 
# players_amount()
game1 = BlackJack()
print(game1.get_player_hand())
# print(game1.get_answer())
# game1.total_count()

