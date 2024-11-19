class TV:
    _numTV = 0
    def __init__(self, marca: Marca, estado:bool):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

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
    
    def setMarca(self, marca: Marca):
        self._marca = marca 

    def setCanal(self, canal: int):
        if self._canal and 120>=canal>=1:
          self._canal = canal

    def setPrecio(self, precio: int):
        self._precio = precio  
    
    def setVolumen(self, volumen: int):
        if self._canal and 7>=volumen>=0:
         self._volumen = volumen 
    
    def setControl(self, control: Control):
        self._control = control 
    
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def getNumTV(cls, numTV: int):
        cls._numTV = numTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        self._canal += 1

    def canalDown(self):
        self._canal -= 1
