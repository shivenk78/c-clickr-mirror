code = int(input())
code1 = code
code4 = 0
while (code != 0):
    code4 *= 10
    code4 += code % 4
    code = int(code/4)
code4Str = str(code4)
for i in range(len(code4Str), 16):
    code4Str += "0"
code4Str = code4Str[::-1]
print(code4Str)
code4Int = int(code4Str)
print(code4Int)

code4Str = code4Str[::-1]
uin = 0
for i in range(16):
    dig = int(code4Str[i])
    uin += dig * (4 ** i)
print(uin)