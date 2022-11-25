class Interface():
    def menu():
        pass
    def mostrarDatos():
        pass
    def pago():
        pass

class Cliente(Interface):
    def __init__(self):
        super().__init__()
        print('-----BIENVENIDO/A. PROCESO DE REGISTRO EN CARGA-----')
        print('-----REGISTRANDO, RELLENE TODOS LOS CAMPOS CORRECTAMENTE---')
        self.nombre=input('Introduzca su nombre: ')
        self.apellidos=input('Introduzca sus apellidos: ')
        self.direccion=input('Introduzca su dirección: ')
        self.telefono=int(input('Introduzca su número de teléfono: '))
        self.correo=input('Introduzca su correo eléctronico: ')
        self.mostrarDatos()
        self.Menu()

    def mostrarDatos():
        print('Se ha registrado correctamente.')


    def Menu(self):
        opcion=0
        while opcion!=0:
            print("1- Selección de productos")
            print("2- Método de pago")
            print("3- Seguimiento del pedido")
            opcion=int(input("Ingrese su opcion: "))
            if opcion==1:
                print('Ha seleccionado Selección de productos')
                self.productos()
            elif opcion==2:
                print('Ha seleccionado Método de Pago')
                self.pago()
            elif opcion==3:
                print('Ha seleccionado Seguimiento del pedido')
                self.seguimiento()
            else:
                print('Por favor, elija una opción del menú')
                self.Menu()

    #def productos(self, nombre,  precio):
        #self.nombre=nombre
        #self.precio=precio
    #productos=[]
    #productos.append()


    def pago(self):
        opcion=0
        print('----Procesando su pago. Por favor, seleccione País en el que se encuentra---')
        print('1--España')
        print('2--Fuera de España')
        opcion=int(input('Seleccione una opción: '))
        while opcion !=0:
            if opcion==1:
                print('¡Recuerda! Se implementa un 1.15 de IVA ')
                preciofinal= (PRODUCTO SELECIONADO +1.15)
                print(f'El precio total será de ------- euros')
            elif opcion==2:
                print('¡Recuerda! Para envíos fuera de España se implementa un 1.30 de IVA')
                preciofinal= (PRODUCTO SELECCIONADO + 1.30)
                print(f'El precio total será de ----- euros')
            else:
                print('Selección errónea. Por favor, seleccione de nuevo')
                self.pago()
        print('-------Método de Pago-----')
        opcion1=0
        print('1--Tarjeta de crédito')
        print('2--Contra-Reembolso')
        opcion1=int(input('Seleccione método de pago: '))
        while opcion1!=0:
            if opcion1==1:
                print('Pago completado correcto')
                self.seguimiento()
            elif opcion1==2:
                print('Opción de Contra-Reembolso efectuada correctamente')
                self.seguimiento()
            else:
                print('Error de método de pago. Por favor, vuelva a seleccionar')
                return

    def seguimiento(self):    
        print('GRACIAS POR SU COMPRA.')
        print('Se ha enviado un SMS al teléfono registrado')
        print('Se ha enviado un correo con un número de seguimiento')
        




        

   


