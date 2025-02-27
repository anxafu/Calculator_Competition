# all operations
# + - / *
# () ^ !
# sqr(n)(x) -> x^(1/n)
# sin() , cos(), tan()
# abs() 
# log(10)(x) -> ln(x)


# inset your GPT generated calculator script to this function
# you are allowed to add extra functions as long as this is
# the main input/output function
# input: an equation string eg. "35 + 23 - 9"
# output: value string eg. "7,433"
def GPTcalculator(inpt:str) -> str :

	# delete everything here before you give it to people

	LevelBasic = [
		[("6 + 3", str(9)),("32 + 54", str(86)),("43 + 23 +  11", str(77))], # addition
		[("6 - 3", str(3)),("18 - 8", str(10)),("1 - 20", str(-19))], # subtraction
		[("5 * 11", str(55)),("102 * 10", str(1020)),("16 * 32", str(512))], # multiplication
		[("15 / 5", str(3)),("9 / 1", str(9)),("121 / 11", str(11))]  # division
	]

	LevelMedium = [
		[("(2 + 6) * 2", str(16)),("(5 * (6 / 2) - 5)", str(10)),("(23 - 24) / 10", str(-0.1))], # bracets
		[("6^2 - 2", str(32)),("7^4 / 5 +  6", str(486.2)),("35^4 - 34^4", str(164289))], # powers
		[("9! / 5", str(72576)),("6! - 5! * 3!", str(0)),("7! / 4! * 5 - 24", str(1024))], # factorials
	]

	LevelHard = [
		[("", str()),("", str()),("", str())], # logs
		[("abs(-42 / 2)", str(21)),("abs(64-2143)", str(-2079)),("abs(-64 * 3 + 423)", str(231))], # absolutes
		[("sqr(2)(64)", str(8)),("sqr(3)((44 * 10 + 1) * 21)", str(21)),("sqr(2)(32)*43", str())]  # roots
	]

	table = [LevelBasic, LevelMedium, LevelHard]

	for level in table:
		for operation in level:
			for i in operation:
				if i[0] == inpt:
					return i[1]

	return 0



def test():
	LevelBasic = [
		[("6 + 3", str(9)),("32 + 54", str(86)),("43 + 23 +  11", str(77))], # addition
		[("6 - 3", str(3)),("18 - 8", str(10)),("1 - 20", str(-19))], # subtraction
		[("5 * 11", str(55)),("102 * 10", str(1020)),("16 * 32", str(512))], # multiplication
		[("15 / 5", str(3)),("9 / 1", str(9)),("121 / 11", str(11))]  # division
	]

	LevelMedium = [
		[("(2 + 6) * 2", str(16)),("(5 * (6 / 2) - 5)", str(10)),("(23 - 24) / 10", str(-0.1))], # bracets
		[("6^2 - 2", str(32)),("7^4 / 5 +  6", str(486.2)),("35^4 - 34^4", str(164289))], # powers
		[("9! / 5", str(72576)),("6! - 5! * 3!", str(0)),("7! / 4! * 5 - 24", str(1024))], # factorials
	]

	LevelHard = [
		[("", str()),("", str()),("", str())], # logs
		[("abs(-42 / 2)", str(21)),("abs(64-2143)", str(-2079)),("abs(-64 * 3 + 423)", str(231))], # absolutes
		[("sqr(2)(64)", str(8)),("sqr(3)((44 * 10 + 1) * 21)", str(21)),("sqr(2)(32)*43", str())]  # roots
	]


	print("levelBasic: ")
	completed = 0
	total = 0
	for operation in LevelBasic:
		for i in operation:
			temp = GPTcalculator(i[0])
			if temp == i[1]:
				completed += 1
			else:
				print("on " + i[0] + " got: " + str(temp) + " expected: " +str(i[1]) )
			total += 1
	print("passed: " + str(completed) + "/" + str(total) + "\n")

	print("level Medium: ")
	completed = 0
	total = 0
	for operation in LevelMedium:
		for i in operation:
			temp = GPTcalculator(i[0])
			if temp == i[1]:
				completed += 1
			else:
				print("on " + i[0] + " got: " + str(temp) + " expected: " +str(i[1]) )
			total += 1
	print("passed: " + str(completed) + "/" + str(total) + "\n")

	print("level Hard: ")
	completed = 0
	total = 0
	for operation in LevelHard:
		for i in operation:
			temp = GPTcalculator(i[0])
			if temp == i[1]:
				completed += 1
			else:
				print("on " + i[0] + " got: " + str(temp) + " expected: " +str(i[1]) )
			total += 1
	print("passed: " + str(completed) + "/" + str(total) + "\n")

	






if __name__ == "__main__":
	test()












