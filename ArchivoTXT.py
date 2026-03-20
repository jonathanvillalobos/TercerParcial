'''
Apertura de archivos 
  open("Archivo,txt", "r")
  
  
modos principales
  
Modo        Descripcion
  r           Leer
  w           Escribir (Sobrescribe)
  a           Agregar
  x           Crear archivo 
  
  
*****  Lecura de archivos
        *archivo.read()
        *archivo.realdile()
        *archivo.readlines()
        
***** Escritura de archivos 



def crear_archivo():
    nombre=input("Nombre del archivo: ")
    with open(nombre,"w") as archivo: #Cuando abre el archivo y dejas de usarlo, lo cierra con el with
       
     print("Archivo creado correctamente")
     
crear_archivo()


'''
def menu():
  
 while True:
   print("\n=•- GESTOR DE ARCHIVOS •.-")
   print("1. Crear archivo")
   print("2. Escribir en archivo")
   print("3. Agregar texto")
   print("4. Leer archivo")
   print("5. Buscar palabra")
   print("6. Salir")
    
   opcion= input("Seleccione una opcion: ")
   
   if opcion == "1":
     crear_archivo()  
   elif opcion == "2":
     escribir_archivo()
   elif opcion == "3":
     agregar_texto()
   elif opcion == "4": 
    leer_archivo()
   elif opcion == "5":
    buscar_palabra()
   elif opcion == "6":
    print("Saliendo del programa...")
    break
   else:
    print("Opcion invalida")
    
    
menu()

 
