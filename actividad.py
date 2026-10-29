#Programa para calcular la comision mensaul de sus vendedores

def ingreso_vendedores ():
    vendedores = []
    legajo = 0
    while legajo != -1:
        try:
            legajo = int(input("Ingrese el numero de legajo"))
            
        except ValueError:
            print ("los datos ingresados no son validos, proba de vuelta")