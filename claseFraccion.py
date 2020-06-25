class Fraccion:
    __Numerador = 0
    __Denominador = 0

    def __init__ (self, numerador, denominador):
        self.__Numerador = numerador
        self.__Denominador = denominador

    def __str__ (self):
        return '{}/{}'.format(self.__Numerador,self.__Denominador)

    def MDC (self,otro):
        z = max(self.__Denominador,otro.__Denominador)
        band = False
        while not band:
            if (z % self.__Denominador == 0) & (z % otro.__Denominador == 0):
                band = True
            else:
                z += 1
        return z

    def __add__(self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if (self.__Numerador == 0):
            resultado = otro
        elif (otro.__Numerador == 0):
            resultado = self
        else:
            den = self.MDC(otro)
            num = int(((den/self.__Denominador) * self.__Numerador) + ((den/otro.__Denominador) * otro.__Numerador))
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def __radd__(self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if (self.__Numerador == 0):
            resultado = otro
        elif (otro.__Numerador == 0):
            resultado = self
        else:
            den = self.MDC(otro)
            num = int(((den/self.__Denominador) * self.__Numerador) + ((den/otro.__Denominador) * otro.__Numerador))
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def __sub__(self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if (self.__Numerador == 0):
            resultado = otro
        elif (otro.__Numerador == 0):
            resultado = self
        else:
            den = self.MDC(otro)
            num = int(((den/self.__Denominador) * self.__Numerador) - ((den/otro.__Denominador) * otro.__Numerador))
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def __rsub__(self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if (self.__Numerador == 0):
            resultado = otro
        elif (otro.__Numerador == 0):
            resultado = self
        else:
            den = self.MDC(otro)
            num = int(((den/otro.__Denominador) * otro.__Numerador) - ((den/self.__Denominador) * self.__Numerador))
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def __mul__(self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if (self.__Numerador == 0) or (otro.__Numerador == 0):
            resultado = Fraccion(0,0)
        else:
            den = int(self.__Denominador * otro.__Denominador)
            num = int(self.__Numerador * otro.__Numerador)
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def __rmul__(self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if (self.__Numerador == 0) or (otro.__Numerador == 0):
            resultado = Fraccion(0,0)
        else:
            den = int(self.__Denominador * otro.__Denominador)
            num = int(self.__Numerador * otro.__Numerador)
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def __truediv__ (self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if self.__Numerador == 0:
            resultado = Fraccion(0,0)
        elif otro.__Numerador == 0:
            resultado = None       #Division por 0
        else:
            den = int(self.__Denominador * otro.__Numerador)
            num = int(self.__Numerador * otro.__Denominador)
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def __rtruediv__ (self, otro):
        if isinstance(otro,int):
            otro = Fraccion(int(otro),1)
        if self.__Numerador == 0:
            resultado = Fraccion(0,0)
        elif otro.__Numerador == 0:
            resultado = None       #Division por 0
        else:
            den = int(otro.__Denominador * self.__Numerador)
            num = int(otro.__Numerador * self.__Denominador)
            resultado = Fraccion(num,den)
            resultado.simplificar()
        return resultado

    def MCD (self):               #Algoritmo de Euclides
        u = self.__Numerador
        v = self.__Denominador
        r = 0
        while v != 0:
            r = u % v
            u = v
            v = r
        return u

    def simplificar (self):
        mcd = self.MCD()
        self.__Numerador = int(self.__Numerador / mcd)
        self.__Denominador = int(self.__Denominador / mcd)
        if (self.__Numerador == 0):
            self.__Denominador = 0
