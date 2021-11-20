from flask import Flask, render_template, request
from joblib import load
import numpy as np
import sklearn

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'ostentacja'


def make_prediction(suits, ranks):
    model = load('./model/good_model_backup')
    x = []

    for s, c in zip(suits, ranks):
        x.extend([s, c])

    unique_cards = [(s, c) for s, c in zip(suits, ranks)]
    if len(unique_cards) != len(set(unique_cards)):
        result = 'At least 2 cards you provided are the same. Try again!'
        return result

    x = np.array(x).reshape(1, -1)
    prediction = int(model.predict(x))

    figures = {0: 'Nothing',
               1: 'One pair',
               2: 'Two pairs',
               3: 'Three of a kind',
               4: 'Straight',
               5: 'Flush',
               6: 'Full house',
               7: 'Four of a kind',
               8: 'Straight Flush',
               9: 'Royal Flush'}

    result = f'Your cards are {figures[prediction]}'

    return result


SUITS_CARD_LIST_UNCHOSEN = [
['1', 'Hearts', '0'],
['2', 'Spades', '0'],
['3', 'Diamonds', '0'],
['4', 'Clubs', '0']
]


RANKS_CARD_LIST_UNCHOSEN = [
['1', 'A', '0'],
['2', '2', '0'],
['3', '3', '0'],
['4', '4', '0'],
['5', '5', '0'],
['6', '6', '0'],
['7', '7', '0'],
['8', '8', '0'],
['9', '9', '0'],
['10', '10', '0'],
['11', 'J', '0'],
['12', 'Q', '0'],
['13', 'K', '0']
]


def mark_choice(pattern, choice):
    choice = str(choice)
    marked_list = [field.copy() for field in pattern]

    for field in marked_list:
        if field[0] == choice:
            field[-1] = '1'

    return marked_list


def make_card_lists(values, kind):
    pattern = globals()[f'{kind.upper()}_CARD_LIST_UNCHOSEN']

    globals()[f'{kind}_card_lists'] = []

    for i, value in enumerate(values):
        globals()[f'{kind}_card_list_{i + 1}'] = mark_choice(pattern, value)
        globals()[f'{kind}_card_lists'].append(globals()[f'{kind}_card_list_{i + 1}'])

    return globals()[f'{kind}_card_lists']


def make_selected_card_selectors(suits_lists, ranks_lists):
    idxs = [str(i) for i in range(1, 6)]
    selected_card_selectors = [[i, s, r] for i, s, r in zip(idxs, suits_lists, ranks_lists)]

    return selected_card_selectors


@app.route('/')
def home():
    DEFAULT_VALUE = 1

    suits = [DEFAULT_VALUE for x in range(5)]
    ranks = [DEFAULT_VALUE for x in range(5)]

    suits_card_lists = make_card_lists(suits, 'suits')
    ranks_card_lists = make_card_lists(ranks, 'ranks')
    card_selectors = make_selected_card_selectors(suits_card_lists, ranks_card_lists)

    return render_template('home.html', card_selectors=card_selectors)


@app.route('/predictfigure', methods=['GET', 'POST'])
def predictfigure():
    if request.method == 'POST':
        suits = []
        ranks = []
        ids = [id for id in range(1, 6)]

        for x in range(0, 5):
            globals()[f'S{x + 1}'] = int(request.form[f'S{x + 1}'])
            suits.append(globals()[f'S{x + 1}'])

            globals()[f'C{x + 1}'] = int(request.form[f'C{x + 1}'])
            ranks.append(globals()[f'C{x + 1}'])

        suits_card_lists = make_card_lists(suits, 'suits')
        ranks_card_lists = make_card_lists(ranks, 'ranks')
        card_selectors = make_selected_card_selectors(suits_card_lists, ranks_card_lists)

        cards = zip(ids, suits, ranks)

        prediction = make_prediction(suits, ranks)

        return render_template('predictfigure.html', prediction=prediction, cards=cards, card_selectors=card_selectors)
    elif request.method == 'GET':
        return 'This is a GET method'
    else:
        return 'Something went very wrong!'
