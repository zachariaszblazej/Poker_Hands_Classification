#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd


# In[11]:


def hands_to_dataframe(hands_list, figure_type):
    
    poker_figures = {'Two_pairs': 2,
                     'Three_of_a_kind': 3,
                     'Straight': 4,
                     'Flush': 5,
                     'Full_house': 6,
                     'Four_of_a_kind': 7,
                     'Straight_flush': 8,
                     'Royal_flush': 9}
    
    column_names = ['S1', 'C1', 'S2', 'C2', 'S3', 'C3', 'S4', 'C4', 'S5', 'C5', 'Poker Hand']
    
    df = pd.DataFrame(columns=column_names)
    
    for hand in hands_list:
        
        row = pd.Series(data=np.zeros(len(column_names)),index=column_names, dtype='int')

        for n in range(1,6):
            row[f'S{n}'] = hand[n-1][0]
            row[f'C{n}'] = hand[n-1][1]

        row['Poker Hand'] = poker_figures[figure_type]
        
        df = df.append(row, ignore_index=True)
        
    return df

def if_flush_straight(cards_numbers):
    
    sorted_numbers = sorted(cards_numbers, reverse=True) 
    highest_number = cards_numbers.max()
    straight_order = list( np.arange(highest_number, highest_number-5, -1) )
    
    return sorted_numbers == straight_order

def is_hand_duplicate(new_hand, hands_list):
    
    result = False
        
    for hand in hands_list:
        if new_hand == hand:
            result = True
            break
            
    return result

def generate_two_pairs_observation():
    
    cards = []
            
    pair_1_number, pair_2_number, other = np.random.choice(np.arange(1,14), size=3, replace=False)
    
    pair_1_suits = np.random.choice(np.arange(1,5), size=2, replace=False)
    pair_1 = [ (suit, pair_1_number) for suit in pair_1_suits ]
    cards.extend(pair_1)
    
    pair_2_suits = np.random.choice(np.arange(1,5), size=2, replace=False)
    pair_2 = [ (suit, pair_2_number) for suit in pair_2_suits ]
    cards.extend(pair_2)
    
    cards.append( (np.random.randint(1,5), other) )
    
    np.random.shuffle(cards)
    
    return cards

def generate_three_of_a_kind_observation():
    
    triple_card_number, other_1, other_2 = np.random.choice(np.arange(1,14), size=3, replace=False)
            
    triple_card_suits = np.random.choice(np.arange(1,5), size=3, replace=False) 
    cards = [(suit, triple_card_number) for suit in triple_card_suits ]
    
    cards.append( (np.random.randint(1,5), other_1) )
    
    cards.append( (np.random.randint(1,5), other_2) )
    
    np.random.shuffle(cards)
    
    return cards

def generate_straight_observation():
    
    is_flush = True
            
    while is_flush:
        suits = np.random.choice(np.arange(1,5), size=5)
        is_flush = len(set(suits)) == 1
    
    highs_possible = list(np.arange(5,14))
    highs_possible.append(1)
    
    card_numbers = []
    highest_number = np.random.choice(highs_possible)
    card_numbers.append(highest_number)
    
    rest = [10,11,12,13] if highest_number == 1 else np.arange(highest_number-1, highest_number-5, -1)
    card_numbers.extend(rest)
    np.random.shuffle(card_numbers)
    
    cards = [(s,n) for s,n in zip(suits, card_numbers)]
    
    return cards

def generate_flush_observation(kind='royal'):
    
    suit = np.random.randint(1,5)
    hand_suit = [suit for i in range(5)]
    
    royals = [1, 10, 11, 12, 13]
    numbers_to_choose_from = royals
    
    if kind == 'straight':
        highest_number = np.random.randint(5,14)
        lowest_number = highest_number - 4
        numbers_to_choose_from = np.arange(highest_number, lowest_number-1, -1)
    
    if kind == 'normal':
        is_straight = True
    
    while kind == 'normal' and (royals == sorted(numbers_to_choose_from) or is_straight):
        numbers_to_choose_from = np.random.choice( np.arange(1,14), size=5, replace=False )
        is_straight = if_flush_straight(numbers_to_choose_from)
    
    
    #card_numbers = np.random.choice(numbers_to_choose_from, size=5, replace=False)
    
    cards = [ (s, n) for s, n in zip(hand_suit, numbers_to_choose_from) ]
    
    np.random.shuffle(cards)
    
    return cards

