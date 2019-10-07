#使用while循环实现输出2-3+4-5+6.....+100的和

count=2
sum=0
while(count<=100):
    if(count % 2 == 0):
      sum += count
    else:
      sum -= count
    count += 1

print(sum)