def func(a,N):
    s = a**N
    t = 1
    for i in range(1,N):
        t *= i
        s += a**N / t
    result = a**N/(a**N + t*(N-a)*s)
    return result
a = float(input('请输入A'))
N = int(input('请输入N'))
print(func(a,N))