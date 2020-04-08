def ripf(fun, x0, err, mit):
	f = fun(x0)
	hx = [x0]

	k = 0
	while k < mit:
		xn = f

		if abs(xn-x0) < err:
			print('El paso es pequeño')
			return hx

		x0 = xn
		f = fun(x0)
		hx.append(x0)

		k+=1
	return hx