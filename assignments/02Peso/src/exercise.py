def main():
    #escribe tu código abajo de esta línea
def peso_final():
    peso = float(input("Dame el peso inicial: "))
    pesoo = float(input("Dame la meta de peso: "))
    meses = int(input("Dame los meses: "))
    meta = (peso - pesoo)/meses
    print("el peso que debe bajar al mes es: " + str(meta))
    
peso_final()    
    pass



if __name__ == '__main__':
    main()
