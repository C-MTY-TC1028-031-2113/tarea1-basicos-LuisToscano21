def main():
    #escribe tu código abajo de esta línea
    def promedio_calificaciones():
        uno = float(input("calificacion de la primera materia: "))
        dos = float(input("calificación de la segunda materia: "))
        tres = float(input("calificación de la tercera materia: "))
        cuatro = float(input("calificación de la cuarta materia: "))
        promedio = (uno + dos + tres + cuatro)/4
        print("El promedio de las calificaciones es: " + str(promedio))
    
promedio_calificaciones()
    pass


if __name__ == '__main__':
    main()
