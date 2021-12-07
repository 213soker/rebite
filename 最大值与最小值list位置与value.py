from collections.abc import Iterable

def findMinAndMax(L):

    if L == []:
        return (None,None)

    temp_max = temp_min = L[0]
    temp_max_mun = temp_min_mun = 0
    for i,value in enumerate(L):
        if value > temp_max:
            temp_max = value
            temp_max_mun = i
        
        if value < temp_min:
            temp_min = value
            temp_min_mun = i

    print(f'最大值位置是：{temp_max_mun}，最小值是：{temp_min_mun}')
    return (temp_min,temp_max)



# 测试
if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('测试成功!')