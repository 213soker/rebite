def trim(s):

    if s == '':
        return ''

    while  s[0] == ' ' or s[-1] == ' ':
        if s[0] == ' ':
            s = s[1:]
        else:
            s = s[:-1]

        return trim(s)

    return s


if trim(' hello  ') != 'hello':
    print('1测试失败!')
elif trim('  hello') != 'hello':
    print('2测试失败!')
elif trim('  hello  ') != 'hello':
    print('3测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('4测试失败!')
elif trim('') != '':
    print('5测试失败!')
elif trim('    ') != '':
    print('6测试失败!')
else:
    print('测试成功!')
