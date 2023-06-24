from funciones import *
print('=='*45)
print ('La Tiendita le ofrece los siguientes productos: ')
print('=='*45)

for articulo in articulos:
    print (articulos)
terminar = True
while terminar == True:
    carrito = CarritoCompra()
    print ('Menú')
    print ('Visualizar lista de productos con su descripcion --> Opcion 1 \n Visualizar productos con breve descripcion --> Opcion 2 \n Buscar a traves del codigo el producto deseado --> Opcion3 \n Confirmar Compra --> Opcion 4 \n Terminar Compra --> Opcion 5 \n Salir --> Opcion 6 ')

    try:
        opcion = int(input('Elegir una opcion: '))

        if opcion == 1:
            print('Opcion 1')
            opcion_uno()

        elif opcion == 2:
            print('Opcion 2')
            opcion_dos()

        elif opcion == 3:
            opcion_tres()

        elif opcion == 4:
            opcion_cuatro()

        elif opcion == 5:
            print('Terminar Compra')
            opcion_cinco ()

        elif opcion == 6:
            print('Salir del Menu')
            terminar = False

        else:
            print('no ingreso ninguna opcion disponible')
        continue

    except ValueError:
        print('Ingresar una opcion disponible, Por favor')

        continue
    else:
        break

