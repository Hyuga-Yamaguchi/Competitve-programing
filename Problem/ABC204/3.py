import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
#import numpy as np #pypyでは使用不可
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
def int_row(N): return [int_input() for _ in range(N)]
def int_row_list(N): return [int_list() for _ in range(N)]
def str_input(): return input()[:-1]
def str_map(): return input().split()
def str_list(): return list(str_map())
def str_row(N): return [str_input() for _ in range(N)]
def str_row_list(N): return [list(str_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353

n, m = int_map()

def main():
    if m == 0:
        return n
    g = [[] for _ in range(n)]
    for i in range(m):
        a, b = int_map()
        g[a - 1].append(b - 1)
    #print(g)
    ans = 0
    for i in range(n):
        dist = bfs(g, i)
        for j in range(n):
            if dist[j] != None:
                ans += 1
    return ans

def bfs(g, u):
    queue = deque([u])
    d = [None] * n
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

if __name__ == '__main__':
    print(main())
