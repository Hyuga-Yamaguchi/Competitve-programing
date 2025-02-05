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
    n = int_input()

    if n % 2 == 1:
        print("")
        exit()

    ans = []
    for bit in range(1 << n):
        cnt_0 = 0; cnt_1 = 0; flag = True
        for i in range(n):
            if (bit >> i) & 1:
                cnt_0 += 1
            else:
                cnt_1 += 1
            if cnt_0 > cnt_1:
                flag = False
        if flag and cnt_0 == cnt_1:
            s = str(bin(bit))[2:]
            #print(s)
            t = ""
            for j in range(len(s)):
                if s[j] == "1":
                    t += "("
                else:
                    t += ")"
            #print(t)
            ans.append(t)
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()
