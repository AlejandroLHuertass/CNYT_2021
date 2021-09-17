import unittest
import math

import cmath 
import lib_complejos as lb 


class test_lib_complejos(unittest.TestCase):
    
    def test_suma(self):
        # Caso 1
        
        x = [6,3]
        y = [5,1]
        self.assertEqual(lb.suma_complejos(x,y), (11,4))

        # Caso 2 negativos

        x = [-6,3]
        y = [5,-1]
        self.assertEqual(lb.suma_complejos(x,y), (-1,2))
        
    def test_multiplicacion(self):
        # Caso 1
        
        x = [6,3]
        y = [5,1]
        self.assertEqual(lb.multiplicacion_complejos(x,y), (27,21))

        # Caso 2 0 y limite

        x = [0,1]
        y = [5,2]
        self.assertEqual(lb.multiplicacion_complejos(x,y), (-2,5))
        
    def test_resta(self):
        # Caso 1
        
        x = [6,12]
        y = [4,3]
        self.assertEqual(lb.resta_complejos(x,y), (2,9))

        # Caso 2 negativos

        x = [-6,12]
        y = [4,-3]
        self.assertEqual(lb.resta_complejos(x,y), (-10,15))
        
    def test_division(self):
        # Caso 1
        
        x = [10,20]
        y = [30,40]
        self.assertEqual(lb.division_complejos(x,y), (0.44,0.08))

        # Caso 2 negativos

        x = [-6,12]
        y = [4,-3]
        self.assertEqual(lb.division_complejos(x,y), (-2.4,1.2))


    def test_division(self):
        # Caso 1
        
        x = [10,20]
        y = [30,40]
        self.assertEqual(lb.division_complejos(x,y), (0.44,0.08))

        # Caso 2 negativos

        x = [-6,12]
        y = [4,-3]
        self.assertEqual(lb.division_complejos(x,y), (-2.4,1.2))

    def test_modulo(self):
        # Caso 1
        
        x = [3,4]
        self.assertEqual(lb.modulo_complejos(x), (5))

        # Caso 2 negativos

        x = [0,4]
        self.assertEqual(lb.modulo_complejos(x), (4))
        
    def test_conjugado(self):
        # Caso 1
        
        x = [3,4]
        self.assertEqual(lb.conjugado_complejos(x), (3,-4))

        # Caso 2 cero

        x = [0,4]
        self.assertEqual(lb.conjugado_complejos(x), (0, -4))
        
    def test_cartesiano_polar(self):
        # Caso 1
        
        x = [4,8]
        self.assertEqual(lb.cartesiano_polar_complejos(x), [8.94427190999916, 63.43494882292201])

        # Caso 2 negativos

        x = [-6,8]
        self.assertEqual(lb.cartesiano_polar_complejos(x), [10.0, 126.86989764584402])
        
    def test_polar_cartesiano(self):
        # Caso 1
        
        x = [9,22]
        self.assertEqual(lb.polar_cartesiano_complejos(x),  [8.344654691101088, 3.371459340743208])

        # Caso 2 negativos

        x = [-4,5]
        self.assertEqual(lb.polar_cartesiano_complejos(x), [-3.984778792366982, -0.34862297099063266])
        
    def test_fase(self):
        # Caso 1
        
        x = [7,8]
        self.assertEqual(lb.fase_complejos(x), 48.81407483429036)

        # Caso 2 cero

        x = [2,0]
        self.assertEqual(lb.fase_complejos(x), 0)
    
if __name__ == '__main__':
    unittest.main()
