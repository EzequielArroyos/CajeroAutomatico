# Cajero Automatico


saldo_actual = 1000
while True:
    print('<Menu>')
    print('1).Ver saldo disponible')
    print('2).Depositar un monto')
    print('3).Retirar dinero de la caja')
    print('4).salir')

    print()

    opcion = int(input('Elija una Opcion; '))

    if opcion==1:
        print(f'saldo disponible; {saldo_actual}')
    elif opcion==2:
        dinero = int(input('Ingrese el monto que desea depositar:'))
        saldo_actual += dinero
        print(f'Saldo total {saldo_actual}')
    elif opcion==3:
        retiro = int(input('Ingrese el monto que desea retirar; '))
        if retiro>saldo_actual:
            print('no tiene esa cantidad')
        else:
            saldo_actual -= retiro
            print(f'saldo actual; {saldo_actual}')
    elif opcion==4:
        print('Gracias por usar el cajero automatico')
        break
    else:
        print('Se equivoco de opcion')