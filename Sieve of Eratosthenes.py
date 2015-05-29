def prime_factors(n):
	i=2
	l = range(2,n)

	while i**2<n:
		for j in xrange(2*i,n+1,i):
			try:
				l.remove(j)
			except ValueError:
				pass
		i+=1
	print max(l)

prime_factors(input())
