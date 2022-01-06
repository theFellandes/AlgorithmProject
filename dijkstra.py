# N = number_of_cities S = source D = destination
# i = node i, j = node j

# Min heap eksik
import graph_util
import heapq

repetition_counter = 0


def main():
    # repetition_for_report()
    N = int(input("Please enter the N value: "))
    S = int(input("Please enter the Source vertex: "))
    D = int(input("Please enter the Destination vertex: "))
    print(dijkstra(S, D, N))


def dijkstra(source: int, destination: int, number_of_cities: int):
    # This is not a part of the dijkstra algorithm, it creates the specified graph
    # then dijkstra's algorithm is applied to this newly created graph.
    vertices, weights, adj = graph_util.graph_generator_dijkstra(number_of_cities)
    global repetition_counter

    # DEMO
    # vertices = [1, 2, 3, 4, 5]
    # weights = [[0, 10, 5, float('inf'), float('inf')],
    #            [float('inf'), 0, 2, 1, float('inf')],
    #            [float('inf'), 3, 0, 9, 2],
    #            [float('inf'), float('inf'), float('inf'), 0, 4],
    #            [7, float('inf'), float('inf'), 6, 0]]
    # adj = [[2, 3], [3, 4], [2, 4, 5], [5], [1, 4]]

    d, pi = initialize_single_source(vertices, source)  # Initializes d and pi arrays. O(1) times.
    S = []  # Initialize the empty S array to put the visited vertices in. O(1) times.
    Q = vertices  # Put all the vertices in the Q array. O(1) times.
    heapq.heapify(Q)  # Creates a min-heap from the Q array. O(1) times.
    while len(Q) > 0:  # Repeats O(V) times.
        u = heapq.heappop(Q)  # Extracts the minimum from the heap to u. O(V) times.
        S.append(u)  # Visited vertices are put into the S array. O(V) times.
        for v in adj[u - 1]:  # Repeated O(E) times.
            relax(u, v, weights, d, pi)  # Relaxes the weight of vertex v. O(E) times.
            repetition_counter += 1
    path = pi[destination - 1]  # Path of source to destination is saved to the path array. O(1) times.
    path.append(destination)  # The destination itself is added to the path. O(1) times.
    total_weight = 0
    for i in range(len(path) - 1):  # Repeats PathLength times so O(E) times.
        total_weight += weights[path[i] - 1][path[i + 1] - 1]  # Weights along the path are summed up. O(E) times.
        repetition_counter += 1
    return path, total_weight


def initialize_single_source(vertices, source):
    d = []
    pi = []
    global repetition_counter
    for v in vertices:  # Repeats O(V) times.
        d.append(float('inf'))  # Initializes d array, the weights of vertices, filled with inf weights. O(V) times.
        pi.append([])  # Creates empty pi arrays to hold the path from source to a vertex, for every vertex. O(V) times.
        repetition_counter += 1
    d[source - 1] = 0  # Initializes the value of source vertex to 0. O(1) times.
    return d, pi


def relax(u, v, weights, d, pi):
    new_weight = d[u - 1] + weights[u - 1][v - 1]  # Calculates the weight between u and v. O(1) times.
    if d[v - 1] > new_weight:  # If the calculated weight is smaller than the previous v weight,
        d[v - 1] = new_weight  # weight of  v is updated. O(1) times.
        pi[v - 1] = list(pi[u - 1])  # Pi of v is updated by copying its predecessor's pi path
        pi[v - 1].append(u)          # and appending its predecessor to that path. O(1) times.


def repetition_for_report():
    repetition_values = [10, 50, 100, 200, 500, 1000, 2000]
    repetition_values = range(10, 2000, 40)
    n = []
    rep = []
    global repetition_counter
    for repetition in repetition_values:
        print("Number of Cities: " + str(repetition))
        dijkstra(source=1, destination=repetition, number_of_cities=repetition)
        print(repetition_counter)
        n.append(repetition)
        rep.append(repetition_counter)

    graph_util.plot_graph(n, rep, "N", "Repetitions", "Dijkstra's Algorithm")


if __name__ == '__main__':
    main()
