class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    def autenticar(self, contrasena_ingresada):
        return self.contrasena == contrasena_ingresada

    def mostrar_info(self):
        print(f"Usuario: {self.nombre}")

#ejem
usuario1 = Usuario("papu", "cr7goat")
print("Autenticación exitosaa" if usuario1.autenticar("cr7goat") else "Autenticación fallida")
