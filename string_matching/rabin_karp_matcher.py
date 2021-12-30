import result

def map_string_to_integer(string) :
    list_int = []
    for i in range(0, len(string)) :
        list_int.append(ord(string[i]))
    return list_int

def find_matches(pattern, sequence, q) :
    global result
    counter = 0
    n = len(sequence)
    m = len(pattern)
    # calculates the size of the alphabet
    d = len(list(set(pattern+sequence)))
    p = 0
    t_s = 0
    h = (d ** (m-1)) % q

    pattern_int = map_string_to_integer(pattern)
    sequence_int = map_string_to_integer(sequence)

    # preprocessing
    for i in range(0, m) :
        p = (d * p + pattern_int[i]) % q
        t_s = (d * t_s + sequence_int[i]) % q

    # matching
    match_list = []
    for s in range(0, n-m) :
        if p == t_s :
            i = 0
            while (i < m) :
                if pattern[i] != sequence[s + i] :
                    counter = counter + i + 1
                    break
                i += 1
            if i == m :
                counter = counter + m
                match_list.append(s)
        if s < n-m :
            t_s = (d * (t_s - sequence_int[s] * h) + sequence_int[s+m]) % q

    # building the result object
    result = result.Result(match_list, counter)

    return result
