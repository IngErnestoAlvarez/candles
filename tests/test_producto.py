import unittest
from velas.model.recurso.recurso import Recurso
from velas.model.producto.producto import Producto

class TestProducto(unittest.TestCase):

    def test_iniciacion(self):
        prod = Producto("vela1")
        self.assertDictEqual(prod.recursos, dict())
        self.assertEqual(prod.ganancia, 0)
        self.assertFalse(prod.porcentaje)
    
    def test_addRecurso_and_remove(self):
        rec = Recurso("cera", 100)
        prod = Producto("vela1")
        prod.addRecurso(rec, 1)
        self.assertDictEqual(prod.recursos, dict([(rec, 1)]))
        prod.removeRecurso(rec)
        self.assertDictEqual(prod.recursos, dict())

    def testPrecioFinal(self):
        rec1 = Recurso("cera", 100)
        rec2 = Recurso("esencia", 50)
        prod = Producto("vela1")
        prod.addRecurso(rec1, 10)
        prod.addRecurso(rec2, 2)
        self.assertEqual(prod.precioFinal(), 1100)
    
    def testPrecioFinal_conGananciaNeta(self):
        rec1 = Recurso("cera", 100)
        rec2 = Recurso("esencia", 50)
        prod = Producto("vela1")
        prod.addRecurso(rec1, 10)
        prod.addRecurso(rec2, 2)
        prod.ganancia = 100
        self.assertEqual(prod.precioFinal(), 1200)

    def testPrecioFinal_conGananciaNeta(self):
        rec1 = Recurso("cera", 100)
        rec2 = Recurso("esencia", 50)
        prod = Producto("vela1")
        prod.addRecurso(rec1, 10)
        prod.addRecurso(rec2, 2)
        prod.porcentaje = True
        prod.ganancia = 1
        self.assertEqual(prod.precioFinal(), 2200)