def generate_full_house_observation():
    
    triple_card_number, pair_card_number = np.random.choice(np.arange(1,14), size=2, replace=False)
            
    triple_suits = np.random.choice(np.arange(1,5), size=3, replace=False)
    pair_suits = np.random.choice(np.arange(1,5), size=2, replace=False)
    
    triple = [(suit, triple_card_number) for suit in triple_suits]
    pair = [(suit, pair_card_number) for suit in pair_suits]
    
    cards = triple + pair
    np.random.shuffle(cards)
    
    return cards

def generate_four_of_a_kind_observation():
    
    main_cards_number, fifth_card_number = np.random.choice(np.arange(1,14), size=2, replace=False)
    fifth_card_suit = np.random.randint(1,5)
    
    cards = [(i+1, main_cards_number) for i in range(4)]
    
    fifth_card = (fifth_card_suit, fifth_card_number)
    cards.append(fifth_card)
    
    np.random.shuffle(cards)
    
    return cards


def generate_poker_observations(size, figure):
    
    hands_list = []
    
    for s in range(size):
        
        is_duplicate = True
        
        while is_duplicate:
            
            if figure == 'Two_pairs':
                cards = generate_two_pairs_observation()
            
            elif figure == 'Three_of_a_kind':
                cards = generate_three_of_a_kind_observation()
            
            elif figure == 'Straight':
                cards = generate_straight_observation()
            
            elif figure == 'Flush':
                cards = generate_flush_observation(kind='normal')
            
            elif figure == 'Full_house':
                cards = generate_full_house_observation()
            
            elif figure == 'Four_of_a_kind':
                cards = generate_four_of_a_kind_observation()
            
            elif figure == 'Straight_flush':
                cards = generate_flush_observation(kind='straight')
            
            elif figure == 'Royal_flush':
                cards = generate_flush_observation()
            
            is_duplicate = is_hand_duplicate(cards, hands_list)
            
        
        hands_list.append(cards)
            
    df = hands_to_dataframe(hands_list, figure)
    
    return df

def generate_poker_dataset(existing_set, size):
    
    TOTAL_NUMBER_OF_ROYAL_FLUSH_COMBINATIONS = 480
    TOTAL_NUMBER_OF_STRAIGHT_FLUSH_COMBINATIONS = 4320
    
    existing_set = existing_set.drop_duplicates()
    
    nothing_hands = existing_set[existing_set['Poker Hand'] == 0]
    
    one_pair_hands = existing_set[existing_set['Poker Hand'] == 1]
    
    two_pair_hands = generate_poker_observations(size, 'Two_pairs')
    
    three_of_a_kind_hands = generate_poker_observations(size, 'Three_of_a_kind')
    
    straight_hands = generate_poker_observations(size, 'Straight')
    
    flush_hands = generate_poker_observations(size, 'Flush')
    
    full_house_hands = generate_poker_observations(size, 'Full_house')
    
    four_of_a_kind_hands = generate_poker_observations(size, 'Four_of_a_kind')
    
    all_straight_flush_hands = generate_poker_observations(TOTAL_NUMBER_OF_STRAIGHT_FLUSH_COMBINATIONS, 'Straight_flush')
    
    all_royal_flush_hands = generate_poker_observations(TOTAL_NUMBER_OF_ROYAL_FLUSH_COMBINATIONS, 'Royal_flush')
    
    hand_dfs = [nothing_hands, one_pair_hands, two_pair_hands, three_of_a_kind_hands, straight_hands, flush_hands, full_house_hands, four_of_a_kind_hands, all_straight_flush_hands, all_royal_flush_hands]
    
    df = pd.concat(hand_dfs, ignore_index=True)
    df = df.sample(frac=1).reset_index(drop=True)
    
    return df
    


# In[ ]:




