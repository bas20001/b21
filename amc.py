N = 10
A = [5,3,2,1,7,6,4,8,11,9]
min1 = min(A)
max1 = max(A)
sum1 = len(A)
sn = (min1 + max1)*sum1 / 2
if sum(A) == sn:
	print ("True")
else :
	print ("False")
