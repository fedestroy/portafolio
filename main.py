from agenda import Agenda

def menu():
    print("""
    =============================
        📞 AGENDA TELEFÓNICA
    =============================
    1. Agregar contacto
    2. Mostrar contactos
    3. Buscar contacto
    4. Modificar contacto
    5. Eliminar contacto
    6. Salir
    """)

def main():
    agenda = Agenda()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agenda.agregar_contacto(nombre, telefono, email)

        elif opcion == "2":
            agenda.mostrar_contactos()

        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            agenda.buscar_contacto(nombre)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a modificar: ")
            agenda.modificar_contacto(nombre)

        elif opcion == "5":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == "6":
            print("👋 Saliendo de la agenda...")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()