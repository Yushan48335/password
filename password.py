num = 3
while True:
	password = input("密碼是： ")
	if password == 'a123456':
		print('密碼成功')
		break
	else:
		num = num - 1
		print('密碼錯誤！還有', num, '次機會')
		if num == 0:
			break

