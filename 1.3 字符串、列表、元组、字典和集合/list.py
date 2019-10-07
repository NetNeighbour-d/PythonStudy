# -*- coding:utf-8 -*-

#列表
list1=['physics','chemistry',1997,2000]
list2=[1,2,3,4,5]
list3=['a','b','c','d','f']

print('list1[0]:',list1[0])
print("list3[1:3]",list3[1:3])  #只有list3[1]、list3[2]的值，不包括list3[3]

#更新
print('list1[2]原先值:',list1[2])
list1[2]=2001
print('list1[2]更改值',list1[2])

#删除
print('删除前：',list1)
del(list1[2])
print('删除后：',list1)

#操作符
print('list1:',list1)
print('list2:',list2)

list4=list1+list2
print("list1 + list2 :",list4)

list5=['hello']*4
print('[\'hello\']*4 :',list5)

#截取
print('list4 :',list4)
#正数从0开始
print('list4[2] :',list4[2])
#倒数正常计数
print('list4[-2] :',list4[-2])
print('list4[1:] :',list4[1:])