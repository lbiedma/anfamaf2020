def error_cos(I,n):
	from math import factorial
	a = I[0]
	b = I[1]
	error = abs(b-a)**n / factorial(n)
	return error
