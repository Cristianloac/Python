
def pitagoras():
    try:
        valor = 1000
        for c in range(2, valor):
            for a in range(1, c):
                #a < c
                # se valida que a + b + c  = 1000
                b = valor - c - a

                #teorema de pitágoras
                if a**2 + b**2 == c**2:
                    print("a = %d, b = %d, c = %d" %(a,b,c))
                    print ("a * b * c = %d" %(a*b*c))
                    print("a^2=",a**2," b^2=",b**2," c^2=",c**2, "a^2+b^2=",((a**2)+(b**2)))
                    return
    except ValueError:
        print("Error!")
pitagoras()


