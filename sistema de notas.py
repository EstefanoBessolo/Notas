print("¡Bienvenido al sistema de notas!")

notas = ["1","2","3","4","5","6","7"]
opcion = 0

while opcion != 5:
    print("\n=== MENU PRINCIPAL ===") 
    print("1. Registrar una nota")
    print("2. Mostrar todas la notas")
    print("3. Mostrar promedio de curso")
    print("4. Mostrar nota mas alta y baja")
    print("5. Salir")
    
    try:
        opcion = int(input("Ingrese una opcion: "))
        
        if opcion == 1:
            print("\n=== INGRESE NOTAS ===")
            nuevas_notas = float(input("Ingrese una nota:"))
            notas.append(nuevas_notas)
            
        elif opcion == 2:
            print("Mostrar todos las notas:", notas)
                       
         
        elif opcion == 3:
            print("Mostrar el promedio del curso:")
           
            
            
        elif opcion == 4:
            print("Mostrar notas altas:", nuevas_notas)
            print("Mostrar notas bajas:", nuevas_notas)
            

        elif opcion == 5:
            print("\n=== FIN DEL PROGRAMA ===")
            print("Gracias por utilizar nuestro software, hasta la proxima.")   
              
            
        else:
            print("Error: opcion incorrecta.")
            
    except ValueError:
        print("Error: debe ingresar un valor numerico valido.")
    except:
        print("Error inesperado.")
        

