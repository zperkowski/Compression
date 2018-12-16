import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(g):
    plt.subplot(111)
    nx.draw(g, with_labels=True, font_weight='bold')
    plt.show()


def split_dict(dict_p):
    keys = list(dict_p.keys())
    values = list(dict_p.values())
    print(keys)
    print(values)
    l = len(keys)
    splits = []
    while len(splits) < l:
        min_diff = abs(sum(values[:1]) - sum(values[1:]))
        split_after = keys[0]
        for i in range(len(keys) - 1):
            diff = abs(sum(values[:i]) - sum(values[i + 1:]))
            if diff < min_diff and keys[i] not in splits:
                min_diff = diff
                split_after = keys[i]
        splits.append(split_after)
        i = keys.index(split_after)
        keys.pop(i)
        values.pop(i)
    return splits


def generate_graph(dict_p):
    g = nx.Graph()
    g.add_nodes_from(dict_p.keys())
    splits = split_dict(dict_p)
    sub_nodes = [i for i in range(len(splits))]
    g.add_nodes_from(sub_nodes)
    return g


