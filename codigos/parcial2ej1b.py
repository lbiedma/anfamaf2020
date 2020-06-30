def trapecio_adaptativo(particion, evaluacion):
    n = len(particion)
    
    integral = 0.0
    for paso in range(n-1):
        integral = integral + (evaluacion[paso] + evaluacion[paso + 1]) * (particion[paso + 1] - particion[paso]) / 2
        
    return integral

