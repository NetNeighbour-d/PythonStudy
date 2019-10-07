#查找字符串中一段连续内容并替换
b='asdfghjklfghasdfghjkl'
if 'fgh' in b:
    c=b.replace("fgh","123")  #使用replace方法进行替换
    print(b)
    print(c)

#字符串本身是不可变的，无法修改本身
#只能创造副本来获得最后的结果

#查找的另一种方法，可以获得位置
to_find = "fgh"
b2=b
index=0
while (b2.find(to_find)>0) :
    index += b2.find(to_find)
    print('字串所在位置：',index)
    index +=3  #跳过本身
    b2=b[(index):]
    print(b2)