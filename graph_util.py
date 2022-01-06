import matplotlib.pyplot as plt


def graph_generator_dijkstra(number_of_cities: int):
    vertices = [*range(1, number_of_cities + 1)]
    weights = []
    adj = []
    for i in vertices:
        row = []
        current_neighbors = []
        for j in vertices:
            if abs(i - j) <= 3 and i != j:
                row.append(i+j)
                current_neighbors.append(j)
            else:
                row.append(float('inf'))
        weights.append(row)
        adj.append(current_neighbors)

    return vertices, weights, adj


def graph_generator_kruskal(number_of_cities: int):
    vertices = [*range(1, number_of_cities + 1)]
    weights = []
    for i in vertices:
        for j in vertices:
            if abs(i - j) <= 3 and i != j:
                weights.append([i + j, i, j])

    return vertices, weights


def plot_graph(x, y, x_label, y_label, title):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(title)
    plt.show()
