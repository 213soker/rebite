# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    number = s.find('.')
    str_top = s[:number]
    str_down = s[number+1:]
    str_point = pow(10,len(str_down))#计算小数点位数
    
    
    def benumber(str1,flag):
        def temp(x,y):#单个int数值化
            return x * 10 + y

        def beInt(top):#单个字符int化
            digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
            return digits[top]

        result = reduce(temp,map(beInt,str1))#字符转int数值

        if flag == 1:
            return result
        else:   
            return result/str_point#小数化

    result = benumber(str_top,1) + benumber(str_down,0)
    return result

print('str2float(\'123.456\') =', str2float('123.456'))

if abs(str2float('123.456') - 123.456) == 0:
    print('测试成功!')
else:
    print('测试失败!')
