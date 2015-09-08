"""MazeCreator"""
#
# MazeCreator.py
#
# @author Alexandros Lattas
#
# created with Spyder
#


# Imports

import sys
import random

# input handling

N = int(sys.argv[2])
START_X = int(sys.argv[3])
START_Y = int(sys.argv[4])
random.seed(sys.argv[5])
OUTPUTFILE = sys.argv[6]

# Visited creation

visited = [[0 for i in range(N)] for i in range(N)]

# ADJ_LIST creation

ADJ_LIST = [[0 for i in range(N)] for i in range(N)]

ADJ_LIST[0][0] = [(0, 1), (1, 0)]
ADJ_LIST[0][N - 1] = [(0, N - 2), (1, N - 1)]
ADJ_LIST[N - 1][0] = [(N - 2, 0), (N - 1, 1)]
ADJ_LIST[N - 1][N - 1] = [(N - 1, N - 2), (N - 2, N - 1)]

for i in range(1, N - 1):
    ADJ_LIST[0][i] = [(0, i - 1), (0, i + 1), (1, i)]
    ADJ_LIST[N - 1][i] = [(N - 1, i - 1), (N - 1, i - 1), (N - 2, i)]
    ADJ_LIST[i][0] = [(i - 1, 0), (i + 1, 0), (i, 1)]
    ADJ_LIST[i][N - 1] = [(i - 1, N - 1), (i + 1, N - 1), (i, N - 2)]

for i in range(1, N - 1):
    for j in range(1, N - 1):
        ADJ_LIST[i][j] = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

# OUTPUT creation

#OUTPUT = [(0,0) for i in range(100)]
OUTPUT = []

# Depth-First Search

def dfs(x, y):
    """Recursive Depth-First Search"""
    visited[x][y] = 1
    random_adj = random.sample(ADJ_LIST[x][y], len(ADJ_LIST[x][y]))

    for h in range(len(random_adj)):

        if not visited[random_adj[h][0]][random_adj[h][1]]:

            OUTPUT.append([(x, y), (random_adj[h][0], random_adj[h][1])])
            dfs(random_adj[h][0], random_adj[h][1])

dfs(START_X, START_Y)

# FileWrite

FILE = open(OUTPUTFILE, 'w')

for i in range(N * N - 1):
    FILE.write(str(OUTPUT[i][0]) + ", " + str(OUTPUT[i][1]))
    FILE.write('\n')

FILE.close()

print('maze created')
