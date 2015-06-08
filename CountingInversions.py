
def CountInversions(A,n):

	if n == 1 :
		return 0
	else:
		left_half = A[:n/2]
		right_half = A[n/2:]

		count_left = CountInversions(left_half,n/2)
		count_right = CountInversions(right_half,n-n/2)
		count_split = CountSplitInversions(left_half,right_half,n/2.0)
	return count_left + count_right + count_split

def CountSplitInversions(left_half, right_half, n):
	i, j, k,count = 0, 0, 0 , 0
	limit = int(n*2)
	output = []
	while k <= limit and i < int(n) and j <= int(n):
		if left_half[i] < right_half[j]:
			output.append(left_half[i])
			i += 1
		else:
			output.append(right_half[j])
			j += 1
			count += int(n) - 1 - i
	return count

def main():
	print "Enter numbers:"
	numbers = map(int,raw_input().split())
	print CountInversions(numbers, len(numbers))

main()
