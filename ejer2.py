class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.calcular_promedio():.2f}")

#ejem
estudiante1 = Estudiante("Joao Felix", [4.5, 1.8, 4.2, 5.0])
estudiante1.mostrar_info()
