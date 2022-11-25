import sys
 
class Interface:
    def __init__(self) -> None:
        pass
    def menu(self):
        pass
    def mostrarDatos(self):
        pass
    def pago(self):
        pass
 
class Cliente(Interface):
    
  
    def __init__(self):
        super().__init__()
        print('-----BIENVENIDO/A. PROCESO DE REGISTRO EN CARGA-----')
        print('-----REGISTRANDO, RELLENE TODOS LOS CAMPOS CORRECTAMENTE---')
        self.nombre=input('Introduzca su nombre: ')
        self.apellidos=input('Introduzca sus apellidos: ')
        self.direccion=input('Introduzca su dirección: ')
        self.telefono=input('Introduzca su número de teléfono: ')
        self.correo=input('Introduzca su correo eléctronico: ')
        print('---------- SE HA REGISTRADO CORRECTAMENTE --------')
        print('--------- LOADING MENU 98% ---------')
    
   
    def menu(self):
        print("Bienvenido/a a la Selección de productos. Por favor, siga las instrucciones del menú")
        self.productos()


    def productos(self):
        listaproductos=['camiseta levis', 'pantalon vaquero diesel', 'pack gorros', 'jersey rayas', 'zapatillas nike', 'zapatillas reebook', 'bolso pedreria', 'pack bisuteria']
        precios=[14.18, 60.99, 13.99, 14.99, 70.75, 65.95, 39.99, 16.99]
        carrito=[] 
        while True:
            print('--------Procesando selección de productos. Por favor, seleccione una opción')
            print('1- Añadir productos que desee comprar')
            print('2- Pago de productos')
            opcion=int(input('Seleccione opción del menú anterior 1/2: '))
        

            if opcion==1:
                print(listaproductos)
                añadirproducto=input('Producto que desea añadir al carrito: ').lower()
                print(f' el producto {añadirproducto} se ha añadido correctamente.')
                if añadirproducto in listaproductos:
                    lista=listaproductos.index(añadirproducto)
                    precio=precios[lista]
                    print(f' El producto tiene valor de {precio} €')
                    carrito.append(precio)
                    preciosiniva=sum(carrito)
                    print(f' el precio total es {preciosiniva} €')
                
                    
                else:
                    print('Lo siento. Ese producto no está disponible')
                    

            elif opcion==2:
                preciosiniva=sum(carrito)
                print(preciosiniva)
                print('----Procesando su pago. Por favor, seleccione País en el que se encuentra---')
                print('1--España')
                print('2--Fuera de España')
                opcion=int(input('Seleccione una opción: '))
                if opcion==1:
                    print('¡Recuerda! Se implementa un 1.15 de IVA ')
                    preciofinal=(preciosiniva*1.15)
                    preciofinal=round(preciofinal, 2)
                    print(f'El precio total será de {preciofinal} euros')
                elif opcion==2:
                    print('¡Recuerda! Para envíos fuera de España se implementa un 1.30 de IVA')
                    preciofinal= (preciosiniva*1.30)
                    preciofinal=round(preciofinal, 2)
                    print(f'El precio total será de {preciofinal} euros')
                else:
                    print('Selección errónea. Por favor, seleccione de nuevo')
                
                print('-------Método de Pago-----')
                print('1--Tarjeta de crédito')
                print('2--Contra-Reembolso')
                opcion1=int(input('Seleccione método de pago: '))
                if opcion1==1:
                    print('Pago completado correcto')
                elif opcion1==2:
                    print('Opción de Contra-Reembolso efectuada correctamente')
                else:
                    print('Error de método de pago. Por favor, vuelva a seleccionar')
            
                print('GRACIAS POR SU COMPRA.')
                print(f'Se ha enviado un PDF con la factura de la compra al correo {self.correo}')
                print(f'Se ha enviado un correo al email {self.correo} y un SMS al telefono {self.telefono} con un número de seguimiento')
                sys.exit()  #EXPLICAR POR QUE HEMOS IMPORTADOD ESTE MODULO
           

 
 
cliente=Cliente()
cliente.menu()
cliente.productos()

 





        

   


