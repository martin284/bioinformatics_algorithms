import naive_string_matcher
import rabin_karp_matcher
import kmp_matcher
import boyer_moore_matcher
import time

def read_file(path) :
    file = open(path, "r")
    data = file.read()
    data = data.split('\n')
    data.pop(0)
    data.pop(len(data)-1)
    sequence = ''
    for i in range(0, len(data)) :
        sequence = sequence + data[i]
    return sequence

# defining pattern and sequence
print('Welcome to this string matcher program.')
string_or_fasta_pattern = input('Do you want to type in a pattern string \
directly or give me a path to a fasta file for the pattern? (string/fasta) ')
if string_or_fasta_pattern == 'string' :
    pattern = input('Please type in the pattern string: ')
elif string_or_fasta_pattern == 'fasta' :
    path = input('Please type in the path to the fasta file: ')
    pattern = read_file(path)
else :
    print('Error! Try again.')
    quit()

path = input('Please enter the path of the sequence (fasta format): ')
sequence = read_file(path)

# choosing algorithm
algorithm = input('Please enter the algorithm which you want to use. \
(naive_string/rabin_karp/kmp/boyer_moore): ')
if algorithm != 'naive_string' and algorithm != 'rabin_karp' and \
algorithm != 'kmp' and algorithm != 'boyer_moore' :
    print('Error! Try again.')
    quit()

# runtime
start = time.time()
if algorithm == 'naive_string' :
    result = naive_string_matcher.find_matches(pattern, sequence)
elif algorithm == 'rabin_karp' :
    result = rabin_karp_matcher.find_matches(pattern, sequence, 11)
elif algorithm == 'kmp' :
    result = kmp_matcher.find_matches(pattern, sequence)
elif algorithm == 'boyer_moore' :
    result = boyer_moore_matcher.find_matches(pattern, sequence)
end = time.time()
runtime = end - start

# printing matches
if not result.match_list :
    print('Sorry, there is no match for your pattern :(')
elif len(result.match_list) == 1:
    print('There is one match for the following index: ', result.match_list)
else :
    print('There are', len(result.match_list),
    'matches for the following indices: ', result.match_list)

# printing runtime
print('The runtime of the algorithm was', runtime, 'seconds.')
# printing search steps
string1 = 'There have been'
string2 = 'char comparisons between the pattern and the sequence.'
print(string1, result.search_steps, string2)
