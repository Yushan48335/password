num = 3
while num > 0:
	num = num - 1
	password = input("密碼是： ")
	if password == 'a123456':
		print('密碼成功')
		break
	else:
		if num > 0:
			print('密碼錯誤！還有', num, '次機會')
		else:
			print('您的帳號已鎖住，請聯絡電腦中心')