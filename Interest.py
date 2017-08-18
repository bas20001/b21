interest = ""
days = ""
total_amount = ""
profit = ""
def licai_interest(profit,days,total_amount,):
	interest = int(profit)*365 /int(days)*int(total_amount)
	print("The interest is : " + str(interest))
	
ndays = raw_input("input days: ")
ntotal_amount = raw_input("input total_amount: ")
nprofit = raw_input("input profit: ")

licai_interest(nprofit,ndays,ntotal_amount)

	
