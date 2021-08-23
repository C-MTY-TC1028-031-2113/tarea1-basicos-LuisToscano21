def main():
def funciones_matematicas():
    from math import sqrt
    a = 4
    b = 5
    oper1 = 2.75 + 4.66 - 3.20 + 5.50
    print(oper1)
    oper2 = 2*sqrt(35**2) + 4*sqrt(36**3) - 6*sqrt(49**2)
    print(oper2)
    oper3 = (a**3 + 2*b**2) / (4*a)
    print(oper3)
    oper4 = (2*(a+b)**2 + 4*(a-b)**2) / (a*b**2)
    print(oper4)
    oper5 = sqrt((a+b)**2 + 2**(a+b)) / (2*a + 2*b)**2
    print(round(oper5, 4))
    


funciones_matematicas()  
    pass
    
   



if __name__ == '__main__':
    main()
