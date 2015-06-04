class Heap(object):
	def __init__(self,index,length):
		self.index = index
		self.length = length
	def parent(self):
		if self.index % 2 == 0:
			return self.index/2 - 1
		else:
			return self.index/2

	def leftchild(self):
		return 2*self.index + 1

	def rightchild(self):
		return 2*self.index + 2

	
def heapsize(A):
	lenth = len(A)
	
def Max_Heapify(A,i): 
	heap_object = Heap(i)

	l = heap_object.leftchild()
	r = heap_object.rightchild()
	heap_size = heapsize(A)

	if l < heap_size  and r < heap_size :
		
		maximum = max(A[i],A[l],A[r])
		
		if maximum == A[i]:
			largest = i
		elif maximum == A[l]:
			largest = l
		else:
			largest = r
		print largest

		if largest != i :
			A[largest], A[i] = A[i], A[largest]
			Max_Heapify(A,largest)
	return A

def Build_Max_Heap(A):
	n = len(A)
	
	for i in xrange(n/2-1,-1,-1):
		Max_Heapify(A,i)

def HeapSort(A):
	Build_Max_Heap(A)
	for i in xrange(n-1,0,-1):
		A[0],A[i] = A[i],A[0]
		Max_Heapify(A,0)

def main():
	print "Enter a list of numbers :"
	a = map(int , raw_input().split())
	HeapSort(a)
	print a

main()



