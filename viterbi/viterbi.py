import numpy as np
from decimal import *

# class wich saves the probability of the path to the corresponding column
# and a pointer for the backtracking
class Entry :
    def __init__(self, probability, prev_state) :
        self.probability = probability
        self.prev_state = prev_state

def initialize_first_column(viterbi_matrix, emission) :
    # at the beginning the probability distribution is uniform
    if emission == 'A' :
        viterbi_matrix[0][0] = Entry(Decimal(0.125), None)
        viterbi_matrix[4][0] = Entry(Decimal(0.125), None)
    elif emission == 'C' :
        viterbi_matrix[1][0] = Entry(Decimal(0.125), None)
        viterbi_matrix[5][0] = Entry(Decimal(0.125), None)
    elif emission == 'G' :
        viterbi_matrix[2][0] = Entry(Decimal(0.125), None)
        viterbi_matrix[6][0] = Entry(Decimal(0.125), None)
    else :
        viterbi_matrix[3][0] = Entry(Decimal(0.125), None)
        viterbi_matrix[7][0] = Entry(Decimal(0.125), None)

def calculate_viterbi_matrix(emmission_seq, transition_matrix) :
    # state coding
    # 0 = A+. 1 = C+, 2 = G+, 3 = T+, 4 = A-, 5 = C-, 6 = G-, 7 = T-
    state_to_code_dict = {'A' : [0, 4], 'C' : [1, 5], 'G' : [2, 6],
    'T' : [3, 7]}

    # initializes matrix which saves all probabilities including pointers
    viterbi_matrix = np.full((8, len(emmission_seq)), None)

    # initializes first column
    initialize_first_column(viterbi_matrix, emmission_seq[0])

    # calculates all following columns
    for i in range(1, len(emmission_seq)) :
        # gives the states which are possible as previous state (A+, A-, ...)
        possible_previous_states = []
        for j in range(0, 8) :
            if viterbi_matrix[j][i-1] != None :
                possible_previous_states.append(j)

        # calculates probability that state is (A/C/G/T)+
        entry = viterbi_matrix[possible_previous_states[0]][i-1]
        plus_state = state_to_code_dict[emmission_seq[i]][0]
        prob1 = Decimal(entry.probability *
        Decimal(transition_matrix[possible_previous_states[0]][plus_state]))
        entry = viterbi_matrix[possible_previous_states[1]][i-1]
        prob2 = Decimal(entry.probability *
        Decimal(transition_matrix[possible_previous_states[1]][plus_state]))

        # chooses maximal probability of both and saves the corresponding state
        if prob1 >= prob2 :
            max_probability = prob1
            calculated_previous_state = possible_previous_states[0]
        else :
            max_probability = prob2
            calculated_previous_state = possible_previous_states[1]

        # saves new entry in viterbi matrix
        viterbi_matrix[plus_state][i] = Entry(max_probability,
        calculated_previous_state)

        # calculates probability that state is (A/C/G/T)-
        entry = viterbi_matrix[possible_previous_states[0]][i-1]
        minus_state = state_to_code_dict[emmission_seq[i]][1]
        prob1 = Decimal(entry.probability *
        Decimal(transition_matrix[possible_previous_states[0]][minus_state]))
        entry = viterbi_matrix[possible_previous_states[1]][i-1]
        prob2 = Decimal(entry.probability *
        Decimal(transition_matrix[possible_previous_states[1]][minus_state]))
        # chooses maximal probability of both and saves the corresponding state
        if prob1 >= prob2 :
            max_probability = prob1
            calculated_previous_state = possible_previous_states[0]
        else :
            max_probability = prob2
            calculated_previous_state = possible_previous_states[1]
        # saves new entry in viterbi matrix
        viterbi_matrix[minus_state][i] = Entry(max_probability,
        calculated_previous_state)

    return viterbi_matrix

def calculate_viterbi_path(emmission_seq, transition_matrix) :
    viterbi_matrix = calculate_viterbi_matrix(emmission_seq, transition_matrix)

    # transform and print viterbi_matrix
    transformed_matrix = np.full((8, len(emmission_seq)), None)
    for i in range(0, 8) :
        for j in range(len(viterbi_matrix[0])) :
            if viterbi_matrix[i][j] != None :
                transformed_matrix[i][j] = viterbi_matrix[i][j].probability

    # finds state with maximal probability in the last column
    last_col = len(viterbi_matrix[0]) - 1 # index of the last column
    last_state = None
    max_probability = 0
    for i in range(0, 8) :
        if viterbi_matrix[i][last_col] != None :
            entry = viterbi_matrix[i][last_col]
            if entry.probability > max_probability :
                max_probability = entry.probability
                last_state = i

    # starts backtracking with calculated (init) state

    # initializes viterbi path
    viterbi_path = [-1] * len(emmission_seq)

    # adds last state to viterbi path
    viterbi_path[last_col] = last_state

    # calculates the other states of viterbi path
    current_state = last_state
    for i in range(last_col, 0, -1) :
        entry = viterbi_matrix[current_state][i]
        viterbi_path[i-1] = entry.prev_state
        current_state = entry.prev_state

    # transform viterbi path from number code to +- model
    for i in range(0, len(emmission_seq)) :
        if viterbi_path[i] < 4 :
            viterbi_path[i] = '+'
        else :
            viterbi_path[i] = '-'

    return viterbi_path
