contactos = {}

while True:
    print("\n--- REGISTRO DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el número de teléfono: ")

        contactos[nombre] = telefono

        print("Contacto agregado correctamente.")

    elif opcion == "2":
        print("\n--- CONTACTOS REGISTRADOS ---")

        if len(contactos) == 0:
            print("No hay contactos registrados.")
        else:
            for nombre, telefono in contactos.items():
                print(nombre, ":", telefono)

    elif opcion == "3":
        nombre = input("Ingrese el nombre que desea buscar: ")

        if nombre in contactos:
            print("Teléfono:", contactos[nombre])
        else:
            print("El contacto no existe.")

    elif opcion == "4":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")