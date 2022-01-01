import numpy as np
def node_generator(number_of_cities: int):
    graph = []
    for i in range(0, number_of_cities):
        row = []
        for j in range(0, number_of_cities):
            if abs(i - j) <= 3 and i != j:
                row.append(i+j)
                graph.append(row)
    return graph
