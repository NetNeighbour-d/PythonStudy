#python默认编码为ASCII格式，无法正确打印汉字
#需要修改编码为utf-8 
#2.0版本，3.0版本已经包含了

#字典
#键值形式 key:value

dict = {'Name':'Zara','Age':7,'Class':'First'}

print("dict['Name']:",dict['Name'])
print('dict[\'Age\']:',dict['Age'])

#修改值
print("dict['Age']修改前:",dict['Age'])
dict['Age']=8
print("dict['Age']修改后:",dict['Age'])

#删除
print('删除age前',dict)
del dict['Age']
print('删除age后',dict)
dict.clear()
print('清空后',dict)
del dict  #删除字典

print('删除字典后',dict)