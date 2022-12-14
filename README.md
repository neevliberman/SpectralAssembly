# SpectralAssembly
The Eulerian path algorithm for spectral assembly with k-mer multiplicity

### Problem to Solve:

The spectral assembly task assumes that each ð-mer in the input spectrum occurs exactly once in the genome sequence. It is possible to relax this assumption if we can provide as input the multiplicity of each  ð-mer (i.e., the number of times the ð-mer occurs in the genome). This generalized task can also be solved using the same Eulerian path algorithm but with a slightly different construction of the graph: for a ð-mer with multiplicity  ð , we will add  ð  edges from the node representing the length  ðâ1  prefix of the  ð -mer to the node representing the length  ðâ1  suffix of the  ð -mer. This construction results in what is often called a multigraph, in which pairs of nodes can have multiple edges connecting them.

The file assembly.py has a function, euler_assemble_multi, that takes as input a set of ð-mers with their multiplicities and outputs a superstring such that each input ð-mer with multiplicity ð occurs as a substring of the superstring exactly ð times. We will represent the input with a dictionary object that has ð-mers as keys and their corresponding multiplicities as values. To solve this problem, the Eulerian path finding algorithm will be utilized, with the graph consruction modification described above.

### Assumptions:

- We are assembling a single-stranded DNA sequence
- There exists such a superstring
- ð > 1 

### Note: 

There exist valid k-mer spectra for which the corresponding k-mer graph has two unbalanced vertices, and the âfake edgeâ one would add to balance those vertices already exists in the graph. To make the Eulerian cycle algorithm work, one still needs to add an extra âfake edgeâ in this case.
