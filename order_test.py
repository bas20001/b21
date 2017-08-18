from collections import OrderedDict
py_word = {}
py_word = OrderedDict()
def show_word() :
	for key,value in py_word.items():
		print("The python word " + key + "\n It " + value)

py_word["print"] = 'mean print on your screen'
py_word["for"] = 'mean make a loop in the formula'
py_word["def"] = 'mean use the def to the formula'
py_word["import"] = 'mean use a module'
show_word()
