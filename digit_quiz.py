# -*- coding:UTF-8 -*- 
# -*- coding:gb2312 -*- 
# -*- coding:GBK -*- 
unknown_answer = raw_input("请输入一个数字范围在(1,100)以内")
unknown_answer = int(unknown_answer)
right_answer = 47
if int(unknown_answer) > int(right_answer):
	print("嘿嘿,宝宝,你输入的数字比答案要大哦 再试试吧~ : ")
elif int(unknown_answer) < int(right_answer):
	print("呼呼,宝宝,你输入的数字比答案要小哦 再试试吧~ : ")
else :
	print("猜对了！我的宝宝真是聪明宝")
while int(unknown_answer) != int(right_answer):
	unknown_answer = raw_input("请输入一个数字范围在(1,100)以内")
	if int(unknown_answer) > int(right_answer):
		print("嘿嘿,宝宝,你输入的数字比答案要大哦 再试试吧~ :  ")
	elif int(unknown_answer) < int(right_answer):
		print("呼呼,宝宝,你输入的数字比答案要小哦 再试试吧~ : ")
	else :
		print("猜对了！我的宝宝真是聪明宝")
		
		
