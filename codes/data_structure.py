import re
import copy

rows_num = None
colors_num = None
cards_num = None

class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return str(self.number) + self.color

    def __eq__(self, other):
        if self.number == other.number and self.color == other.color:
            return True
        return False

    def __repr__(self):
        return str(self)


class State:
    def __init__(self, rows):
        self.rows = rows


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

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return str(self)


class Node:
    def __init__(self, state, parent, action, par_action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.par_action = par_action # the action that parent has done to generate this child
        self.cost = cost


class Action:
    def __init__(self, first_row, second_row): # move the front card from first row to second row
        self.first_row = first_row
        self.second_row = second_row

    def __str__(self):
        return 'action: ' + str(self.first_row + 1) + ' to ' + str(self.second_row + 1)

    def __repr__(self):
        return str(self)



def get_all_actions(node):
    actions = []
    state = node.state
    row = state.rows
    for i in range(len(row)):
        if row[i] != []:
            for j in range(len(row)):
                if (row[j] == []) or (i != j and row[i][-1].number < row[j][-1].number):
                    action = Action(i, j)
                    actions.append(action)
    return actions



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
        init_state = State(row_cards)
    return init_state


def goal_test(state):
    rows = state.rows
    colors_available = 0
    for i in range(len(rows)):
        if len(rows[i]) != 0 and len(rows[i]) != cards_num:
            return False
        elif len(rows[i]) == cards_num:
            colors_available += 1
        for j in range(len(rows[i])-1):
            if rows[i][j].number <= rows[i][j+1].number or rows[i][j].color != rows[i][j+1].color:
                return False
    if colors_available != colors_num:
        return False
    return True

def get_solution(node):
    solution = []
    child = node
    parent = node.parent
    solution.insert(0, child)
    while parent is not None:
        child = parent
        parent.action = child.par_acion
        parent = parent.parent
        solution.insert(0, child)
    return solution

        

