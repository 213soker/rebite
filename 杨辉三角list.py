def triangles():
    L = [1]
    while True:
        yield L
        L = L + [0]
#        L.append(0)  #不行，会在原地址添加0，进而修改下面的t
        L = [L[N] + L[N-1] for N in range(len(L))]#相当于[0，1，0] [0，1，1，0]


def triangles_1():
    L = [1]
    while True:
        yield L
        L = [L[i] + L[i-1] if i > 0 else L[i] for i in range(len(L))]
        L.append(1)
      

n = 0
results = []
for t in triangles_1():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')