import numpy as np
import result

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
    return pi

def find_matches(pattern, sequence) :
    global result
    counter = 0
    match_list = []
    n = len(sequence)
    m = len(pattern)
    q = -1
    pi = compute_prefix_function(pattern)
    for i in range(0, n) :
        while q > -1 and pattern[q+1] != sequence[i] :
            counter = counter + 1
            q = pi[q]
        counter = counter + 1
        if pattern[q+1] == sequence[i] :
            q = q + 1
        if q == m-1 :
            match_list.append(i-(m-1))
            q = pi[q]

    # building the result object
    result = result.Result(match_list, counter)
    return result
