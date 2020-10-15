import pickle

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
        if self.exists(): return 
        with open(r"resources\data\recursos\\"+self.nombre.lower()+".dat", "wb") as f:
            pickle.dump(self, f)
    
    def exists(self) -> bool:
        pass