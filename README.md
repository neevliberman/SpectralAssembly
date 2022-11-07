# SpectralAssembly
The Eulerian path algorithm for spectral assembly with k-mer multiplicity

### Problem to Solve:

The spectral assembly task assumes that each 𝑘-mer in the input spectrum occurs exactly once in the genome sequence. It is possible to relax this assumption if we can provide as input the multiplicity of each  𝑘-mer (i.e., the number of times the 𝑘-mer occurs in the genome). This generalized task can also be solved using the same Eulerian path algorithm but with a slightly different construction of the graph: for a 𝑘-mer with multiplicity  𝑚 , we will add  𝑚  edges from the node representing the length  𝑘−1  prefix of the  𝑘 -mer to the node representing the length  𝑘−1  suffix of the  𝑘 -mer. This construction results in what is often called a multigraph, in which pairs of nodes can have multiple edges connecting them.

The file assembly.py has a function, euler_assemble_multi, that takes as input a set of 𝑘-mers with their multiplicities and outputs a superstring such that each input 𝑘-mer with multiplicity 𝑚 occurs as a substring of the superstring exactly 𝑚 times. We will represent the input with a dictionary object that has 𝑘-mers as keys and their corresponding multiplicities as values. To solve this problem, the Eulerian path finding algorithm will be utilized, with the graph consruction modification described above.

### Assumptions:

- We are assembling a single-stranded DNA sequence
- There exists such a superstring
- 𝑘 > 1 

### Note: 

There exist valid k-mer spectra for which the corresponding k-mer graph has two unbalanced vertices, and the “fake edge” one would add to balance those vertices already exists in the graph. To make the Eulerian cycle algorithm work, one still needs to add an extra “fake edge” in this case.
