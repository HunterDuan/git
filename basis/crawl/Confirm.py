fp = open('user.txt','a+')
reg_time = 1
while  True:
	is_reg = False
	account = input('请输入你要注册的账号：')
	fp.seek(0,0)
	for buf in fp:
		account_buf = buf.split(':')[0]
		if account_buf == account:
			is_reg = True
			break
	if not is_reg:
		passwd1 = input('请输入你要注册的密码：')
		passwd2 = input('请再次输入你要注册的密码：')
		if passwd2 == passwd1:
			str = '%s:%s\n'%(account,passwd1)
			fp.write(str)
			print('注册成功')
			break
		else:
			print('密码不同，请再次输入')
			continue
	else:
		if reg_time <= 3:
			print('已经被注册，这是你第%d次尝试注册，你还剩余%d次机会'%(reg_time,4 - reg_time))
			reg_time += 1
		else:
			print('机会用尽，再见！')
			break
fp.close()


