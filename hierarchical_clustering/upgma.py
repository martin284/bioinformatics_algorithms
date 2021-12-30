import numpy as np

def find_min_pos(distance_matrix) :
    min_distance = distance_matrix[0][1]
    row_nr = 0
    column_nr = 1
    for i in range(0, len(distance_matrix)) :
        for j in range(0, len(distance_matrix[0])) :
            if i == j :
                continue
            if min_distance > distance_matrix[i][j] :
                min_distance = distance_matrix[i][j]
                row_nr = i
                column_nr = j
    return row_nr, column_nr

def change_headers(headers, i, j) :
    header1 = headers[i]
    header2 = headers[j]
    # add new header to the smaller index and delete the larger index
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
        distance_matrix[j][y])
    # update column
    for y in range(0, len(distance_matrix)) :
        if x == y :
            continue
        distance_matrix[y][x] = 0.5 * (distance_matrix[y][i] +
        distance_matrix[y][j])

    # delete unnecessary row
    distance_matrix = np.delete(distance_matrix, max(i, j), axis=0)
    # delete unnecessary column
    distance_matrix = np.delete(distance_matrix, max(i, j), axis=1)

    return distance_matrix

def create_tree(headers, distance_matrix) :
    while len(headers) > 1 :
        i, j = find_min_pos(distance_matrix)
        headers = change_headers(headers, i, j)
        distance_matrix = update_distance_matrix(distance_matrix, i, j)
    return headers[0]
