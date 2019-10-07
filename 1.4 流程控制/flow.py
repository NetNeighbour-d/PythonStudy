
# if...else

x=int(input('请输入一个整数：'))  #input,在终端等待用户输入
if x==0 :
    print('输入的整数为%d,==0' %x)
elif x<0:
    print('输入的整数为%d,<0' %x)
else:
    print('输入的整数为%d,>0' %x)


#for语句

words = ['cat','window','defenestrate']
for word in words:
    print(word,len(word))


for word in words[:]: 
#切片操作，基本表达式 object[start_index:end_index:step]
#不只是列表，字符串和元组都可操作
#words[:]相当于拷贝出一个副本来
    if len(word)>6:
        words.insert(2,word)  #将指定对象插入到指定位置
print(words)


#while语句

count=0
while(count<9):
    print('the index is:',count)
    count +=1


