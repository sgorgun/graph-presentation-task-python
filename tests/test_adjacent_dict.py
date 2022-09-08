"""Tests for 'tasks.adjacent_list_using_dict' module."""
import random
import pytest

from tasks.adjacent_dict import GraphAdjacentDictionary


@pytest.mark.timeout(2)
def test_adjacency_list_sample():
    """Tests for adjacency dictionary class."""
    num_of_vertices = 5
    graph = GraphAdjacentDictionary(num_of_vertices)

    with pytest.raises(ValueError):
        _ = graph.is_edge(2,7)

    assert graph.get_number_of_adjacent_vertices(0) == 0

    for vertex in range(4):
        graph.add_new_edge(vertex, vertex+1)

    assert graph.get_number_of_adjacent_vertices(0) == 1
    assert graph.get_number_of_adjacent_vertices(1) == 2
    with pytest.raises(ValueError):
        _ = graph.get_number_of_adjacent_vertices(5) == 1

    for vertex in range(4):
        assert graph.is_edge(vertex, vertex+1) == True

    # Pop when stack is empty.
    assert graph.is_edge(0, 4) == False
