def area(base,altura):
    return base*altura

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))

    print("El área del rectángulo es:",area(b,a))

if __name__=='__main__':
    main()
