class Producto:
    def __init__(self, codigo, nombre, marca, precio, stock, color, caracteristicas):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.color = color
        self.caracteristicas = caracteristicas

    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getMarca(self):
        return self.marca

    def getPrecio(self):
        return self.precio

    def getStock(self):
        return self.stock

    def setStock(self, cantidad):
        self.stock = cantidad

    def getColor(self):
        return self.color

    def getCaracteristicas(self):
        return self.caracteristicas


class ProductoCarrito(Producto):
    def __init__(self, codigo, nombre, marca, precio, cantidad, color, caracteristicas):
        super().__init__(codigo, nombre, marca, precio, cantidad, color, caracteristicas)
        self.subtotal = precio * cantidad

    def getSubtotal(self):
        return self.subtotal


def checkNum(num):
    while True:
        try:
            return int(num)
        except ValueError:
            try:
                return float(num)
            except ValueError:
                print(f"La opción ingresada: '{num}' no es un número válido.")
                num = input("Ingrese nuevamente la opción: ")


def checkOption(opcion, cantidad, menu=""):
    while True:
        try:
            opcion = int(opcion)
            if 0 < opcion <= cantidad:
                return opcion
            print(menu)
            print("Valor fuera de rango.")
        except ValueError:
            print(menu)
            print("Valor inválido.")
        opcion = input("Ingrese una opción válida: ")


def listarProductos(productos, carritoFlag=False):
    productosListados = []
    for producto in productos:
        if carritoFlag:
            productosListados.append([
                producto.getNombre(),
                producto.getPrecio(),
                producto.getMarca(),
                producto.getColor(),
                producto.getStock(),
                producto.getCaracteristicas(),
                producto.getCodigo(),
                producto.getSubtotal()
            ])
        else:
            productosListados.append([
                producto.getNombre(),
                producto.getPrecio(),
                producto.getMarca(),
                producto.getColor(),
                producto.getStock(),
                producto.getCaracteristicas(),
                producto.getCodigo()
            ])
    return productosListados


def buscarProducto(codigo, listaProductos):
    codigo = codigo.lower() if not codigo.isnumeric() else int(codigo)
    for producto in listaProductos:
        if codigo == producto.getCodigo() or codigo == producto.getNombre().lower():
            return producto
    print("No se encontró el producto.")
    return False


def añadirACarrito(producto, clase, subclase, carrito):
    if isinstance(producto, clase):
        cantidad = checkNum(input(f"¿Qué cantidad desea añadir?\nDisponibles: {producto.getStock()} kg\n:"))
        if 0 < cantidad <= producto.getStock():
            productoCarrito = subclase(
                producto.getCodigo(),
                producto.getNombre(),
                producto.getMarca(),
                producto.getPrecio(),
                cantidad,
                producto.getColor(),
                producto.getCaracteristicas()
            )
            carrito.append(productoCarrito)
            producto.setStock(producto.getStock() - cantidad)
            print("\n¡Producto agregado al carrito!")
            return True
        elif cantidad == 0:
            print("No puede agregar 0 unidades.")
        else:
            print("Cantidad fuera de rango.")
    else:
        print("No se pudo añadir el producto al carrito.")
    return False


def removerDeCarrito(producto, carrito):
    if producto in carrito:
        carrito.remove(producto)
        producto.setStock(producto.getStock() + producto.getStock())
        print("\n¡Producto eliminado del carrito!")
        return True
    else:
        print("El producto no se encuentra en el carrito.")
    return False


def calcularTotal(carrito):
    total = 0
    for producto in carrito:
        total += producto.getSubtotal()
    return total


def imprimirCarrito(carrito):
    if carrito:
        print("\n---- Carrito de Compras ----")
        productosListados = listarProductos(carrito, True)
        for producto in productosListados:
            print("Código: ", producto[6])
            print("Nombre: ", producto[0])
            print("Marca: ", producto[2])
            print("Color: ", producto[3])
            print("Cantidad: ", producto[4])
            print("Características: ", producto[5])
            print("Subtotal: ", producto[7])
            print()
        print("Total a pagar: ", calcularTotal(carrito))
    else:
        print("El carrito de compras está vacío.")


# Ejemplo de uso del código:

# Crear productos
producto1 = Producto(1,"Vacio","Swift",1400,2000,"Rojo","Carne de Novillo")
producto2 = Producto(2,"Costilla","Swift",1100,2500,"Rojo","Carne de Novillo")
producto3 = Producto(3,"Matambre","Swift",1350,2000,"Rojo","Carne de Novillo")
producto4 = Producto(4,"Bondiola","Piamontesa",1200,2300,"Rosado","Carne de Cerdo")
producto5 = Producto(5,"Jamon","Piamontesa",900,3000,"Rosado","Carne de Cerdo")
producto6 = Producto(6,"Chorizo","Piamontesa",1250,3000,"Rosado y Blanco","Embutido de Puro Cerdo")
producto7 = Producto(7,"Pollo","CrestaRoja",500,5000,"Ambar","Pollo Fresco con menudos")

# Lista de productos disponibles
productosDisponibles = [producto1, producto2, producto3, producto4, producto5, producto6, producto7]

# Carrito de compras
carritoCompras = []

# Menú principal
while True:
    print("\n---- Bienvenidos a FUEGOS ----")
    print("1. Ver productos disponibles")
    print("2. Ver producto en detalle")
    print("3. Buscar producto por código o nombre")
    print("4. Añadir producto al carrito")
    print("5. Eliminar producto del carrito")
    print("6. Ver carrito de compras")
    print("7. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("\n---- Productos Disponibles ----")
        productosListados = listarProductos(productosDisponibles)
        for i, producto in enumerate(productosListados, start=1):
            print(i, ".", producto[0], "-", producto[2])

    elif opcion == "2":
        print("\n---- Detalles del Producto ----")
        productosListados = listarProductos(productosDisponibles)
        for i, producto in enumerate(productosListados, start=1):
            print(i, ".", producto[6], "-", producto[0],"-", producto[2],"-", producto[1],"-", producto[4],"-", producto[3],"-", producto[5])

    elif opcion == "3":
        codigo = input("\nIngrese el código o nombre del producto a buscar: ")
        productoEncontrado = buscarProducto(codigo, productosDisponibles)
        if productoEncontrado:
            print("\nProducto encontrado:")
            print("Código: ", productoEncontrado.getCodigo())
            print("Nombre: ", productoEncontrado.getNombre())
            print("Marca: ", productoEncontrado.getMarca())
            print("Precio: ", productoEncontrado.getPrecio())
            print("Stock: ", productoEncontrado.getStock())
            print("Color: ", productoEncontrado.getColor())
            print("Características: ", productoEncontrado.getCaracteristicas())

    elif opcion == "4":
        codigo = input("\nIngrese el código o nombre del producto a añadir al carrito: ")
        productoEncontrado = buscarProducto(codigo, productosDisponibles)
        if productoEncontrado:
            añadirACarrito(productoEncontrado, Producto, ProductoCarrito, carritoCompras)

    elif opcion == "5":
        imprimirCarrito(carritoCompras)
        codigo = input("\nIngrese el código o nombre del producto a eliminar del carrito: ")
        productoEncontrado = buscarProducto(codigo, carritoCompras)
        if productoEncontrado:
            removerDeCarrito(productoEncontrado, carritoCompras)

    elif opcion == "6":
        imprimirCarrito(carritoCompras)

    elif opcion == "7":
        print("¡Gracias por utilizar el sistema de carrito de compras!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
