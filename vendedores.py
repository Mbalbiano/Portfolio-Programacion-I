import json #temporal para hacer pruebas, ya que se supone que esto lo ejecutas desde el main y ahi importa la libreria

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
    
def pedir_mes():
    while mes == None:
        try:
            mes = int(input("Ingrese el mes al que corresponden los datos del vendedor (1-12): "))
            if not 1 <= mes <= 12:
                raise ValueError
            return mes - 1  # posición en la lista
        except ValueError:
            print("Error, ingrese un mes válido")
            mes = None

def cargar_datos():
    try:
        with open("vendedores.json", "r", encoding="UTF-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [[] for _ in range(12)]  # una lista vacía por mes

def agregar_vendedor():
    while legajo != -1:  #revisar condicion de corte
        print(f"A continuacion se solicitaran los datos de los vendedores. \n Para salir, ingrese -1 en el numero de legajo")
        legajo = validar_legajo()
        sueldo = validar_sueldo()
        ventas, comision = validar_ventas_mensuales()
    #ahora se viene lo jodido..
        mes = pedir_mes()
        datos = {
            "legajo": legajo,
            "sueldo":sueldo,
            "ventas":ventas,
            "comision":comision
        }

        matriz = cargar_datos()
        matriz[mes].append(datos)

        json_str = json.dumps(datos)
        with open ("vendedores.json","w",encoding="UTF-8") as file: #me parece que es muy ineficiente esta forma de hacer las cosas en terminos de memoria
            json.dump(json_str,file, ensure_ascii=False, indent=4)  #mas si el archivo fuera mas grande
    
        
    

