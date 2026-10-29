#Todo programa arranca por algun lado. yo arranco por el menu!
import vendedores, ventas, exportar_csv

def main_menu():
    print("""
    ____                _     _                                
    / ___|___  _ __ ___ (_)___(_) ___  _ __    _ __   ___  _ __ 
    | |   / _ \| '_ ` _ \| / __| |/ _ \| '_ \  | '_ \ / _ \| '__|
    | |__| (_) | | | | | | \__ \ | (_) | | | | | |_) | (_) | |   
    \____\___/|_| |_| |_|_|___/_|\___/|_| |_| | .__/ \___/|_|   
    __   _____ _ __ | |_ __ _ ___              |_|               
    \ \ / / _ \ '_ \| __/ _` / __|                               
    \ V /  __/ | | | || (_| \__ \                               
    \_/ \___|_| |_|\__\__,_|___/                               
    
    Seleccione una opcion:
    1) Gestion de vendedores
    2) Generar reporte de ventas
    3) Exportar datos a .csv
    """)

    opcion = 0
    while opcion != 1 and opcion != 2 and opcion != 3: 
        try:
            opcion = int(input(f"Ingrese una opcion (1,2,3): ")) 
        except ValueError:
            print ("Error, ingrese una opcion valida")

    if opcion == 1:
        vendedores()
    elif opcion == 2:
        ventas()
    elif opcion == 3:
        exportar_csv() 

main_menu()