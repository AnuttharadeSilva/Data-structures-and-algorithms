#!/bin/python3

import math
import os
import random
import re
import sys
from queue import Queue

class Node():
    def __init__(self):
        self.visited = False
        self.children = []
        self.distance = -1

# Complete the bfs function below.
def bfs(n, m, edges, s):
    nodesList = []
    for i in range(n):
        nodesList.append(Node())

    for j in edges:
        first, second = [nodesList[i - 1] for i in j]
        first.children.append(second)
        second.children.append(first)
    
    startNode = nodesList[s - 1]
    startNode.distance = 0
    queue = Queue()
    queue.put(startNode)
    while(not queue.empty()):
        node = queue.get()
        for child in node.children:
            if (not child.visited) or (child.distance > node.distance + 6):
                child.distance = node.distance + 6
                child.visited = True
                queue.put(child)
    del nodesList[s - 1]
    return [node.distance for node in nodesList]


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))
        s = int(input())

        result = bfs(n, m, edges, s)
        print(' '.join(map(str, result)))