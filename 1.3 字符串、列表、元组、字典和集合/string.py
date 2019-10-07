#字符串
str1='Hello World！'
print('声明字符串')
print(str1)

#字符串截取
print('str1[0]:',str1[4])
print('str1[1:5]:',str1[1:5])  #从0开始数

#字符串操作符
a='hello'
b='world'

print('a+b=',a+b)
print('a*2=',a*2)

if('h' in a):  #if后面需要加上:号
   print('h在a中')
else:
   print('h不在a中')

if('m' in b):
   print('m在b中')
else:
   print('m不在b中')

print(r'\n')  #可以直接打印出\n来
print('\n')   #直接换行了

#格式化输出
print("My computer's name is %s and it is %d years old"%('破牙',1))
print("format method : My computer's name is {name} and it is {age} years old".format(name='破牙',age=1))

#三引号 跨行
hi = ''' hello
 world '''
print(hi)

