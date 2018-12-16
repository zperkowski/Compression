import os

from graph_sf import generate_graph, draw_graph
from utils import histogram_from_file, get_probabilities_dict

if __name__ == '__main__':
    path_to_text = os.path.join("data", "text.txt")
    try:
        os.path.isfile(path_to_text)
    except FileNotFoundError:
        print("You need to add text.txt file to data directory")
        exit(1)
    letters, frequency = histogram_from_file(path_to_text)
    print("letters\t" + str(letters))
    print("frequency\t" + str(frequency))
    dict_p = get_probabilities_dict(letters, frequency)
    print("dict_p\t" + str(dict_p))
    graph = generate_graph(dict_p)
    draw_graph(graph)
