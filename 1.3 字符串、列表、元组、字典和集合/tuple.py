# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

#元组
#元组元素不可修改
#使用小括号

tup0=()
tup1=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5)
tup3="a","b","c","d"
tup4=(50,)  #元组只包含一个元素时，需要在元素后面添加逗号

print('tup0:',tup0)
print('tup1:',tup1)
print('tup2[1:5]:',tup2[1:5])  #超出范围也可以显示数值，为实际数值
print('tup3:',tup3)
print('tup4*4:',tup4*4)
print('tup2+tup3:',tup2+tup3)
print('tup1[1:]:',tup1[1:])
print('tup1[-2]:',tup1[-2])

