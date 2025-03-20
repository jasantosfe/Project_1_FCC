import unittest
import numpy as np
import random
from mean_var_std import calculate

class TestCalculate(unittest.TestCase):
    def test_manual_inputs(self):
        """ Prueba con valores fijos para validación manual """
        input_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected_output = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(calculate(input_data), expected_output)

    def test_random_inputs(self):
        """ Prueba con 30 conjuntos de datos aleatorios """
        for i in range(30):
            input_data = random.sample(range(-100, 100), 9)  # 9 números aleatorios entre -100 y 100
            result = calculate(input_data)

            # Validar que el resultado tiene la estructura correcta
            self.assertTrue(isinstance(result, dict), f"Error en iteración {i}: No es un diccionario.")
            self.assertEqual(len(result), 6, f"Error en iteración {i}: Faltan claves en el diccionario.")
            
            for key in result:
                self.assertEqual(len(result[key]), 3, f"Error en iteración {i}: {key} no tiene 3 elementos.")
                self.assertTrue(all(isinstance(x, list) for x in result[key][:2]), f"Error en iteración {i}: {key} no tiene listas en las dos primeras posiciones.")
                self.assertTrue(isinstance(result[key][2], (int, float)), f"Error en iteración {i}: {key} en la tercera posición no es un número.")

# Ejecutar pruebas en Jupyter
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCalculate))
