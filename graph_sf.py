import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()


def draw_graph(g):
    plt.subplot(111)
    nx.draw_shell(g, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(g, 'weight')
    pos = nx.shell_layout(g)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()


def build_graph(g, node, dict_p, keys, values):
    draw_graph(g)
    print(keys)
    print(values)
    splits = []
    min_diff = abs(sum(values[:1]) - sum(values[1:]))
    split_after = keys[0]
    for i in range(len(keys) - 1):
        diff = abs(sum(values[:i]) - sum(values[i + 1:]))
        if diff < min_diff and keys[i] not in splits:
            min_diff = diff
            split_after = keys[i]
    i = keys.index(split_after)
    if len(keys) > 2:
        node_value_l = node + 1
        g.add_edge(node, node_value_l, weight=0)
        node_value_p = (node + 1) * -1
        g.add_edge(node, node_value_p, weight=1)
        build_graph(g, node_value_l, dict_p, keys[:i + 1], values[:i + 1])
        build_graph(g, node_value_p, dict_p, keys[i + 1:], values[i + 1:])
    else:
        g.add_edge(node, keys[0], weight=0)
        if len(keys) == 2:
            g.add_edge(node, keys[1], weight=1)


def generate_graph(dict_p):
    keys = list(dict_p.keys())
    values = list(dict_p.values())
    build_graph(g, 0, dict_p, keys, values)
    return g


