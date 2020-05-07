def inewton(x,y,z):
	#import pdb
	#pdb.set_trace()
	if len(x) != len(y):
		print("Error: los tamaños de x e y no coinciden")
		return None
	n = len(x)-1
	m = len(z)

	# c = [dif_div(x,y,0,k) for k in range(n+1)]
	c = [[y[i]] for i in range(n+1)]
	for j in range(1,n+1):
		for i in range(n-j+1):
			c[i] = c[i] + [(c[i+1][j-1] - c[i][j-1]) / (x[i+j] - x[i])]
	c = [c[0][k] for k in range(n+1)]
	w = [horn_newt(c,x[:-1],z[i]) for i in range(m)]
	return w

def horn_newt(c_orig,x,zi):
	c = c_orig.copy()
	wi = c.pop(-1)
	while c:
		wi = c.pop(-1)+(zi - x.pop(-1))*wi
	return wi

# c_0 + c_1 (z - x_0) + c_2 * (z - x_0) * (z - x_1) + ...
# c_0 + (z - x_0) [ c_1 + c_2 * (z - x_1) + ... ]
# c_0 + (z - x_0) [ c_1 + c_2 * (z - x_1) + c_3 * (z - x_1) * (z - x_2) + ... ]
# c_0 + (z - x_0) [ c_1 + (z - x_1) * [c_2 + c_3 * (z - x_2) + ...  ] ]

#  (z - x_{k-2}) * [ c_{k-1} + c_k * (z - x_{k-1}) ]
#  (z - x_{k-2}) * [ c_{k-1} + (z - x_{k-1}) * [c_k] ]
