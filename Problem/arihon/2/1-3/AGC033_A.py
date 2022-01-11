import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
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

#メモリ消費を抑える時はグローバル空間に書く
def main():
    h, w = int_map()
    a = str_row_list(h)

    seen = [[INF] * w for _ in range(h)]
    black = deque()
    for i in range(h):
        for j in range(w):
            if a[i][j] == "#":
                black.append([i, j])
                seen[i][j] = 0

    while black:
        #print(black)
        [y, x] = black.popleft()
        for (dy, dx) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ny = y + dy; nx = x + dx
            if not 0 <= ny < h or not 0 <= nx < w:
                continue
            if a[ny][nx] == "#":
                continue
            a[ny][nx] = "#"
            if seen[ny][nx] == INF:
                seen[ny][nx] = seen[y][x] + 1
            black.append([ny, nx])
        #print(a)
        #print(seen)
    ans = 0
    for i in range(h):
        for j in range(w):
            ans = max(ans, seen[i][j])
    print(ans)


if __name__ == '__main__':
    main()
