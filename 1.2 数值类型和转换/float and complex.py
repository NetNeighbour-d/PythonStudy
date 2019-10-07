#双精度浮点型

a=0.0
print(a)
print(0.0)
print(-777.)
print(-5.327847213)
print(96e3*1.0)  #可以使用科学计数法
print(-1.739E-19)

#decimal类型，主要用于金融计算,精度较高
#十进制浮点型

from decimal import *

dec=Decimal('.1')
print(dec)
print(Decimal(0.1))
a=Decimal(0.1)
print(len(str(a)))
b=dec+Decimal(0.1)
print(dec+Decimal(0.1))
print(len(str(b)))

#复数
print(complex(2,4))
print(1.23e-045+6.7e+089j)