class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.numTV += 1

    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self._canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen
    
    def getControl(self):
        return self._control
    
    def getEstado(self):
        return self._estado
    
    def setMarca(self, marca):
        self._marca = marca 

    def setCanal(self, canal):
        if self._estado ==True and 120>=canal>=1:
          self._canal = canal

    def setPrecio(self, precio):
        self._precio = precio  
    
    def setVolumen(self, volumen):
        if self._estado==True and 7>=volumen>=0:
         self._volumen = volumen 
    
    def setControl(self, control):
        self._control = control 
    
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    @classmethod
    def setNumTV(cls, numTV: int):
        cls.numTV = numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
       if 120>self._canal>=1 and self._estado == True:
        self._canal += 1

    def canalDown(self):
       if 120>=self._canal>1 and self._estado == True: 
        self._canal -= 1

    def volumenUp(self):
       if 7>self._volumen>=0 and self._estado == True:
          self._volumen += 1

    def volumenDown(self):
       if 7>=self._volumen>0 and self._estado == True:
          self._volumen -= 1      