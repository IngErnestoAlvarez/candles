from model.producto.producto import Producto
from typing import Dict


class Compra(object):
    """
    Referencia a la compra de un cliente.
    """
    def __init__(self, comprador : str) -> None:
        self.comprador = comprador
        self.productos : Dict[Producto, int] = {}
    
    def precioFinal(self) -> float:
        return sum([pro.precioFinal()*cant for pro,cant in self.productos.items()])