from tkinter import *
from tkinter import ttk
from functools import partial
from claseFraccion import Fraccion

class Aplicacion():
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None
    __contFraccion = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux=None
        self.__contFraccion = 0

        ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled').grid(column=0, row=0, sticky=(W,E))
        ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled').grid(column=1, row=0, columnspan=2, sticky=(W,E))

        ttk.Button(mainframe, text='1', command=partial(self.ingresarNumero,'1', False)).grid(column=0, row=1, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ingresarNumero,'2', False)).grid(column=1, row=1, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ingresarNumero,'3', False)).grid(column=2, row=1, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ingresarNumero,'4', False)).grid(column=0, row=2, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ingresarNumero,'5', False)).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ingresarNumero,'6', False)).grid(column=2, row=2, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ingresarNumero,'7', False)).grid(column=0, row=3, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ingresarNumero,'8', False)).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ingresarNumero,'9', False)).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ingresarNumero,'0', False)).grid(column=0, row=4, sticky=W)

        ttk.Button(mainframe, text='+', command=partial(self.ingresarSimbolo,'+')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ingresarSimbolo,'-')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ingresarSimbolo,'*')).grid(column=0, row=5, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ingresarSimbolo,'%')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ingresarSimbolo,'=')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ingresarNumero,'/', True)).grid(column=0, row=6, columnspan=2, sticky=(W,E))
        ttk.Button(mainframe, text='C', command=self.clear).grid(column=2, row=6, sticky=(W,E))

        self.__panel.set('0')
        self.__ventana.mainloop()

    def clear (self):
        self.__operador.set('')
        self.__panel.set('0')

    def ingresarNumero(self, numero, band):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            if (valor == '0') & (numero == '/'):
                print('ERROR')
                self.clear()
            else:
                self.__panel.set(valor+numero)
        else:
            self.__operadorAux=None
            valor=self.__panel.get()
            if not ('/' in valor):
                self.__primerOperando=int(valor)
            else:
                if (self.__contFraccion <= 1):
                    num = int(valor[:valor.find('/')])
                    den = int(valor[valor.find('/')+1:])
                    if (den == 0):
                        print('ERROR')
                        self.clear()
                    else:
                        self.__primerOperando= Fraccion(num,den)
                        self.__contFraccion = 0
                else:
                    print('ERROR')
                    self.clear()
            self.__panel.set(numero)
        if band:
            self.__contFraccion += 1

    def resolverOperacion(self, operando1, operacion, operando2):
        self.__bandFraccion = False
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='%':
                        resultado=operando1/operando2
        self.__panel.set(str(resultado))

    def ingresarSimbolo(self, op):
        band = False
        if op=='=':
            operacion=self.__operador.get()
            valor = self.__panel.get()
            if not ('/' in valor):
                self.__segundoOperando=int(valor)
            else:
                if (self.__contFraccion <= 1):
                    num = int(valor[:valor.find('/')])
                    den = int(valor[valor.find('/')+1:])
                    if (den == 0):
                        print('ERROR')
                        self.clear()
                        band = True
                    else:
                        self.__segundoOperando = Fraccion(num,den)
                        self.__contFraccion = 0
                else:
                    print('ERROR')
                    self.clear()
                    band = True
            if not band:
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion=self.__operador.get()
                valor = self.__panel.get()
                if not ('/' in valor):
                    self.__segundoOperando=int(valor)
                else:
                    if (self.__contFraccion <= 1):
                        num = int(valor[:valor.find('/')])
                        den = int(valor[valor.find('/')+1:])
                        if (den == 0):
                            print('ERROR')
                            self.clear()
                            band = True
                        else:
                            self.__segundoOperando = Fraccion(num,den)
                            self.__contFraccion = 0
                    else:
                        print('ERROR')
                        self.clear()
                        band = True
                if not band:
                    self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                    self.__operador.set(op)
                    self.__operadorAux=op
