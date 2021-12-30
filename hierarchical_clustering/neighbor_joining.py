import numpy as np

def get_n_matrix(distance_matrix, seq_nr) :
    length = len(distance_matrix)
    # calculates rs
    r_array = np.zeros(length)
    for i in range(0, length) :
        r = 1/(seq_nr-2) * np.sum(distance_matrix[i])
        r_array[i] = r

    # calculates n_matrix
    n_matrix = np.zeros((length, length))
    for i in range(0, length) :
        for j in range(0, length) :
            if i == j :
                continue
            n = distance_matrix[i][j] - r_array[i] - r_array[j]
            n_matrix[i][j] = n

    return n_matrix

def find_min_pos(n_matrix) :
    min_distance = n_matrix[0][1]
    row_nr = 0
    column_nr = 1
    for i in range(0, len(n_matrix)) :
        for j in range(0, len(n_matrix[0])) :
            if i == j :
                continue
            if min_distance > n_matrix[i][j] :
                min_distance = n_matrix[i][j]
                row_nr = i
                column_nr = j
    return row_nr, column_nr

def change_headers(headers, i, j) :
    header1 = headers[i]
    header2 = headers[j]
    headers[min(i, j)] = '(' + header1 + ',' + header2 + ')'
    headers.pop(max(i, j))
    return headers

def update_distance_matrix(distance_matrix, i, j) :
    x = min(i, j)
    # update row
    for y in range(0, len(distance_matrix)) :
        if x == y :
            continue
        distance_matrix[x][y] = 0.5 * (distance_matrix[i][y] +
        distance_matrix[j][y] - distance_matrix[i][j])
    # update column
    for y in range(0, len(distance_matrix)) :
        if x == y :
            continue
        distance_matrix[y][x] = 0.5 * (distance_matrix[y][i] +
        distance_matrix[y][j] - distance_matrix[i][j])

    # delete unnecessary row
    distance_matrix = np.delete(distance_matrix, max(i, j), axis=0)
    # delete unnecessary column
    distance_matrix = np.delete(distance_matrix, max(i, j), axis=1)

    return distance_matrix

def create_tree(headers, distance_matrix) :
    seq_nr = len(headers)
    while len(headers) > 1 :
        n_matrix = get_n_matrix(distance_matrix, seq_nr)
        row_nr, column_nr = find_min_pos(n_matrix)
        change_headers(headers, row_nr, column_nr)
        distance_matrix = update_distance_matrix(distance_matrix, row_nr,
        column_nr)
    return headers[0]
