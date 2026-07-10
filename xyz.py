import csv
import random

with open("Top Trumps - Skyscrapers.csv", mode ="r") as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)


print("Welcome to the Top Trumps Game, Skyscrapers theme")
print('Make your choices wisely and try to win all the cards')
print('Click Enter to begin')

input()

def display_card(card):
  # Display the attributes of a card
  # A card is a dictionary with several attributes

  max_chars = 0
  
  for keys in card:
    if len(keys) > max_chars:
      max_chars = len(keys)
  
  for keys in card:
    print(keys, (max_chars-len(keys))*' ', ': ', card[keys])
  
def determine_winner(m1, m2, order = 1):
  # Explain why this concise code is useful
  dct = {'player': m1, 'computer': m2}
  v = list(dct.values())
  k = list(dct.keys())

  if m1 == m2:
    return 'draw'
  else:
    if order == 1:
      return k[v.index(max(v))]
    else:
      return k[v.index(min(v))]
    

random.shuffle(all_cards)

comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []
game_over = False
chance = 'player'

# We need an identfier for each of the meaninful attributes
#
# We can create a new dictionary
relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[2::]

# Create a mapping dictionary
# Short Cut : Long Key
# for every key in the keys
mapping_dict = {}

for key in relevant_keys:
  mapping_dict[key[0]] = key

input()



while not game_over:

  print('player cards: ', len(player_cards), 'computer cards: ', len(comput_cards), 'table_cards: ', len(table_cards))
  
  player = player_cards.pop(0)
  comput = comput_cards.pop(0)

  table_cards.append(player)
  table_cards.append(comput)

  print()
  print(f'It is now {chance}\'s chance')
  print()

  print('Your (Player) card is ')
  display_card(player)
  print()

  if chance == 'player':
    # Determine which attribute
    chosen_key = input('What is your choice?')
    if chosen_key not in list(mapping_dict.keys()):
      print("Incorrect input, selecting randomly")
      chosen_key = random.choice(list(mapping_dict.keys()))
    chance = 'computer'    

  else:
    # Choose a random attribute from the mapping directory
    chosen_key = random.choice(list(mapping_dict.keys()))
    chance = 'player'


  key_requested = mapping_dict[chosen_key]
  value_player = player[key_requested]
  value_comput = comput[key_requested]
  
  print('Key of interest is ', key_requested)

  if chosen_key in ['H','F', 'B']:
    winner = determine_winner(float(value_player), float(value_comput)); 
  else:
    winner = determine_winner(float(value_player), float(value_comput), 0); 
    
  player_rank = category_rank(player, chosen_key)
  comput_rank = category_rank(comput, chosen_key)
  
  print('Player ', key_requested, 'is', value_player,"(rank =",player_rank,")")
  print('Computer ', key_requested, 'is', value_comput, "(rank =",comput_rank,")")
  print()
  print('Winner is ... ', winner)
  input()

  # Re-distribute the cards
  # Notice, in case of DRAW, noone takes the cards. 

  addn_cards_ex = abs(player_rank - comput_rank)//6

  if winner == 'player':
    player_cards.extend(table_cards)
    table_cards.clear()
    
    # Additional card exhange
    cards_exch = min(addn_cards_ex, len(comput_cards))
    new_cards = []
    for _ in range(cards_exch):
      new_cards.append(comput_cards.pop(0))
    player_cards.extend(new_cards)

  elif winner == 'computer':
    comput_cards.extend(table_cards)
    table_cards.clear()

    # Additional card exhange
    cards_exch = min(addn_cards_ex, len(player_cards))
    new_cards = []
    for _ in range(cards_exch):
      new_cards.append(player_cards.pop(0))
    comput_cards.extend(new_cards)

  if len(player_cards) == 0:
    print('Computer Won')
    game_over = True
  elif len(comput_cards) == 0:
    print('Player Won')
    game_over = True





