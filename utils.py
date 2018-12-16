import numpy as np


def histogram_from_file(file):
    f = open(file, 'r')
    output = []
    lines = f.readlines()
    for line in lines:
        for c in line:
            output.append(c)

    unique, count = np.unique(output, return_counts=True)
    return unique, count


def get_probabilities_dict(letters, frequency):
    probability = []
    for i in range(len(frequency)):
        probability.append(frequency[i] / sum(frequency))
    dict_p = dict(zip(letters, probability))
    return dict_p
