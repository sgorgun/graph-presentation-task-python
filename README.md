# Graph representation (python)

Set of programming assignments that are designed to test knowledge of graph representation.

## Problem 1: Present undirected graph using adjacency matrix
Your first programming assignment is to implement the provided default interface _GraphAdjacencyMatrix_ for undirected graph. Tests will check your implementation in different scenarios. Number of vertices *N* is an input parameter, which shows that graph consists of *N* vertices from *0* to *N-1*.
Functionality that class should support:
* add edge between vertices X and Y to the graph
* get number of adjacent vertices
* get list for vertex X with information of existing edges between X and all vertices from *0* to *N-1*, e.g. V = {0,1,2,3}, E = {{0,1}, {1,2}, {0,3}}, expected output for vertex '0' is [0, 1, 0, 1].
* check whether edge between vertices X and Y exists

Please use a template for the implementation (tasks/adjacency_matrix:GraphAdjacencyMatrix).

`class GraphAdjacencyMatrix:
    """Default interface for undirected graph using adjacency matrix."""

    def __init__(self, number_of_vertices: int):
        pass

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def get_list_of_adjacent_vertices(self, vertex: int) -> list:
        """Returns for given vertex 0/1 list, where 0/1 at i-th position
        means that edge doesn't exist/exist between given vertex and i-th vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} function should return for vertex 0 the following list: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - number of vertices
        """
        pass

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns number of adjacent vertices for the given vertex.

        NOTE: O(N) complexity is expected for this operation.
        """
        pass

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks if graph has edge between 2 given vertices.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass`

## Problem 2: Present undirected graph using adjacency dictionary
Your task is to implement the provided default interface _GraphAdjacencyDictionary_ for undirected graph. Tests will check your implementation in different scenarios. Number of vertices *N* is an input parameter, which shows that graph consists of *N* vertices from *0* to *N-1*.
Functionality that class should support:
* add edge between vertices X and Y to the graph
* get number of adjacent vertices
* get list for vertex X with information of existing edges between X and all vertices from *0* to *N-1*, e.g. V = {0,1,2,3}, E = {{0,1}, {1,2}, {0,3}}, expected output for vertex '0' is [0, 1, 0, 1].
* check whether edge between vertices X and Y exists

Please use a template for the implementation (tasks/adjacency_dict:GraphAdjacencyDictionary).


`class GraphAdjacencyDictionary:
    """Default interface for undirected graph using adjacency dictionary."""

    def __init__(self, number_of_vertices: int):
        pass

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def get_list_of_adjacent_vertices(self, vertex: int) -> list:
        """Returns for given vertex 0/1 list, where 0/1 at i-th position
        means that edge doesn't exist/exist between the given vertex and the i-th vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} function should return for vertex 0 the following list: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - number of vertices
        """
        pass

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns number of adjacent vertices for the given vertex.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks if graph has an edge between 2 given vertices.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass`

