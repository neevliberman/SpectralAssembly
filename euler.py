def find_cycle_in_eulerian_graph(g, start_vertex):
    """Finds an arbitrary cycle starting at a given vertex in a directed graph.
    Assumes that the graph is Eulerian, and thus that such a cycle exists."
    
    Args:
        g: a DirectedGraph object
        start_vertex: the index of the vertex from which the cycle should start
    Returns:
        A cycle represented by a list of indices of the vertices traversed, in order, by the cycle.  
        The first and last entries of the list will be identical and equal to start_vertex.
    """
    cycle = []
    curr_vertex = None
    
    
    while curr_vertex != start_vertex:
        if curr_vertex is None:
            curr_vertex = start_vertex
            cycle.append(curr_vertex)
        
        for edge in g.out_edges(curr_vertex):
            curr_vertex = edge[1]
            cycle.append(curr_vertex)
            g.remove_edge(*edge)
            break

    return cycle
        
        
def is_eulerian(g):
    """Checks if a directed graph is Eulerian. Assumes that g is connected.
    
    Args:
        g: a DirectedGraph object
    Returns:
        True if g is Eulerian, False otherwise.
    """
    for vertex in range(g.num_vertices()):
        if g.indegree(vertex) != g.outdegree(vertex):
            return False
    return True

