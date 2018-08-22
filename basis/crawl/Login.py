#用户登陆，user.txt存在已有账户信息
myfile = open('user.txt', 'r')
logintimes = 0
islogin = 1
while True:
	if islogin == 1:
		if logintimes == 3:
			print('登陆超过次数，再见')
			break
		else:
			print('这是你第%d次登陆，你还剩余%d次机会'%(logintimes + 1 , 3 - logintimes))
			account = input('请输入你的账户：')
			password = input('请输入你的密码：')
			myfile.seek(0,0)
			for buf in myfile:
				account_buf = buf.split(':')[0]
				password_buf = buf.split(':')[1][:-1]
				if account_buf == account and password == password_buf:
					print('登录成功：', account_buf)
					islogin = 0
					break
			logintimes += 1
			continue
	else:
		break
