
def pascal(filas):
    error = True
    while error == True:
        try:

            ele = 0
            divsiete = 0
            print('Por favor espere...')

            #Recorre cada fila
            for i in range(0, filas):
                num = 1
                #busca cada elemento de cada fila y el numero de elementos de la fila no supera el numero de fila
                for j in range(0, i + 1):
                    '''print('%d' % num)'''
                    #hace conteo de elementos totales
                    ele = ele + 1
                    if num % 7 == 0:
                        #hace conteo de numeros divisibles por 7
                        divsiete = divsiete + 1
                    #busca el siguiente numero de la fila
                    num = num * (i - j) / (j + 1)
                '''print("\n")'''
            error = False
            print('Número de elementos : %d' % ele)
            print('Número de divisores de 7: %d' % divsiete)
            nodiv = ele - divsiete
            print('Número de no divisores de 7: %d' % nodiv)
        except ValueError:
            print("Error! Ingrese unicamente numeros , intente de nuevo.")
            error = True

pascal(100)