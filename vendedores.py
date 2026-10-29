print ("hola tu codigo funca")

def validar_legajo ():
    while lu == None:
        try:    
            lu = int(input("Ingrese el numero de legajo del vendedor: "))
            if lu < 0:
                raise ValueError
        except ValueError:
            print ("Error, ingrese un legajo valido")
            lu = None
    return lu

def agregar_vendedor():
    legajo = validar_legajo()
