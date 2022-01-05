def graph_generator(number_of_cities: int):
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
