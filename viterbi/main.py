import sequence_generation as sg
import viterbi

def calculate_error_rate(hidden_states, viterbi_path) :
    error_number = 0
    for i in range(0, len(hidden_states)) :
        if hidden_states[i] != viterbi_path[i] :
            error_number = error_number + 1
    return error_number / len(hidden_states)

def main() :
    n = 1000

    # stochastic matrix
    P = [
    [0.144, 0.219, 0.341, 0.096, 0.050, 0.050, 0.050, 0.050],
    [0.137, 0.294, 0.219, 0.150, 0.050, 0.050, 0.050, 0.050],
    [0.129, 0.271, 0.300, 0.100, 0.050, 0.050, 0.050, 0.050],
    [0.063, 0.284, 0.307, 0.146, 0.050, 0.050, 0.050, 0.050],
    [0.025, 0.025, 0.025, 0.025, 0.270, 0.184, 0.256, 0.189],
    [0.025, 0.025, 0.025, 0.025, 0.290, 0.268, 0.070, 0.272],
    [0.025, 0.025, 0.025, 0.025, 0.223, 0.221, 0.268, 0.187],
    [0.025, 0.025, 0.025, 0.025, 0.159, 0.215, 0.263, 0.263]]

    # stochastic matrix for wrong viterbi algorithm
    P_wrong = [
    [0.025, 0.025, 0.025, 0.025, 0.270, 0.184, 0.256, 0.189],
    [0.025, 0.025, 0.025, 0.025, 0.290, 0.268, 0.070, 0.272],
    [0.025, 0.025, 0.025, 0.025, 0.223, 0.221, 0.268, 0.187],
    [0.025, 0.025, 0.025, 0.025, 0.159, 0.215, 0.263, 0.263],
    [0.144, 0.219, 0.341, 0.096, 0.050, 0.050, 0.050, 0.050],
    [0.137, 0.294, 0.219, 0.150, 0.050, 0.050, 0.050, 0.050],
    [0.129, 0.271, 0.300, 0.100, 0.050, 0.050, 0.050, 0.050],
    [0.063, 0.284, 0.307, 0.146, 0.050, 0.050, 0.050, 0.050]]

    # state coding
    # 0 = A+. 1 = C+, 2 = G+, 3 = T+, 4 = A-, 5 = C-, 6 = G-, 7 = T-

    # generates emissions and hidden hidden states
    seq = sg.generate_states_and_emissions(n, P)

    # print('Code sequence:', seq)

    # calculates emission sequence from the code sequence
    emmission_seq = sg.calculate_emission_seq(seq)
    print('Emission sequence:', emmission_seq)

    # calculates sequence von hidden states
    hidden_states = sg.calculate_hidden_states(seq)
    print('Hidden states:', hidden_states)

    # calculates viterbi path
    viterbi_path = viterbi.calculate_viterbi_path(emmission_seq, P)
    print('Viterbi path:', viterbi_path)

    # calculates error rate
    error_rate = calculate_error_rate(hidden_states, viterbi_path)
    print('Error rate:', error_rate)

    # calculates viterbi path with wrong stochastic matrix
    wrong_viterbi_path = viterbi.calculate_viterbi_path(emmission_seq, P_wrong)
    print('Viterbi path with wrong stochastic matrix:', wrong_viterbi_path)

    # calculates error rate
    wrong_error_rate = calculate_error_rate(hidden_states, wrong_viterbi_path)
    print('Error rate:', wrong_error_rate)

if __name__ == "__main__" :
    main()
