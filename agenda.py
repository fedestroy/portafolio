import json
import os

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email
        }

class Agenda:
    def __init__(self, archivo="data.json"):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def cargar_contactos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return []

    def guardar_contactos(self):
        with open(self.archivo, "w") as f:
            json.dump(self.contactos, f, indent=4)

    def agregar_contacto(self, nombre, telefono, email):
        nuevo = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo.to_dict())
        self.guardar_contactos()
        print(f"✅ Contacto '{nombre}' agregado correctamente.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("📭 No hay contactos en la agenda.")
        else:
            print("\n📒 Lista de contactos:")
            for i, c in enumerate(self.contactos, 1):
                print(f"{i}. {c['nombre']} | {c['telefono']} | {c['email']}")
            print()

    def buscar_contacto(self, nombre):
        encontrados = [c for c in self.contactos if nombre.lower() in c["nombre"].lower()]
        if encontrados:
            print("\n🔍 Resultados de búsqueda:")
            for c in encontrados:
                print(f"{c['nombre']} | {c['telefono']} | {c['email']}")
        else:
            print("⚠️ No se encontró ningún contacto con ese nombre.")

    def modificar_contacto(self, nombre):
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                print(f"Modificando contacto '{nombre}'")
                c["nombre"] = input("Nuevo nombre: ") or c["nombre"]
                c["telefono"] = input("Nuevo teléfono: ") or c["telefono"]
                c["email"] = input("Nuevo email: ") or c["email"]
                self.guardar_contactos()
                print("✅ Contacto actualizado correctamente.")
                return
        print("⚠️ Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        for c in self.contactos:
            if c["nombre"].lower() == nombre.lower():
                self.contactos.remove(c)
                self.guardar_contactos()
                print(f"🗑️ Contacto '{nombre}' eliminado.")
                return
        print("⚠️ Contacto no encontrado.")