import sys, re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import copy, deepcopy
from collections import Counter, deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
from operator import itemgetter
#import numpy as np
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
def str_row_list(N): return [list(str_map()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード
number_start = 48 #"0"のASCIIコード

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        #各要素の親要素番号を格納するリスト　要素が根の場合は、-(そのグループの要素数)

    """要素xが属するグループの根を返す"""
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    """要素xが属するグループと要素yが属するグループとを併合する"""
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    """要素xが属するグループのサイズ（要素数）を返す"""
    def size(self, x):
        return -self.parents[self.find(x)]

    """要素x, yが同じグループに属するかどうかを返す"""
    def same(self, x, y):
        return self.find(x) == self.find(y)

    """要素xが属するグループに属する要素をリストで返す"""
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    """すべての根の要素をリストで返す"""
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    """グループの数を返す"""
    def group_count(self):
        return len(self.roots())

    """{ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す"""
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    """print()での表示用"""
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, m = int_map()
    uf = UnionFind(n)

    g = [[] for _ in range(n)]
    for i in range(m):
        a, b = int_map()
        a -= 1; b -= 1
        g[a].append(b)
    #print(g)

    uf = UnionFind(n); ans = [0]; cnt = 0
    for i in range(n - 1, -1, -1):
        cnt += 1
        for j in g[i]:
            if not uf.same(i, j):
                cnt -= 1
                uf.union(i, j)
        ans.append(cnt)    
    ans = ans[::-1][1:]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()
