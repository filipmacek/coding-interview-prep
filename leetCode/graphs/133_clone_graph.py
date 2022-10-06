"""
---
title: Clone graph
number: 133
difficulty: medium
tags: ['Hash table','Depth-First Search','Bread-First Search','Graph']
url: https://leetcode.com/problems/clone-graph/
solved: false
---
"""
from typing import List

"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

"""


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Node(val: {self.val},neighbors: {self.neighbors})"

def make_graph(adj_list: List):
    nodes = [Node(i+1) for i in range(len(adj_list))]
    for i,neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    return nodes[0]

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None


if __name__ == '__main__':
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph = make_graph(adjList)
    print(Solution().cloneGraph(graph))
