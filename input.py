unknown_answer = input("Press a number range in (1,20)")
right_answer = 17
if unknown_answer > right_answer:
	print("It is not a right answer,It may be lower than your ")
elif unknown_answer < right_answer:
	print("It is not a right answer,It may be upper than your ")
else :
	print("Congrations! It is a right answer!")
