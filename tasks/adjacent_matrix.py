"""Templates for programming assignments: Graph Adjacent Matrix."""
from typing import Any, Optional


class GraphAdjacentMatrix:
    """Default interface for Graph using adjacency matrix."""

    def __init__(self, number_of_vertices: int):
        pass

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def get_list_of_adjacent_vertices(self, vertex: list):
        """Returns for given vertex 0/1 list, where 0/1 at i-th position
        means that edge doesn't exist/exist between given vertex and i-th vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} function should return for vertex 0 the following list: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - number of vertices
        """
        pass

    def get_number_of_adjacent_vertices(self, vertex: list):
        """Returns number of adjacent vertices for the given vertex.

        NOTE: O(N) complexity is expected for this operation.
        """
        pass

    def is_edge(self, vertex1: int, vertex2: int):
        """Checks if graph has edge between 2 given vertices.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass
