class Heap(object):
	def __init__(self,index):
		self.index = index
	def parent(self):
		if self.index % 2 == 0:
			return self.index/2 - 1
		else:
			return self.index/2

	def leftchild(self):
		return 2*self.index + 1

	def rightchild(self):
		return 2*self.index + 2

def Max_Heapify(A,i): 
	heap_object = Heap(i)

	l = heap_object.leftchild()
	r = heap_object.rightchild()
	if l < len(A) and r < len(A) :
		
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

