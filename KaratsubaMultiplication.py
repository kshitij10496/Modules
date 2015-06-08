def Karatsuba(num1,num2,base=10) :
	if num1 < base or num2 < base :
		return num1*num2

	b1 = max(size(num1,base),size(num2,base))
	b2 = b1/2

	high1 = num1 / (base ** b2)
	high2 = num2 / (base ** b2)
	low1 = num1 % (base ** b2)
	low2 = num1 % (base ** b2)

	m1 = Karatsuba(low1, low2, base)
	m2 = Karatsuba(low1 + high1, low2 + high2)
	m3 = Karatsuba(high1, high2)

	multiplication = m3 * (base ** b1) + (m2 - m1 - m3) * base ** m2 + m1

	return multiplication

def size(num,base):
	n = num
	count = 0
	while n > 0:
		count += 1
		n = n/base

	return count

def main():
	print "Enter a number :"
	number1 = input()
	print "Enter another number :"
	number2 = input()
	print "Enter base:"
	base = input()
	print Karatsuba(number1, number2, base)

main()
