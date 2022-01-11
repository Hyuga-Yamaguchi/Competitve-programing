import sys, re
# from math import ceil, floor, sqrt, pi, factorial, gcd
# from copy import copy, deepcopy
from collections import Counter, deque
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
# from functools import reduce
# from decimal import Decimal, getcontext
# from operator import itemgetter
#import numpy as np #pypyでは使用不可
input = sys.stdin.readline
def int_input(): return int(input())
def int_map(): return map(int, input().split())
def int_list(): return list(int_map())
# def int_row(N): return [int_input() for _ in range(N)]
# def int_row_list(N): return [int_list() for _ in range(N)]
# def str_input(): return input()[:-1]
# def str_map(): return input().split()
# def str_list(): return list(str_map())
# def str_row(N): return [str_input() for _ in range(N)]
# def str_row_list(N): return [list(str_input()) for _ in range(N)]
# def lcm(a, b): return a * b // gcd(a, b)
# sys.setrecursionlimit(10 ** 9)
# INF = 1 << 60
# MOD = 10 ** 9 + 7
# mod = 998244353

#メモリ消費を抑える時はグローバル空間に書く
def main():
    n = int_input()
    a = int_list()

    b = [None for _ in range(n)]
    #累積和
    b[0] = a[0]
    for i in range(1, n):
        if i % 2 == 1:
            b[i] = b[i - 1] - a[i]
        else:
            b[i] = b[i - 1] + a[i]
    b = [0] + b

    #座標圧縮
    c = sorted(list(set(b)))
    b_comp = [None] * (n + 1)
    for i in range(n + 1):
        b_comp[i] = bisect_left(c, b[i])

    u = [0] * (n + 1)
    for i in range(n + 1):
        u[b_comp[i]] += 1

    ans = 0
    for i in range(len(u)):
        if u[i] > 1:
            ans += u[i] * (u[i] - 1) // 2
        if u[i] == 0:
            break
    print(ans)


if __name__ == '__main__':
    main()