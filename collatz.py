import sys

number = int(sys.argv[1])

def collatz(number):
	if number%2 == 0:
		print(number // 2)
		return number//2
	else:
		print(3*number + 1)
		return 3*number+1

def something(number):
	while number > 1:
		number = collatz(number)

something(number)


