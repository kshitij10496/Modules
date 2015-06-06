from random import randint

def Partition(A,p,r):

	x = A[r]
	i = p - 1

	for j in xrange(p,r):
    	if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	
	A[i + 1] ,A[r] = A[r], A[i+1]   

	return i       


def QuickSort(A,p,r):
	
	if p < r:
		q = RandomPartition(A,p,r)
		QuickSort(A,p,q)
		QuickSort(A,q+1,r)

def RandomPartition(A,p,r):
	
	i = randint(p,r)
	A[r], A[i] = A[i],A[r]
	return Partition (A,p,r)

def main():
	
	print "Enter a sequene of numbers:"
	num = map(int, raw_input().split())
	QuickSort(num,0,len(num)-1)
	print num

main()