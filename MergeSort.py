def Merge(A,p,q,r):

	L= []
	R = []
	for i in xrange(p,q):
		L.append(A[i])
	for j in xrange(q, r):
		R.append(A[j])

	i = 0
	j = 0
	k = p

	while k < r:
		if i < len(L) :    
			if j < len(R) :
				if L[i] < R[j]:
					A[k] = L[i]
					i += 1
				else:
					A[k] = R[j]
					j += 1
				k += 1
			else:
				for x in xrange(i,len(L)):
					A[k] = L[x]
					k += 1
				break
		else:
			if j < len(R):
				for x in xrange(j,len(R)):
					A[k] = R[x]
					k += 1	
				break
			else:
				break


def MergeSort(A,p,r):
    q = (p+r)/2
    if p == q:  # r -> q
		     return A[p]
		MergeSort(A,p,q)
		MergeSort(A,q,r)   
		Merge(A,p,q,r)

def main():
    print "Enter a sequence:"
    try:
        a = raw_input().split()
    except ValueError:
        print "Value Error"

	A = map(int, a)
	print A
	MergeSort(A,0,len(a))

main()
