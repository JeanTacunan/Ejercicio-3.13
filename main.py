class Evaluacion:
    def __init__(self, calificacion: float, asistencia: int):
        self.calificacion = calificacion
        self.asistencia = asistencia

    def evaluar(self) -> str:
        if self.calificacion > 9.0 and self.asistencia == 1:
            return "La calificación es A Excelente con Mención Honorífica."
        elif self.calificacion > 9.0 and self.asistencia != 1:
            return "La calificación es A Excelente."
        elif self.calificacion > 8.0 and self.asistencia == 1:
            return "La calificación es B Muy bien con mención."
        elif self.calificacion > 8.0 and self.asistencia != 1:
            return "La calificación es B Muy bien."
        elif self.calificacion == 7.5:
            return "La calificación es C Bien."
        else:
            return "La calificación es R Reprobado. Lo siento mucho </3."

def main():
    try:
        calificacion = float(input("Dame una calificación: \n"))
        print('Dame la asistencia: 1 si asistió o 0 si no asistió.')
        asistencia = int(input())

        evaluacion_obj = Evaluacion(calificacion, asistencia)
        resultado = evaluacion_obj.evaluar()
        print(resultado)
    except ValueError:
        print("Por favor, ingrese valores válidos para la calificación y asistencia.")

if __name__ == "__main__":
    main()
