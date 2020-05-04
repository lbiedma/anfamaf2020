def devolver_algo(numero):
    assert numero > 0, "El numero no es mayor que cero."
    
    print(numero)
    
def devolver_algo_v2(numero):
    output = None
    
    if type(numero) != int:
        print("Ingrese un numero entero.")

    elif numero <= 0:
        print("el numero es menor o igual que cero")
                
    else:
        output = numero
        
    return output
