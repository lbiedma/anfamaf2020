def  rsteff(fun, x0, err, mit):
	f , _ = fun(x0)
	
	f_ , _ = fun(x0 + f)
	hx, hf = [x0], [f]
	
	k = 0
	while (abs(f) >= err) and (k <mit):
		xn = x0 - f**2/(f_ - f)
		
		if abs( (xn-x0)/xn ) < err:
			print('El paso es muy pequeño')
			return hx, hf

		x0 = xn
		f, _ = fun(x0)
		f_, _ = fun(x0 + f)
		hx.append(x0)
		hf.append(f)

		k = k+1
	return hx, hf