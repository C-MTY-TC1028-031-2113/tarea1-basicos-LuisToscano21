def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
def slope_coordenadas():
    cx1 = float(input("Dame la coordenada x1: "))
    cx2 = float(input("Dame la coordenada x2: "))
    cy1 = float(input("Dame la coordenada y1: "))
    cy2 = float(input("Dame la coordenada y2: "))
    pendiente = (cy2 -cy1) / (cx2 - cx1)
    print("La pendiente de la recta es igual a: " + str(pendiente))
    
slope_coordenadas()      

    pass



if __name__ == '__main__':
    main()
