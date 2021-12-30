import random

def generate_states_and_emissions(length, P) :
    # initializes sequence array
    seq = [0] * length
    
    # generates sequence
    generate_init_state(seq)
    generate_states(seq, P)

    return seq

def generate_init_state(seq) :
    random_nr = random.uniform(0, 1)
    if random_nr < 1/8 :
        seq[0] = 0
    elif random_nr < 2/8 :
        seq[0] = 1
    elif random_nr < 3/8 :
        seq[0] = 2
    elif random_nr < 4/8 :
        seq[0] = 3
    elif random_nr < 5/8 :
        seq[0] = 4
    elif random_nr < 6/8 :
        seq[0] = 5
    elif random_nr < 7/8 :
        seq[0] = 6
    else :
        seq[0] = 7

def generate_states(seq, P) :
    for i in range(1, len(seq)) :
        prev_state = seq[i-1]
        random_nr = random.uniform(0, 1)
        threshold = P[prev_state][0]
        if random_nr < threshold :
            seq[i] = 0
            continue

        threshold = threshold + P[prev_state][1]
        if random_nr < threshold :
            seq[i] = 1
            continue

        threshold = threshold + P[prev_state][2]
        if random_nr < threshold :
            seq[i] = 2
            continue

        threshold = threshold + P[prev_state][3]
        if random_nr < threshold :
            seq[i] = 3
            continue

        threshold = threshold + P[prev_state][4]
        if random_nr < threshold :
            seq[i] = 4
            continue

        threshold = threshold + P[prev_state][5]
        if random_nr < threshold :
            seq[i] = 5
            continue

        threshold = threshold + P[prev_state][6]
        if random_nr < threshold :
            seq[i] = 6
            continue

        seq[i] = 7

def calculate_emission_seq(seq) :
    emmission_seq = []
    for i in range(0, len(seq)) :
        if seq[i] == 0 or seq[i] == 4 :
            emmission_seq.append('A')
        elif seq[i] == 1 or seq[i] == 5 :
            emmission_seq.append('C')
        elif seq[i] == 2 or seq[i] == 6 :
            emmission_seq.append('G')
        else :
            emmission_seq.append('T')
    return emmission_seq

def calculate_hidden_states(seq) :
    hidden_states = []
    for i in range(0, len(seq)) :
        if seq[i] < 4 :
            hidden_states.append('+')
        else :
            hidden_states.append('-')
    return hidden_states
