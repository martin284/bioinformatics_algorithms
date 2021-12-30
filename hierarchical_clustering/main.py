# import other modules in project
import distance_matrix_module
import upgma
import neighbor_joining

# import packages
import numpy as np
from copy import deepcopy
import time

# returns a list of the sequence names and a list of the sequences
# with the same order
def get_seqence_list(path) :
    fhandle = open(path)
    data = fhandle.read()
    data = data.split('>')
    data.pop(0)

    seq_list = []
    seq_names = []

    for str in data :
        # adds sequence
        seq = str.split('\n')[1] + str.split('\n')[2]
        seq_list.append(seq)
        # adds sequence name
        name = str.split('\n')[0][12] + str.split('\n')[0][13]
        if name[1] == '-' :
            name = name[0]
        seq_names.append(name)

    return seq_names, seq_list

def get_distance_matrix(seq_list, type) :
    distance_matrix = distance_matrix_module.Distance_matrix(seq_list, type)
    return distance_matrix.matrix



def main() :
    path = input('Please enter the path to your multifasta file: ')
    seq_names, seq_list = get_seqence_list(path)

    # calculates hamming distance matrix
    start = time.time()
    hamming_distance_matrix = get_distance_matrix(seq_list, 'hamming')
    end = time.time()
    print('\nHamming distance matrix:')
    print(hamming_distance_matrix)
    print('\nRuntime: ' + str(end-start))

    # calculates levenshtein distance matrix
    start = time.time()
    levenshtein_distance_matrix = get_distance_matrix(seq_list, 'levenshtein')
    end = time.time()
    print('\nLevenshtein distance matrix:')
    print(levenshtein_distance_matrix)
    print('\nRuntime: ' + str(end-start))

    # # example from lecture
    # headers = ['Bsu', 'Bst', 'Lvi', 'Amo', 'Mlu']
    # distance_matrix = np.array([
    # [0, 0.1715, 0.2147, 0.3091, 0.2326],
    # [0.1715, 0, 0.2991, 0.3399, 0.2058],
    # [0.2147, 0.2991, 0, 0.2795, 0.3943],
    # [0.3091, 0.3399, 0.2795, 0, 0.4289],
    # [0.2326, 0.2058, 0.3943, 0.4289, 0]
    # ])

    # clusters the hamming distance matrix with UPGMA
    print('\nTree made with UPGMA and hamming distance:\n')
    start = time.time()
    newick_string_upgma = upgma.create_tree(deepcopy(seq_names),
    deepcopy(hamming_distance_matrix))
    end = time.time()
    print(newick_string_upgma)
    print('\nRuntime: ' + str(end-start))

    # clusters the hamming distance matrix with Neigbor-Joining
    print('\nTree made with Neighbor-Joining and hamming distance:\n')
    start = time.time()
    newick_string_nj = neighbor_joining.create_tree(deepcopy(seq_names),
    deepcopy(hamming_distance_matrix))
    end = time.time()
    print(newick_string_nj)
    print('\nRuntime: ' + str(end-start))

    # clusters the levenshtein distance matrix with UPGMA
    print('\nTree made with UPGMA and levenshtein distance:\n')
    start = time.time()
    newick_string_upgma = upgma.create_tree(deepcopy(seq_names),
    deepcopy(levenshtein_distance_matrix))
    end = time.time()
    print(newick_string_upgma)
    print('\nRuntime: ' + str(end-start))

    # clusters the hamming distance matrix with Neigbor-Joining
    print('\nTree made with Neighbor-Joining and levenshtein distance:\n')
    start = time.time()
    newick_string_nj = neighbor_joining.create_tree(deepcopy(seq_names),
    deepcopy(levenshtein_distance_matrix))
    end = time.time()
    print(newick_string_nj)
    print('\nRuntime: ' + str(end-start))


if __name__ == '__main__' :
    main()
