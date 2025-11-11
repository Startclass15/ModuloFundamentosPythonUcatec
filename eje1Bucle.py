#COMBINACION DE BUCLES CON CONDICIONALES
#BUCLE INFINITO WHILE TRUE
#ROMPER BUCLES: BREAK

#menu de opciones
while True:
    print("Opciones")
    print("1. Opcion1")
    print("2. Opcion2")
    print("3. Opcion3")
    print("4. Opcion4")
    print("5. Salir") # romper el bucle
    opcion=int(input("Ingrese la opcion que desea realizar. "))
    if opcion==1:
        print("Eligio la opcion 1")
    elif opcion==2:
        print("Eligio la opcion 2")
    elif opcion==3:
        print("Eligio la opcion 3")
    elif opcion==4:
        print("Eligio la opcion 4")
    elif opcion==5:
        print("Gracias hasta pronto...")
        break
    else:
        print("Error opcion invalida...")