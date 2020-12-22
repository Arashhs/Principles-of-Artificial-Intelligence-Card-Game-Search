import re

rows_num = None
colors_num = None
cards_num = None

class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return self.number + self.color


class State:
    def __init__(self, rows, parent, action):
        self.rows = rows
        self.parent = parent
        self.action = action

    def __str__(self):
        string = ""
        for i in range(len(self.rows)):
            string += str(i+1) + ":  "
            for j in range(len(self.rows[i])):
                string += self.rows[i][j].__str__() + " "
            if len(self.rows[i]) == 0:
                string += '#'
            string = string + "\n" if i != len(self.rows) - 1 else string
        return string



def init_game(file_name):
    global rows_num, colors_num, cards_num
    rows = []
    row_cards = []
    with open(file_name, 'r') as reader:
        # read first line
        rows_num, colors_num, cards_num = [int(x) for x in next(reader).split()]
        rows = [None] * rows_num
        row_cards = [None] * rows_num

        # reading each rows
        for i in range(rows_num):
            rows[i] = [x for x in next(reader).split()]

        # converting each element to our Card data structure        
        for i in range(len(rows)):
            row_cards[i] = []
            for elem in rows[i]:
                match = re.match(r"([0-9]+)([a-z]+)", elem, re.I)
                if match:
                    elem_items = match.groups()
                    card = Card(elem_items[0], elem_items[1])
                    row_cards[i].append(card)

        # building the initial state
        init_state = State(row_cards, None, None)
    return init_state

        

