# CMPS 2200 Recitation 08

## Answers

**Name:** Jaedan Curcio



Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**

  - This algorithm is an implementation of Dijkstra's algorithm modified to track the number of edges in the path in order to return the path with smallest edge weight and least edges.
The tracking/comparison of the edges itself takes place in constant time, and the rest of the algorithm has the same work as Dijstra's, so the work is O(|E| log(|E|)), since heap operations are performed once per each edge. Since
the heap operations cannot be parallelized, the span is also O(|E| log(|E|))





