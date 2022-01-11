# 二分探索
import bisect

#################
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

#リストをソート
a = sorted(a)
b = sorted(b)
c = sorted(c)

count = 0
#a[i]の個数
for i in range(n):
    a_count = bisect.bisect_left(a, b[i])
    c_count = bisect.bisect_right(c, b[i])
    count += a_count * (len(c) - c_count)

print(count)
