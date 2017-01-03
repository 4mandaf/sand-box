# evenFibonacci.py

# Problem 2 of ProjectEuler.net
# Each new term in the Fibonacci sequence is generated by 
# adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 		1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.

# Input the limit of the Fibonacci numbers to sum (4 million for the problem).
limit = int(input('Sum even Fibonacci numbers less than the following number:'))

# Initial values for the n and n+1 values of the Fibinocci sequence.
first = 1
second = 2

# Variable to track the sum of the even Fibonacci numbers.
answer = 2

# Variable to track the n+2 value of the Fib sequence.
new = first + second

# While the n+2 value of the Fib sequence is less than 4 million
# track the sum of the even Fib numbers.
while new < limit:
	if new % 2 == 0:
		answer += new
	first = second
	second = new
	new += first

print(answer)