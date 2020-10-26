import pathlib
import pickle
import os.path as path
from typing import List
from multipledispatch import dispatch

class Recurso(object):
    """
    Este recurso se refiere a los recursos fisicos habilitados para su uso
    """
    def __init__(self, nombre : str, precio : float, cantidad:float) -> None:
        self.nombre = nombre
        self.precio = precio
        self.distribuidor = ""
        self.cantidad = cantidad
    
    def setDistribuidor(self, dist : str) -> None: self.distribuidor = dist
    
    def agregarStock(self, cantidad: int =1) -> None: self.cantidad += cantidad

    def quitarStock(self, cantidad: int =1) -> None: self.cantidad -= cantidad

    def setStock(self, cantidad:int) -> None: self.cantidad = cantidad

    def guardar(self) -> None:
        with open(r"resources\data\recursos\\"+self.nombre.lower()+".dat", "wb") as f:
            pickle.dump(self, f)
    
    #! Chequear
    
    def eliminar(self) -> None:
        pathlib.Path(r"resources\data\recursos\\"+self.nombre.lower()+".dat").unlink(missing_ok=True)

@dispatch(str)
def cargarRecursoAlSistema(nombre:str) -> Recurso:
    print("Hola")
    return Recurso("Hola", 10, 10)

@dispatch()
def cargarRecursoAlSistema() -> List[Recurso]:
    path = pathlib.Path(r"resources\data\recursos")
    mylist = []
    for rec in path.iterdir():
        with open(r"resources\data\recursos\\"+ rec.name, "rb") as f:
            i = pickle.load(f)
            mylist.append(i)
    return mylist
