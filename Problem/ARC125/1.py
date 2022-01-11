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
def str_row_list(N): return [list(str_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 10 ** 9 + 7
mod = 998244353
lower_start = 97 #"a"のASCIIコード
upper_start = 65 #"A"のASCIIコード
number_start = 48 #"0"のASCIIコード

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n, m = int_map()
    s = int_list()
    t = int_list()

    if len(set(s)) == 1 and set(s) != set(t):
        print(-1)
        exit()

    front = 0; back = 0
    flag = s[0]
    for i in range(n):
        if s[i] != flag:
            front = i
            break
    for i in range(n - 1, -1, -1):
        if s[i] != flag:
            back = n - i
            break
    #print(front, back)

    ans = 0; move = False
    for i in range(m):
        if t[i] == flag:
            ans += 1
        else:
            if not move:
                ans += min(front, back)
                ans += 1
                flag ^= 1
                move = True
            else:
                ans += 2
                flag ^= 1
    print(ans)


if __name__ == '__main__':
    main()
