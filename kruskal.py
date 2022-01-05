# N = number_of_cities S = source D = destination
# i = node i, j = node j
import graph_util


def kruskal(source: int, destination: int, number_of_cities: int):
    graph = graph_util.graph_generator(number_of_cities=number_of_cities)


def repetition_for_report():
    repetition_values = [10, 50, 100, 200, 500, 1000, 2000]
    for repetition in repetition_values:
        print("Number of Cities: " + str(repetition))
        kruskal(source=1, destination=repetition, number_of_cities=repetition)


def main():
    pass


if __name__ == '__main__':
    main()
