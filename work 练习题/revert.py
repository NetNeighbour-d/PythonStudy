#逆序输出列表

a=[1,2,3,4,5,6]
for i in range(len(a)):
    print(a[-i-1])

#其他方法
#输出的结果仍是一个列表
a1=list(reversed(a))
print(a1)

a2=a[::-1]  #代表从后往前取值，每次步进值为1
print(a2)