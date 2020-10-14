
from typing import Dict
from velas.model.recurso.recurso import Recurso


class Producto(object):
    """
    Es la clase encargada de manejar cada producto, pudiendo modificar su precio para la ganancia
    Cuando porcentaje esta activo, la ganancia se transforma en un multiplicador
    que es el que se multiplica por el precio final y SE LE SUMA.
    """
    def __init__(self, nombre:str) -> None:
        self.recursos : Dict[Recurso, float] = {}
        self.nombre = nombre
        self.ganancia = 0
        self.porcentaje = False
        

    def addRecurso(self, recurso : Recurso, cantidad:float) -> None:
        self.recursos[recurso] = cantidad
    
    def removeRecurso(self, recurso:Recurso) -> None:
        self.recursos.pop(recurso)
    
    def precioFinal(self) -> float:
        precio = 0
        for rec,cant in self.recursos.items():
            precio += rec.precio*cant
        if self.porcentaje:
            return precio*(self.ganancia+1)
        else:
            return precio+self.ganancia