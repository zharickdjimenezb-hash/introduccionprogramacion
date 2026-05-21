LIMITE_AFORO = 20
lista_asistentes = []

def registrar_asistente():
    if len(lista_asistentes) >= LIMITE_AFORO:
        print("\n[ERROR] ¡Cupo lleno! No pueden ingresar más personas.")
        return

    nombre = input("\nIngrese el nombre completo del asistente: ").strip()

    if nombre == "":
        print("[ERROR] El nombre no puede estar vacío.")
        return

    if nombre in lista_asistentes:
        print(f"[ERROR] '{nombre}' ya está registrado en el evento.")
    else:
        lista_asistentes.append(nombre)
        print(f"¡Éxito! '{nombre}' ha sido agregado a la lista.")

def mostrar_lista():
    if len(lista_asistentes) == 0:
        print("\nLa lista está vacía. No hay nadie en el evento aún.")
    else:
        print("\n--- LISTA DE ASISTENTES ---")
        for posicion, persona in enumerate(lista_asistentes, start=1):
            print(f"{posicion}. {persona}")

def corregir_nombre():
    mostrar_lista()
    if len(lista_asistentes) == 0:
        return

    try:
        numero = int(input("\nIngrese el número de la persona que desea corregir: "))
        indice = numero - 1

        if 0 <= indice < len(lista_asistentes):
            nuevo_nombre = input("Ingrese el nombre correcto: ").strip()
            if nuevo_nombre != "":
                lista_asistentes[indice] = nuevo_nombre
                print("¡Nombre corregido con éxito!")
            else:
                print("[ERROR] El nombre no puede estar vacío.")
        else:
            print("[ERROR] Ese número de asistente no existe in la lista.")
            
    except ValueError:
        print("[ERROR] Por favor, ingrese un número válido.")

def retirar_asistente():
    mostrar_lista()
    if len(lista_asistentes) == 0:
        return

    try:
        numero = int(input("\nIngrese el número de la persona que se va del evento: "))
        indice = numero - 1

        if 0 <= indice < len(lista_asistentes):
            persona_eliminada = lista_asistentes.pop(indice)
            print(f"'{persona_eliminada}' ha sido retirada de la lista.")
        else:
            print("[ERROR] Ese número de asistente no existe.")
            
    except ValueError:
        print("[ERROR] Por favor, ingrese un número válido.")

def mostrar_estadisticas():
    actuales = len(lista_asistentes)
    cupos_libres = LIMITE_AFORO - actuales
    print("\n--- ESTADÍSTICAS DEL EVENTO ---")
    print(f"Asistentes actuales dentro: {actuales}")
    print(f"Cupos disponibles: {cupos_libres} / {LIMITE_AFORO}")

def menu_principal():
    while True:
        print("\n=================================")
        print("  SISTEMA DE GESTIÓN VIP - CONSOLA ")
        print("=================================")
        print("1. Registrar asistente")
        print("2. Ver lista de asistentes")
        print("3. Corregir nombre")
        print("4. Retirar asistente")
        print("5. Ver estadísticas de aforo")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()

        if opcion == "1":
            registrar_asistente()
        elif opcion == "2":
            mostrar_lista()
        elif opcion == "3":
            corregir_nombre()
        elif opcion == "4":
            retirar_asistente()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            print("\nCerrando el sistema... ¡Buen evento!")
            break
        else:
            print("\n[ERROR] Opción no válida. Intente de nuevo.")

menu_principal()