
# ᗷᒪᗩᑕᛕᒎᗩᑕᛕ

#print(''' 
    ######     #         #         #####    #     #   ####   #         #####    #     #                                                                    
    #      #   #         ##       #     #   #    #        #  ##       #     #   #    #                                                                             
    #      #   #         # #      #         #   #         #  # #      #         #   #                                                                                 
    #******    #         #  #     #         #**#          #  #  #     #         #**#                                                                           
    #      #   #         #***#    #         #   #         #  #***#    #         #   #                                                                             
    #       #  #      #  #    #   #      #  #    #  #     #  #    #   #      #  #    #                                                                                  
    ########   #######   #     #   ######   #     #  #####   #     #   ######   #     #
                                                                                           
#''')
import random

player_card = ''
cards_list = []

###Выдает  по одному элементу в лист и обновляет 
#cards_list.append(random.choices(['A','K','Q','J','10','9','8','7','6','5','4','3','2'], k=10))# + random.choice(['♠','♣','♢','♡'])

###


# print(cards_list)
# Не работает .append()




# answer = input("1Enter Yes or No => ")
# print("You entered " + answer)
answer = ""

def player_answer(answer, count = True):
    answer = input("2Enter Yes or No => ")
    if "Y" in answer:
        count  = True
    elif "N" in answer :
        count = False
    return count



def deck(sequence, suit):
    while player_answer(answer) == True:
        playing_card = random.choice(sequence) + random.choice(suit)
        cards_list.append(playing_card)
        print(cards_list)
    else :
        # print(cards_list)
        return cards_list
print(deck("AKQJ🔟98765432", "♠♣♢♡"))
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
