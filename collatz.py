import sys



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




print("Please enter a number")

try:
    number = int(input())
    something(number)
    
except:
    print("Please enter a valid integer")




