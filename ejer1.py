class Empleado:
    def __init__(self, nombre, salario_base, bonificaciones=0):
        self.nombre = nombre
        self.salario_base = salario_base
        self.bonificaciones = bonificaciones

    def calcular_salario(self):
        return self.salario_base + self.bonificaciones

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Salario Base: ${self.salario_base}")
        print(f"Bonificaciones: ${self.bonificaciones}")
        print(f"Salario Total: ${self.calcular_salario()}")

#ejem
empleado1 = Empleado("Messi Ronaldo", 1250000, 200000)
empleado1.mostrar_info()
