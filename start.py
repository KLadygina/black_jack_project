import random
import os 

os.system('cls')



print("ᗷ ᒪ ᗩ ᑕ ᛕ  ᒎ ᗩ ᑕ ᛕ")

# print(''' 
    ######     #         #         #####    #     #   ####   #         #####    #     #                                                                    
    #      #   #         ##       #     #   #    #        #  ##       #     #   #    #                                                                             
    #      #   #         # #      #         #   #         #  # #      #         #   #                                                                                 
    #******    #         #  #     #         #**#          #  #  #     #         #**#                                                                           
    #      #   #         #***#    #         #   #         #  #***#    #         #   #                                                                             
    #       #  #      #  #    #   #      #  #    #  #     #  #    #   #      #  #    #                                                                                  
    ########   #######   #     #   ######   #     #  #####   #     #   ######   #     #
                                                                                           
#''')


player_card = ''
cards_list = []

###Выдает  по одному элементу в лист и обновляет 
#cards_list.append(random.choices(['A','K','Q','J','10','9','8','7','6','5','4','3','2'], k=10))# + random.choice(['♠','♣','♢','♡'])

###


##Correspondence with a user
answer = ""

def player_answer(answer, count = True):
    answer = input("2Enter Yes or No => ")
    if "Y" in answer or "y" in answer:
        count  = True
    elif "N" in answer or "n" in answer:
        count = False
    return count

##Checks if a card is alreadyy in card_list
def card_check(cards_list, card_to_add):
    for card in cards_list:
        if card != card_to_add:
            print("The card can be added")
            print(card)
            return True
        return False
    if len(cards_list) == 0:
        return True
    return False
    

##Adding to a list random cards
def deck(sequence, suit):
    while player_answer(answer) == True:
        playing_card = random.choice(sequence) + random.choice(suit)
        # print(len(cards_list))
        if card_check(cards_list, playing_card) == True:
            cards_list.append(playing_card)
        else:
            print("Your card {} is already exist in card_list", playing_card)
        print(cards_list)
    else :
        print(cards_list)
        return cards_list
    
##Calling a deck function with one suit
print(deck("AKQJ🔟98765432", "♠"))

##Calling a deck function with all suits
# print(deck("AKQJ🔟98765432", "♠♣♢♡"))

print(cards_list)
# for i in range(1, 10):
#     playing_card = i
#     cards_list.append(playing_card)
# print(cards_list)


# print(cards_list)
# # Не работает .append()
# def deck(sequence, count):
#     # playing_card = random.choice(sequence)
#     i = 0
#     while i <= count:
#         cards_list.append(random.choice(sequence))
#     return cards_list
# # print(deck("AKQJ🔟98765432", "♠♣♢♡"))
# print(deck(['A♠','K♠','Q♠']))
# # print(cards_list)
