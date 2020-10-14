
class Recurso(object):
    """
    Este recurso se refiere a los recursos fisicos habilitados para su uso
    """
    def __init__(self, nombre : str, precio : float) -> None:
        self.nombre = nombre
        self.precio = precio
        self.distribuidor = ""
        self.cantidad = 0
    
    def setDistribuidor(self, dist : str) -> None: self.distribuidor = dist
    
    def agregarStock(self, cantidad: int =1) -> None: self.cantidad += cantidad

    def quitarStock(self, cantidad: int =1) -> None: self.cantidad -= cantidad

    def setStock(self, cantidad:int) -> None: self.cantidad = cantidad

    def guardar(self):
        print("Programar guardado")