def get_base_count_from_sequence(sequence):
    '''Get count of nucleotide bases from DNA/RNA sequence'''
    base_count_dict = dict()
    for base in sequence:
        if base not in base_count_dict:
            base_count_dict[base] = 1
        else:
            base_count_dict[base] += 1
    return base_count_dict

def print_base_freq_from_count(base_count_dict):
    '''Print the frequence of nucleotide bases from the count'''
    print('freqs')
    total = float(sum([base_count_dict[base] for base in base_count_dict.keys()]))
    for base in base_count_dict.keys():
        print(base + ':' + str(base_count_dict[base]/total))
sequence = 'ATCTGACGCGCGCCGC'
#new branch
base_count_dict = get_base_count_from_sequence(sequence)
print_base_freq_from_count(base_count_dict)