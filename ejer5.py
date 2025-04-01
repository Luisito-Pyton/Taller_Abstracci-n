class Menu:
    def __init__(self):
        self.opciones = {
            "1": "Ver Camisetas",
            "2": "Comprar",
            "3": "Salir"
        }

    def mostrar_menu(self):
        for clave, valor in self.opciones.items():
            print(f"{clave}. {valor}")

    def ejecutar_opcion(self, opcion):
        if opcion in self.opciones:
            print(f"Ejecutando la opción: {self.opciones[opcion]}")
        else:
            print("Opción invalida")
#ejem
menu1 = Menu()
menu1.mostrar_menu()
menu1.ejecutar_opcion("3")
