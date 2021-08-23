def main():
    #escribe tu código abajo de esta línea
def cuenta_bancaria():
    saldoma = float(input("Dame el saldo del mes anterior: "))
    ingresos = float(input("Dame los ingresos: "))
    egresos = float(input("Dame los egresos: "))
    cheques = int(input("Dame el número de cheques: "))
    saldofi = (saldoma + ingresos) - ((cheques*13) + egresos)
    saldof = saldofi - (saldofi*.075)
    print("El saldo final de la cuenta este mes es de: " + str(saldof))
    
cuenta_bancaria()        
    pass



if __name__ == '__main__':
    main()
