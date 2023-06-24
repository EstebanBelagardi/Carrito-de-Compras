from datetime import date
from datetime import datetime

#Creando la clase para los productos.
class Articulos(object):
    def __init__(self, codigo, nombre, marca,  stock, precio, color, detalle):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca        
        self.stock = stock
        self.precio = precio
        self.color = color
        self.detalle = detalle

    def info_ampliada(self):
        return f'Los articulos que tenemos disponibles cuentan con las siguientes caracteristicas: \n Código: {self.codigo} \n Nombre: {self.nombre} \n Marca: {self.marca} \n Stock: {self.stock} \n Precio: {self.precio} \n Color: {self.color} \ \n Detalle: {self.detalle}'

    def info_compra(self):
        return f'Breve descripcion para que pueda realizar su compra: \n Código: {self.codigo} \n Nombre: {self.nombre} \n Precio: {self.precio} \n Stock: {self.stock}'

    def asumir_nombre(self):
        return self.nombre

    def __str__(self):
        return self.asumir_nombre()

    def corregir_stock(self, cantidad):
        self.stock -= cantidad

    def revisar_stock (self, cantidad ):
        if self.stock >=cantidad:
            return True
        else:
            return False

    def buscararticulo(codigo, articulos):
        articulo_encontrado = None
        for articulo in articulos:
            if articulo.codigo == codigo:
                articulo_encontrado = articulo
                break
        if articulo_encontrado:
            return articulo_encontrado
        else:
            print("No se encontró el artículo seleccionado.")
            return None


class CarritoCompra:
    def __init__(self):
        self.articulo = []
        self.monto_total = 0 

    def agregar_carrito (self, articulo, cantidad):
        if articulo.revisar_stock(cantidad):
            articulo.corregir_stock(cantidad)
            precio_total = articulo.precio*cantidad
            self.monto_total += precio_total
            self.articulo.append((articulo, cantidad))
            print('=='*45)
            print (f'{cantidad} articulos disponibles de {articulo.nombre} agregada(s) al CarritoTiendita.')
            print('=='*45)
        else:
            print('=='*45)
            print (f'Lamentablemente no contamos con la cantidad solicitada de dicho articulo: {articulo.nombre}.')
            print('=='*45)

    def mostrar_carrito(self):

        if len(self.articulo) == 0:
            print ('No agrego ningun articulo en su carrito.')
            return (False)
        else:
            print('=='*45)
            nombre = input('¿Desea abonar el CarritoTiendita que usted selecciono?, ¿A nombre de quien realizar su Factura?')


            print ('Articulos que cuenta en su CarritoTiendita')

            for articulo, cantidad in self.articulo:

                print (f'{cantidad} articulos disponibles de {articulo.nombre} agregada(s) al CarritoTiendita.')
            print(f'Factura B a nombre de: {nombre} Fecha: {date.today()}')
            print (f'El total a pagar de su CarritoTiendita es: ${self.monto_total}')
            print('=='*45)

            return True
            

carrito = CarritoCompra()

articulos = [
    Articulos ('0001', 'Cofler', 'Arcor', 105, 800, 'Marron', 'Tableta de Chocolate con leche, 100gr.'),
    Articulos ('0002', 'Cofler Rocklets', 'Arcor', 75, 850, 'Marron y Negro', 'Tableta de Chocolate con confites Rocklets, 100gr.'),
    Articulos ('0003', 'Cofler Air', 'Arcor', 150, 900, 'Marron y Verde', 'Tableta de Chocolate con Almendras, 100gr.'),
    Articulos ('0004', 'Cofler Block', 'Arcor', 120, 630, 'Amarillo', 'Tableta de Chocolate con Mani, 110gr.'),
    Articulos ('0005', 'Cofler Chocolinas', 'Arcor', 60, 720, 'Blanco y Violeta', 'Tableta de Chocolate Blanco con Chocolinas, 100gr.'),
    Articulos ('0006', 'Cofler Tres Placeres', 'Arcor', 85, 445, 'Marron y Fuxia', 'Tableta de Chocolate tres tipos de chocolate (leche, semiamargo y blanco), 55gr.'),
    Articulos ('0007', 'Cofler Rio de Frutilla', 'Arcor', 55, 580, 'Rosaso', 'Tableta de Chocolate con Yogurt de Frutilla, 64gr.'),
    Articulos ('0008', 'Cofler Air Blanco', 'Arcor', 75, 470, 'Marron y Celeste', 'Tableta de Chocolate aireado Blanco, 55gr.'),
    Articulos ('0009', 'Cofler Air Mixto', 'Arcor', 75, 470, 'Marron y Amarillo', 'Tableta de Chocolate negro y blando aireado , 55gr.'),
    Articulos ('0010', 'Cofler Air', 'Arcor', 75, 470, 'Marron y Rojo', 'Tableta de Chocolate aireado Negro, 55gr.'),
                
    ]

