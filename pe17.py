# this program solves the project euler
# problem number 17

position = {
	0: "one",
	1: "ten",
	2: "hundred",
	3: "thousand"
}

number = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine"
}

specialnum = {
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",

	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety"
}

def numToWord(n):
	s = str(n)
	numword = ""
	pos = len(s)
	for i in range(0, len(s)):
		d = int(s[i])
		pos -= 1 
		if d == 1 and pos == 1:
			numword = (numword + "and " + specialnum[int(s[-2:])]) if numword != "" else specialnum[int(s)]
			break
		elif d > 1 and pos == 1:
			numword = (numword + "and " + specialnum[d*10]) if numword != "" else specialnum[d*10] 
		elif d > 0 and pos > 1:
			numword = numword + number[d] + " " + position[pos] + " "
		elif d > 0 and pos == 0:
			if numword == "":
				numword = number[d]
			elif int(s[-2]) == 0 and numword != "":
				numword = numword + "and " + number[d]
			elif int(s[-2]) != 0:
				numword = numword + "-" + number[d]
			else:
				numword = number[d]
			# numword = (numword + "-" + number[d]) if s != "" else number[d] 
	return numword

if __name__ == "__main__":
	while True:
		n = raw_input("enter an integer: ")
		try:
			n = int(n)
			if n > 10000:
				print "num should be less than 1000.",
				raise ValueError
			print numToWord(n)
			break
		except ValueError:
			print "invalid input"
