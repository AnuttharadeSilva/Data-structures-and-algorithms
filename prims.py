#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the prims function below.
def prims(n, edges, start):
    edgesList = {}
    weight = 0
    for i in range(1, n+1):
        edgesList[i] = []
    for j in edges:
        [x, y, z] = j
        edgesList[x] += [[y,z]]
        edgesList[y] += [[x,z]]

    mst = set([start])
    while len(mst) < n:
        minNo = sys.maxsize
        minNode = -1
        for i in mst:
            for j in edgesList[i]:
                if j[0] not in mst:
                    if j[1] < minNo:
                        minNo = j[1]
                        minNode = j[0]
        if minNode > 0:
            mst.add(minNode)
            weight += minNo
    return weight

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))
    start = int(input())

    result = prims(n, edges, start)
    print(str(result))
