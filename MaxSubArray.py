class index(object):

	def __init__(self,low,high,total):
		self.low = low
		self.high = high
		self.total = total
	def printing(self):
		print "Low:",self.low
		print "High:",self.high
		print "Total:",self.total
	
def max_crossing_subarray(A,low,mid,high):
    sum, left_sum = 0, -10000000       # Better limit for left_sum
    left_max = mid
    for i in xrange(mid-1,low-1,-1):
    	sum += A[i]
    	if sum > left_sum :
    		left_sum = sum
    		left_max = i

    sum, right_sum = 0, -10000000      # Better limit for right_sum
    right_max = mid
    for i in xrange(mid,high):
    	sum += A[i]
    	if sum > right_sum:
    		right_sum = sum
    		right_max = i

    total = left_sum + right_sum
    cross_sub = index(left_max,right_max,total)
    return cross_sub

def max_subarray(A,low,high):

	if low >= 0 and high < len(A):
		base = index(low,high,A[low])
		if high == low :
			return base
		else:
			mid = ( high + low )/2
			left = max_subarray(A,low,mid)
			right = max_subarray(A,mid+1,high)
			cross = max_crossing_subarray(A,low,mid,high)

			if left.total >= right.total and left.total >= cross.total:
				return left
			elif right.total >= left.total and right.total >= cross.total:
				return right
			else:
				return cross

def main():

	print "Enter a sequence:"
	A = map(int , raw_input().split())
	result = max_subarray(A,0,len(A))
	

main()