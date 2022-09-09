# Graph representation (python)

Set of programming assignments that are designed to test knowledge of graph representation.

## Problem 1: Present undirected graph using adjacency matrix
Your first programming assignment is to implement the provided default interface for GraphAdjacencyMatrix. Tests will check your implementation in different scenarios. Number of vertices *N* is an input parameter, which shows that graph consists of *N* vertices from *0* to *N-1*.
Functionality that class should support:
* add edge between vertices X and Y to the graph
* get number of adjacent vertices
* get list for vertex X with information of existing edges between X and all vertices from *0* to *N-1*, e.g. V = {0,1,2,3}, E = {{0,1}, {1,2}, {0,3}}, expected output for vertex '0' is [0, 1, 0, 1].
* check whether edge between vertices X and Y exists

## Problem 2: Present undirected graph using adjacency dictionary
Your task is to implement the provided default interface for GraphAdjacenyDictionary. Tests will check your implementation in different scenarios. Number of vertices *N* is an input parameter, which shows that graph consists of *N* vertices from *0* to *N-1*.
Functionality that class should support:
* add edge between vertices X and Y to the graph
* get number of adjacent vertices
* get list for vertex X with information of existing edges between X and all vertices from *0* to *N-1*, e.g. V = {0,1,2,3}, E = {{0,1}, {1,2}, {0,3}}, expected output for vertex '0' is [0, 1, 0, 1].
* check whether edge between vertices X and Y exists