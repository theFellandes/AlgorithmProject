# N = number_of_cities S = source D = destination
# i = node i, j = node j
import graph_util


def kruskal(number_of_cities: int):
    # This is not a part of the kruskal's algorithm, it creates the specified graph
    # then kruskal's algorithm is applied to this newly created graph.
    vertices, weights = graph_util.graph_generator_kruskal(number_of_cities=number_of_cities)

    # DEMO
    # vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # weights = [[4, 1, 2], [8, 2, 3], [7, 3, 4],
    #            [9, 4, 5], [10, 5, 6], [2, 6, 7],
    #            [1, 7, 8], [7, 8, 9], [11, 2, 8],
    #            [2, 3, 9], [6, 7, 9], [4, 6, 3],
    #            [14, 4, 6]]

    A = []  # Initializing the A array that will hold the edges of the resulting MST. O(1) times.
    sets = []  # Initializing the sets array that will hold the sets created for kruskal's algorithm. O(1) times.
    for v in vertices:  # Repeats O(V) times.
        sets.append(make_set(v))  # Creates a set for every vertex, holding only that vertex. O(V) times.
    # Elements of weights array are in the shape of [Weight, u, v],
    # so this operation sorts this array by the weights and edges are thus sorted with them.
    weights.sort()  # O(1) times.
    total_weight = 0
    for i in weights:  # Repeats O(E) times.
        weight, u, v = i[0], i[1], i[2]  # Unpacks the weight, u and v from the weights array for all indices. O(E) times.
        if find_set(u, sets) != find_set(v, sets):  # If u and v are not in the same set meaning they don't form a cycle, O(E) times.
            A.append([u, v])                        # this edge is appended to the A array. O(E) times.
            total_weight += weight                  # Appended weight is added to the total_weights. O(E) times.
            union(u, v, sets)                       # The sets of these edges are unified to a single set. O(E) times.
    return A, total_weight  # Returns the resulting A array, and the total weight of the resulting MST. O(1) times.


def make_set(u):
    return [u]  # Turns the u to a list. O(1) times.


def find_set(u, sets):
    for set_index in range(len(sets)):  # Repeats O(V) times. Although not a tight upper bound.
        if u in sets[set_index]:  # If the vertex is in this specific set, O(V) times.
            return set_index  # return its index inside the sets array. O(V) times.
    return None


def union(u, v, sets):
    first_set_index = find_set(u, sets)  # Gets the index of u's set in the sets array. O(1) times.
    second_set_index = find_set(v, sets)  # Gets the index of v's set in the sets array. O(1) times.
    if first_set_index != second_set_index:  # If they are in different sets, O(1) times.
        sets[first_set_index] += sets[second_set_index]  # They are concatenated, O(1) times.
        sets[first_set_index].sort()  # and the resulting set is sorted. O(1) times.
        del sets[second_set_index]  # Lastly the second set is deleted. O(1) times.


def repetition_for_report():
    repetition_values = [10, 50, 100, 200, 500, 1000, 2000]
    for repetition in repetition_values:
        print("Number of Cities: " + str(repetition))
        kruskal(number_of_cities=repetition)


def main():
    print(kruskal(10))
    # arr = [[4, 5, 6], [1, 2, 3]]
    # union(1, 4, arr)
    # print(arr)


if __name__ == '__main__':
    main()