def opcion_uno():

    for articulo in articulos:
        print('=='*45)
        print (articulo.info_ampliada())
    carrito.agregar_carrito(articulo)

def opcion_dos ():

    for articulo in articulos:
        print('=='*45)
        print (articulo.info_compra())
        print('=='*45)
    carrito.agregar_carrito(articulo)
    
def opcion_tres():
    while True:
        try:
            codigo = int(input('Por favor, ingrese el código del artículo que desea buscar en La Tiendita: '))
            articulo_encontrado = buscararticulo(codigo)

            if articulo_encontrado:
                print(articulo_encontrado.info_ampliada())
                carrito.agregar_carrito(articulo_encontrado)

            else:
                print('No se encontró el artículo seleccionado')

        except ValueError:
            print('El código que ingresaste no es válido')
        else:
            break
        
def opcion_cuatro ():
    while True:
        try:
            codigo_articulo = int(input('¿Cual articulo de La Tiendita desea agregar a su carrito? (Ingrese el código del aticulo): '))
            articulo = buscararticulo(codigo_articulo)

            if articulo:
                unidades = int(input(f'¿Cuantas unidades de {articulo.nombre} desea llevar?: '))
                carrito.agregar_carrito (articulo, unidades)
            else:
                print ('No se encontro el Articulo seleccionado')

        except ValueError:
            print ('El codigo que ingresaste no es valido')

        else:
            break

def opcion_cinco ():

    if carrito.mostrar_carrito() == True:
        carrito.corregir_carrito()

    

def carrito_agregar():
    while True:
        try:
            opcion = int(input('Quiere agregar algun articulo al su CarritoTiendita? (\n SI -----> 1 \n NO -----> 2): '))
            if opcion == 1:
                opcion_cuatro ()
            else:
                print('=='*45)
                print ('Regresando al MENU')
                print('=='*45)
        except ValueError:
            print ('La opcion que ingresaste no es correcta, ingresala otra vez')
        else:
            break
def corregir_carrito ():
    while True:
        try:
            corregir = int(input('¿Queres cambiale algo a tu CarritoTiendita? (\n SI -----> 1 \n NO -----> 2): '))
            if corregir == 1:
                
                articulo_corregir = int(input('Ingresa el codigo del articulo que queres corregir: '))

                articulo_encontrado = None
                for articulo in articulos:
                    if articulo.codigo == articulo_corregir:
                        articulo_encontrado = articulo
                        break
                    if articulo_encontrado:
                        articulo = articulo_encontrado
                        cantidad_nueva = int(input(f'Ingresa la nueva cantidad de {articulo.nombre}: '))
                        
                    if articulo.revisar_stock(cantidad_nueva):

                        cantidad_actual = carrito.obtener_cantidad_articulo(articulo)
                        diferencia = cantidad_nueva - cantidad_actual

                        articulo.corregir_stock (diferencia)

                        carrito.corregir_cantidad_articulo (articulo, cantidad_nueva)

                        print (f'Articulo {articulo.nombre} corregir correctamente en el carrito. ')
                    else:
                        print (f'No hay la cantidad de necesaria de {articulo.nombre}, para entregarle la cantidad deseada.')
                else:
                    print ('No se encontro el Articulo seleccionado')
            else:
                print ('No va a realizar cambios en el CarritoTiendita.')
        except ValueError:
            print ('No ingresaste una opcion que fuera valida, ingrese nuevamente la opcion deseada.')
        else:
            break


