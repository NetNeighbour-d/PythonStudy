# -*- coding:utf-8 -*-

a=0o101  #八进制
print("a="+str(a))  #str() 字符转化

b=64
print("b="+str(b))
c=-237
print("c="+str(c))
d=0x80  #十六进制
print("d="+str(d))
e=-0x92
print("e="+str(e))

#格式转换
print(int(2.4345))
print(int(2.67676))  #直接截断，无四舍五入
print(float(4))
print(complex(4))

#进制转换
print(hex(255))  #十六进制
print(oct(255))
print(oct(0x111))  #十进制

#ASII转换
print(chr(76))
print(ord('L'))