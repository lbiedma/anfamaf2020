def  rnewton(fun, x0, err, mit):
	f, df = fun(x0)

	hx, hf = [x0], [f]

	if df == 0:
		print('La derivada es nula en tal punto')
		return hx, hf

	
	k = 0
	while (abs(f) >=err) and (k < mit):
	
		xn = x0 - f/df
	
		if abs( (xn - x0)/xn ) < err:
			print('El paso es muy pequeño')
			return hx, hf

		x0 = xn
		f, df = fun(x0)
		hx.append(x0)
		hf.append(f)

	k +=1
	return hx, hf