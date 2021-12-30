import result

def find_matches(pattern, sequence) :
    global result
    counter = 0
    # preprocessing
    n = len(sequence)
    m = len(pattern)
    # array with results
    match_list = []
    # for every shift
    for s in range(0, n-m+1) :
        i = 0
        while (i < m) :
            if pattern[i] != sequence[s + i] :
                counter = counter + i + 1
                break
            i += 1
        if i == m :
            counter = counter + m
            match_list.append(s)
    # build a result object
    result = result.Result(match_list, counter)

    return result
