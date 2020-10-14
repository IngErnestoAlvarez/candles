import unittest
from velas.model.recurso.recurso import Recurso

class TestRecurso(unittest.TestCase):

    def test_iniciacion(self):
        recurso = Recurso("cera", 100)
        self.assertEqual(recurso.nombre, "cera")
        self.assertEqual(recurso.precio, 100, "El precio tiene que ser con el que se inicio")
        self.assertFalse(recurso.distribuidor)
        self.assertFalse(recurso.cantidad)
    
    def test_agregarStock(self):
        recurso = Recurso("cera", 100)
        recurso.agregarStock(100)
        self.assertEqual(recurso.cantidad, 100)
    
    def test_quitarStock(self):
        recurso = Recurso("cera", 100)
        recurso.agregarStock(100)
        recurso.quitarStock(50)
        self.assertEqual(recurso.cantidad, 50)
    
    def test_distribuidor(self):
        recurso = Recurso("cera", 100)
        self.assertEqual(recurso.distribuidor, "")
        recurso.setDistribuidor("Maria")
        self.assertEqual(recurso.distribuidor, "Maria")


if __name__ == "__main__":
    unittest.main()