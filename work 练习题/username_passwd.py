
#用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败！

username=input('请输入用户名：')
passwd=input('请输入密码：')

if((username=='seven') & (passwd=='123')):
    print('登陆成功')
else:
    print('登陆失败')