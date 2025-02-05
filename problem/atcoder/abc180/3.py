n = int(input())

#約数をリストで全列挙する

def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n　//　i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

lis = make_divisors(n)

for i in range(len(lis)):
    print(lis[i])
