# Graph representation

## Purpose

The coding exercises are designed to test knowledge of the following concepts:

* Representation of graph in memory
* Adjacency matrix as a data structure for representing graphs in memory
* Adjacency dictionary as a data structure for representing graphs in memory

## Overview

The coding exercises cover the following practical problems:
* Implementing `Adjacency matrix` interface for undirected graphs
* Implementing `Adjacency dictionary` interface for undirected graphs

## Coding exercises

### Exercise 1: Adjacency matrix interface for undirected graphs

Your task is to implement the following interface for `Adjacency matrix` data structure for representing undirected graphs in memory:

```python
class GraphAdjacencyMatrix:
    """Default interface for supporting undirected graphs using adjacency matrix."""

    def __init__(self, number_of_vertices: int):
        pass

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds a new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def get_list_of_adjacent_vertices(self, vertex: int) -> List[int]:
        """Returns a 0/1 list for a given vertex that indicates vertices adjacent to it.

        Positions of 1-s in the result list correspond to vertices that are adjacent to a given vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} the following list should be returned for the vertex 0: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns the number of adjacent vertices for a given vertex.

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks whether there is an edge in the graph between 2 given vertices.

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass
```

As you can see there are multiple details that might need some clarification:
* The class constructor expects a number `number_of_vertices`, which defines the number of vertices in the graph. You may assume that vertices are enumerated from *0* to *number_of_vertices - 1*.
* `add_new_edge` method support addition of new edges to the graph
* `get_number_of_adjacent_vertices` and `get_list_of_adjacent_vertices` methods are about getting some info regarding adjacent vertices for some vertex of interest.
* `is_edge` method simply checks whether some edges of interest is present within the graph

Please check the unit tests to get some understanding on how to use the class *in the field*.

<br>

Please use a template for the implementation (tasks/adjacency_matrix:GraphAdjacencyMatrix).


### Exercise 2: Adjacency dictionary interface for undirected graphs
Your task is to implement the following interface for `Adjacency matrix` data structure for representing undirected graphs in memory:

```python
class GraphAdjacencyDictionary:
    """Default interface for supporting undirected graphs using adjacency dictionary."""

    def __init__(self, number_of_vertices: int):
        pass

    def add_new_edge(self, vertex1: int, vertex2: int):
        """Adds a new edge to the graph.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def get_list_of_adjacent_vertices(self, vertex: int) -> List[int]:
        """Returns a 0/1 list for a given vertex that indicates vertices adjacent to it.

        Positions of 1-s in the result list correspond to vertices that are adjacent to a given vertex.
        E.g. V = {0,1,2), E = {{0,1}, {1,2}} the following list should be returned for the vertex 0: [0, 1, 0].

        NOTE: O(N) complexity is expected for this operation, where N - the number of vertices in the graph.
        """
        pass

    def get_number_of_adjacent_vertices(self, vertex: int) -> int:
        """Returns the number of adjacent vertices for a given vertex.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass

    def is_edge(self, vertex1: int, vertex2: int) -> bool:
        """Checks whether there is an edge in the graph between 2 given vertices.

        NOTE: O(1) complexity is expected for this operation.
        """
        pass
```

As you can see the provided interface is identical to the `GraphAdjacencyMatrix`, but please note that the time complexity requirements differ for `get_number_of_adjacent_vertices` and `is_edge` method (due to the different underlying data structures that should be used for implementing the interfaces).

Please check the unit tests to get some understanding on how to use the class *in the field*.

<br>

Please use a template for the implementation (tasks/adjacency_dict:GraphAdjacencyDictionary).
