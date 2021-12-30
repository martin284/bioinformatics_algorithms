import numpy as np
import result

def compute_last_occurence_function(pattern, alphabet) :
    lambda_map = {}
    for a in alphabet :
        lambda_map[a] = 0
    for j in range(0, len(pattern)) :
        lambda_map[pattern[j]] = j
    return lambda_map

def compute_prefix_function(pattern) :
    m = len(pattern)
    pi = np.zeros((m,), dtype=int)
    pi[0] = -1
    k = -1
    for q in range(1, m) :
        while k > -1 and pattern[k+1] != pattern[q] :
            k = pi[k]
        if pattern[k+1] == pattern[q] :
            k = k + 1
        pi[q] = k
    for i in range(0, m) :
        pi[i] = pi[i] + 1
    return pi

def compute_good_suffix_function(pattern) :
    m = len(pattern)
    gamma = np.zeros((m,), dtype=int)
    pi = compute_prefix_function(pattern)
    pattern_reverse = pattern[::-1]
    pi_reverse = compute_prefix_function(pattern_reverse)
    for j in range(0, m) :
        gamma[j] = m - pi[m-1]
    for l in range(0, m) :
        j = (m-1) - pi_reverse[l]
        if gamma[j] > l - pi_reverse[l] :
            gamma[j] = l - pi_reverse[l] + 1
    return gamma

def get_alphabet(string) :
    alphabet = list(set(string))
    return alphabet


def find_matches(pattern, sequence) :
    global result
    counter = 0
    match_list = []
    n = len(sequence)
    m = len(pattern)
    alphabet = get_alphabet(sequence+pattern)
    lambda_map = compute_last_occurence_function(pattern, alphabet)
    gamma = compute_good_suffix_function(pattern)
    s = 0
    while s <= n - m :
        j = m - 1
        while j >= 0 and pattern[j] == sequence[s+j] :
            counter = counter + 1
            j = j - 1
        if j == -1 :
            match_list.append(s)
            s = s + gamma[0]
        else :
            s = s + max(gamma[j], j - lambda_map[sequence[s+j]])

    # building the result object
    result = result.Result(match_list, counter)
    return result
