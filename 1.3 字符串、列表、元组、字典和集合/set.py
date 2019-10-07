#集合

s1=set('abcdef')   #可变集合
s2=set([1,2,3,4,5])
s3=frozenset("test")  #不可变集合

print(type(s1))  #显示类型
print(type(s3))
print(s2)

#集合是无序的，只能循环遍历或者使用in、not in来访问或判断集合元素
for item in s3:
    print(item)  
#同样数值的不会遍历出来。默认算作一个
#即集合无序，无重复元素

#集合更新
print("原始数据",s2)
s2.add("jss")
print("添加数据j后：",s2)
s2.remove(3)
print("删除数据3后：",s2)
s2.update('jss')
print("update数据后：",s2) 
#update是将拆分字符串进行追加，而add是整体追加

#操作符


s2=set([1,2,3,4,5])
print('s1:',s1)
print('s2:',s2)
print('s1|s2:',s1|s2) #union，相当于or
print('s1&s2:',s1&s2) #相当于交集
print('s1-s2:',s1-s2) #差集
print('s1 dif s2:',s1.difference(s2)) #差集
