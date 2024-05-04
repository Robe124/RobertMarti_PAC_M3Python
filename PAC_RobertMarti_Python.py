import os
diccionario = {}

#! MENU INICIAL
def menu():
    os.system('cls')
    print("-------------------------------------")
    print("DICCIONARIO PALABRAS I DESCRIPCIONES")
    print("-------------------------------------")

    print("Escoja una de las opciones")
    print("[1] Agregar palabra")
    print("[2] Agregar descripcion")
    print("[3] Mostrar diccionario")
    opcion_menu = int(input("Elije una opcion [1-4]: "))
    if opcion_menu == 1:
        input_palabra()

    elif opcion_menu == 2:
        input_descripcion()
    
    elif opcion_menu == 3:
        ver_diccionario()


#! INPUT PARAULA
def input_palabra():
    os.system('cls')
    print("-------------------------------------")
    print("DICCIONARIO PALABRAS Y DESCRIPCIONES")
    print("-------------------------------------")
    
    print("[1] Agregar palabra")
    print("[2] Salir")
    
    Opcion_MenuAgregarParaula = input("Elija una opcion[1-2]: ")

    if Opcion_MenuAgregarParaula == 1:
        for palabra, descripcion in diccionario.items():
            print(f"Palabra: {palabra} - Descripción: {descripcion}")
            palabra = input("Ingrese la palabra: ")
            
            if palabra in diccionario:
                print("La palabra ya existe en el diccionario.")
            
            else:
                diccionario[palabra] = ""   
    
    elif Opcion_MenuAgregarParaula == 2:
            menu()

    return Opcion_MenuAgregarParaula




def input_descripcion():
    os.system('cls')
    print("-------------------------------------")
    print("DICCIONARIO PALABRAS Y DESCRIPCIONES")
    print("-------------------------------------")

    print("[1] Agregar Descripcion")
    print("[2] Salir")
    
    Opcion_MenuAgregarParaula = input("Elija una opcion[1-2]: ")

    if Opcion_MenuAgregarParaula == 1:
        if not diccionario:
            print("No hay palabras para agregar descripción. Primero agregue una palabra.")
            menu()
            return
        
        if palabra not in diccionario:
            print("La palabra no existe en el diccionario.")
            menu()
            return
    
        palabra = input("Inserte la palabra a la que desea agregar una descripción: ")

        descripcion = input("Inserte la descripción de la palabra anterior: ")
        diccionario[palabra] = descripcion  # Asigna la descripción a la palabra correspondiente
 
    elif Opcion_MenuAgregarParaula == 2:
        menu()
       
    
    return Opcion_MenuAgregarParaula




def ver_diccionario():
    os.system('cls')
    print("-------------------------------------")
    print("DICCIONARIO PALABRAS Y DESCRIPCIONES")
    print("-------------------------------------")

    print("[1] Ver diccionario")
    print("[2] Salir")

    opciones_segundoMenu = input("Que opcion vas a elegir: ")

    if opciones_segundoMenu == 1:
        
        if diccionario:
            print("Palabras y descripciones guardadas:")
            for palabra, descripcion in diccionario.items():
                print(f"Palabra: {palabra} - Descripción: {descripcion}")
        else:
            print("El diccionario está vacío.")
    

    elif opciones_segundoMenu == 2:
        menu()

    return opciones_segundoMenu

menu()

 

  