##Maze Creation
A python script that creates maze, implementing [Depth-First Algorithm](https://en.wikipedia.org/wiki/Depth-first_search). The output maze is organized like a graph. The result is saved to a text file with the following format:  
```
(5, 2), (6, 2)
(6, 2), (6, 3)
(6, 3), (7, 3)
```

### Depth-first Search
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking.

![example of DFS](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Depth-first-tree.svg/300px-Depth-first-tree.svg.png)

### DFS in Pseudocode
```
1  procedure DFS(G,v):
2      label v as discovered
3      for all edges from v to w in G.adjacentEdges(v) do
4          if vertex w is not labeled as discovered then
5              recursively call DFS(G,w)
```