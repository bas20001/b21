# -*- coding:UTF-8 -*- 
# -*- coding:gb2312 -*- 
# -*- coding:GBK -*- 
unknown_answer = raw_input("������һ�����ַ�Χ��(1,100)����")
unknown_answer = int(unknown_answer)
right_answer = 47
if int(unknown_answer) > int(right_answer):
	print("�ٺ�,����,����������ֱȴ�Ҫ��Ŷ �����԰�~ : ")
elif int(unknown_answer) < int(right_answer):
	print("����,����,����������ֱȴ�ҪСŶ �����԰�~ : ")
else :
	print("�¶��ˣ��ҵı������Ǵ�����")
while int(unknown_answer) != int(right_answer):
	unknown_answer = raw_input("������һ�����ַ�Χ��(1,100)����")
	if int(unknown_answer) > int(right_answer):
		print("�ٺ�,����,����������ֱȴ�Ҫ��Ŷ �����԰�~ :  ")
	elif int(unknown_answer) < int(right_answer):
		print("����,����,����������ֱȴ�ҪСŶ �����԰�~ : ")
	else :
		print("�¶��ˣ��ҵı������Ǵ�����")
