n, q = map(int, input().split())
s = input()

a = [0] * n
for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "C":
        a[i + 1] += 1
#print(a)

for i in range(n - 1):
    a[i + 1] += a[i]

#print(a)

for i in range(q):
    l, r = map(int, input().split())
    print(a[r - 1] - a[l - 1])
