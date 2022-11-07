class DirectedGraph:
    """Abstract base class for a directed graph.

    A functional directed graph class can be obtained by inheriting from 
    this class and overriding the methods has_edge, add_edge, and remove_edge.
    All other methods have default implementations.
    """
    def __init__(self, num_vertices):
        """Constructs a directed graph with num_vertices vertices and zero edges"""
        self._num_vertices = num_vertices
    
    def has_edge(self, i, j):
        """Returns True if the graph contains the directed edge (i, j), False otherwise."""
        raise NotImplementedError
        
    def add_edge(self, i, j):
        """Adds the directed edge (i, j) to the graph."""
        raise NotImplementedError
        
    def remove_edge(self, i, j):
        """Removes the directed edge (i, j) from the graph."""
        raise NotImplementedError
        
    def out_edges(self, i):
        """Returns a list of directed edges outgoing from vertex i."""
        return [(i, j) for j in range(self._num_vertices) if self.has_edge(i, j)]
    
    def in_edges(self, j):
        """Returns a list of directed edges incoming to vertex j."""
        return [(i, j) for i in range(self._num_vertices) if self.has_edge(i, j)]
    
    def outdegree(self, i):
        """Returns the outdegree of vertex i."""
        return len(self.out_edges(i))
    
    def indegree(self, i):
        """Returns the indegree of vertex i."""
        return len(self.in_edges(i))
    
    def degree(self, i):
        """Returns the degree of vertex i."""
        return self.indegree(i) + self.outdegree(i)
        
    def add_edges(self, edges):
        """Adds all edges from a list to the graph."""
        for i, j in edges:
            self.add_edge(i, j)
            
    def remove_edges(self, edges):
        """Removes all edges from a list from the graph."""
        for i, j in edges:
            self.remove_edge(i, j)
            
    def num_vertices(self):
        """Returns the number of vertices in the graph."""
        return self._num_vertices

    def num_edges(self):
        """Returns the number of edges in the graph."""
        return len(tuple(self.edges()))
    
    def edges(self):
        """Returns an iterator over the edges of the graph."""
        for i in range(self._num_vertices):
            for edge in self.out_edges(i):
                yield edge
    
    def __str__(self):
        """Returns a string representation of the graph, so that it may be printed."""
        return "DirectedGraph with %d vertices and %d edge(s):\n%s" % (self.num_vertices(),
                                                                       self.num_edges(),
                                                                       sorted(self.edges()))

        
class AdjacencyListDirectedGraph(DirectedGraph):
    """An implementation of a Directed Graph that uses adjacency lists to store edges.
    
    Overrides add_edge, remove_edge, has_edge, out_edges, in_edges, indegree, and outdegree.
    Note, some methods did not need to be overidden, but were for efficiency."""
        
    def __init__(self, num_vertices):
        """Constructs an ALD graph with num_vertices vertices and empty out/in lists"""
        super().__init__(num_vertices)
        self._out_lists = [[] for i in range(num_vertices)]
        self._in_lists = [[] for i in range(num_vertices)]
    
    def add_edge(self, i, j):
        """Adds the directed edge (i, j) to the graph by updating its in & out edges."""
        self._out_lists[i].append(j)
        self._in_lists[j].append(i)
        
    def remove_edge(self, i, j):
        """Removes the directed edge (i, j) to the graph by updating its in & out edges."""
        if self.has_edge(i, j):
            self._out_lists[i].remove(j)
            self._in_lists[j].remove(i)
        else:
            print(f"The edge {(i, j)} does not exist in the current graph")
    
    def has_edge(self, i, j):
        """Returns True if the graph contains the directed edge (i, j), False otherwise."""
        return j in self._out_lists[i]
        
    def out_edges(self, i):
        """Returns a list of directed edges outgoing from vertex i."""
        return [(i, j) for j in self._out_lists[i]]
        
    def in_edges(self, j):
        """Returns a list of directed edges incoming to vertex j."""
        return [(i, j) for i in self._in_lists[j]]
    
    def indegree(self, i):
        """Returns the indegree of vertex i."""
        return len(self._in_lists[i])
        
    def outdegree(self, i):
        """Returns the outdegree of vertex i."""
        return len(self._out_lists[i])
