print ("hola tu codigo funca")

def validar_legajo ():
    while lu == None:
        try:    
            lu = int(input("Ingrese el numero de legajo del vendedor: "))
            if lu < -1:
                raise ValueError
        except ValueError:
            print ("Error, ingrese un legajo valido")
            lu = None
    return lu

def validar_sueldo():
    while sueldo == None:
        try:
            sueldo = int(input("Ingrese el sueldo del vendedor: "))
            if sueldo < 0:
                raise ValueError
        except ValueError:
            print ("Error, ingrese un sueldo valido")
            sueldo = None
    return sueldo

def validar_ventas_mensuales():
    while ventas == None: #Validamos que las ventas mensuales sean un numero mayor a -1
        try:
            ventas = int(input("Ingrese las ventas del vendedor: "))
            if ventas < -1:
                raise ValueError
        except ValueError:
            print ("Error, ingrese un valo de ventas valido")
            ventas = None

    #calculamos la comision
    comision = lambda ventas: 120000 + 40000 * (ventas - 9) if ventas >= 10 else 120000 if ventas >= 5 else 0
    return ventas, comision 
    


def agregar_vendedor():
    while legajo != -1:
        print(f"A continuacion se solicitaran los datos de los vendedores. \n Para salir, ingrese -1 en el numero de legajo")
        legajo = validar_legajo()
        sueldo = validar_sueldo()
        ventas, comision = validar_ventas_mensuales()

