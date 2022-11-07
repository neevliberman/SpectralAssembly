import graph
import euler

def minus_one(kmer_counts):
    """Returns a list of k_minus_one_mers, given a dictionary of kmer counts."""
    
    k_minus_one_mers = []
    for kmer in list(kmer_counts):
        if kmer[:-1] not in k_minus_one_mers:
            k_minus_one_mers.append(kmer[:-1])
        if kmer[1:] not in k_minus_one_mers:
            k_minus_one_mers.append(kmer[1:])
            
    return k_minus_one_mers

def construct_graph(g, kmer_counts, k_minus_one_mers):
    """Adds an edge between each corresponding (k-1)-mer."""

    for kmer in kmer_counts:
        m = kmer_counts[kmer]
        k1 = k_minus_one_mers.index(kmer[:-1])
        k2 = k_minus_one_mers.index(kmer[1:])
        for _ in range(m):
            g.add_edge(k1, k2)
            
def create_fake_edge(g, kmer_len):
    """Creates a fake edge if there are any nodes with outdegree = indegree + 1 or vice versa
    
    Returns None for both vertices if there is no fake edge created.

    Args:
        g: ALD graph object
        kmer_len: number of (k-1)-mers
    Returns:
        A tuple of the form (vertex_A, vertex_B) from which the fake edges were created
    """
    v1 = None
    v2 = None
    for i in range(len(kmer_len)):
        if not v1 and g.indegree(i) - g.outdegree(i) == 1:
            v1 = i
        elif not v2 and g.indegree(i) - g.outdegree(i) == -1:
            v2 = i
        if v1 is not None and v2 is not None:
            g.add_edge(v1, v2)
            break 
        
    return v1, v2
    

def join_loops(cycles):
    """Joins multiple cycles found in an eulerian griph into one big cycle.

    Args:
        cycles: a 2d list, where each list represents an eulerian cycle in the graph
    Returns:
        A list of vertices representing the final joined loop
    """
    
    joined = []
    # for each cycle to join...
    for cycle in cycles:
        # initialize joined list to just be the first cycle
        if not joined:
            joined.extend(cycle)
        else:
            # for each vertex in the cycle to join
            for vertex in cycle:
                # try to find shared vertex
                if vertex in joined:
                    # update joined to be the new joined cycle
                    i = joined.index(vertex)
                    joined = joined[:i] + cycle + joined[i+1:]
                    # break and continue to next cycle
                    break
                
    return joined


def euler_assemble_multi(kmer_counts):
    """Assembles a set of kmers with multiplicities using the Eulerian path algorithm.
    
    Args:
        kmer_counts: a dictionary with k-mers as keys and corresponding multiplicities as values
    Returns:
        A superstring such each input k-mer with multiplicity m is contained as a substring exactly m times
    """
    
    # make list of unique (k-1)mers to associate with index for graph construction
    k_minus_one_mers = minus_one(kmer_counts)
    
    # construct graph
    g = graph.AdjacencyListDirectedGraph(len(k_minus_one_mers))
    construct_graph(g, kmer_counts, k_minus_one_mers)
        
    # Find which vertex is missing inedges and which vertex is missing outedges in graph, 
    # create fake edge if necessary
    v1, v2 = create_fake_edge(g, len(k_minus_one_mers))
    
    # find first cycle in graph, insert into list for later access
    cycles = [euler.find_cycle_in_eulerian_graph(g, 0)]

    # while there are still edges to go over
    while g.num_edges() > 0:
        start = next(g.edges())[0] # set the next starting vertex to the next available edge
        cycles.append(euler.find_cycle_in_eulerian_graph(g, start)) # find the next cycle

    # join seperate loops into one big loop
    joined = join_loops(cycles)                 
    
    # remove the fake edge:
    if v1 is not None and v2 is not None:
        # cut off last redundant vertex
        joined = joined[:-1]
        # convert joined to a string to find substring easier. Then find index of where to split.
        temp_joined = ''.join([str(i) for i in joined])
        split_idx = temp_joined.find(str(v1)+str(v2)) + 1
        joined = joined[split_idx:] + joined[:split_idx]
          
    
    # finally, construct the superstring. initialize with first vertex in final loop.
    superstring = k_minus_one_mers[joined[0]]
    for i, v in enumerate(joined):
        if i == 0:
            continue
        superstring += k_minus_one_mers[v][-1]
    
    return superstring