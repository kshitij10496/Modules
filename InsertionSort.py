import timeit

def InsertionSort(a):

	l = len(a)
	print "Before sorting :", a
	for i in xrange(2,l):
		key = a[i]
		j = i - 1
		while j >= 0 and a[j]> key:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key
	print "After sorting :", a

def input_list():

	print "Enter a sequence of numbers: "
	try:
		A = raw_input().split() 
	except ValueError:
		print "Wrong Input"
	return [int(n) for n in A if n.isdigit()]

def main():

	numbers = input_list()
	InsertionSort(numbers)

start = timeit.default_timer()
main()
stop = timeit.default_timer()
print "Execution time :", stop - start, "seconds"
