import numpy as np

class Distance_matrix :
    def __init__(self, seq_list, type) :
        self.matrix = self.get_distance_matrix(seq_list, type)

    def calculate_hamming_distance(self, seq1, seq2) :
        hamming_distance = 0
        for i in range(0, min(len(seq1), len(seq2))) :
            if seq1[i] != seq2[i] :
                hamming_distance = hamming_distance + 1

        return hamming_distance

    def calculate_levenshtein_distance(self, seq1, seq2) :
        m = len(seq1)
        n = len(seq2)
        D = np.zeros((m+1, n+1))

        for i in range(1, m+1) :
            D[i][0] = i

        for j in range(1, n+1) :
            D[0][j] = j

        for j in range(1, n+1) :
            for i in range(1, m+1) :
                if seq1[i-1] == seq2[j-1] :
                    substitution_cost = 0
                else :
                    substitution_cost = 1
                D[i][j] = min(D[i-1][j] + 1, D[i, j-1] + 1, D[i-1][j-1] +
                substitution_cost)

        return D[m][n]


    def get_distance_matrix(self, seq_list, type) :
        length = len(seq_list)
        distance_matrix = np.zeros((length, length))
        if type == 'hamming' :
            for i in range(0, length) :
                for j in range(0, length) :
                    distance_matrix[i, j] = self.calculate_hamming_distance(
                    seq_list[i], seq_list[j])
        elif type == 'levenshtein' :
            for i in range(0, length) :
                for j in range(0, length) :
                    distance_matrix[i, j] = self.calculate_levenshtein_distance(
                    seq_list[i], seq_list[j])
        else :
            print('Error in get_distance_matrix()')
            quit()
        return distance_matrix

    def set_distance(self, row, column, value) :
        self.matrix[row][column] = value

    def get_distance(self, row, column) :
        return self.matrix[row, column]

    def get_maximal_distance() :
        maximal_distance = self.matrix[0][0]
        for i in range(0, len(matrix)) :
            for j in range(0, len(matrix[0])) :
                if maximal_distance < self.matrix[i][j] :
                    maximal_distance = self.matrix[i][j]
