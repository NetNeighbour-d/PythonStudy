
#range和xrange
#range可以生成一个等差数列
#range[start,end,step=1]

#range
a=range(5)
b=range(2,5)
c=range(2,5,2)

print(a)
print(b)
for i in c:
    print("value is",i)

#xrange与range用法一致，但生成的不是数组，而是一个生成器
#python3中没有xrange函数
d=xrange(8)
print(d)
print(list(d))

#break、continue和pass

#break
#可以跳出最近一级for或者while循环
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0 :
        #%求mod，即计算除法的余数
        #即判断是否可以整除
            print(n,'equals',x,'*',n//x)  #//取整除 - 返回商的整数部分(向下取整)
            break
    else:
        print(n,'is a prime number')

#for..else的写法是存在的，即执行完for后执行else
#如果for正常执行完，else将会被执行
#如果else不被执行，那么for语句中很有可能会出现break、return、异常

#continue
#表示循环继续执行下一次迭代
#输出奇数
for num in range(2,10):
    if (num % 2 ==0):
        continue
    print(num)


#pass 
#pass语句什么也不做，相当于汇编的nop指令
#占位
#可用来规划程序功能和结构

def funcname(parameter_list):
    pass

