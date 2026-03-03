import unittest
import sys
import os

# Pour que GitHub Actions trouve le dossier src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculatrice import division, puissance, moyenne

class TestCalculatrice(unittest.TestCase):
    def test_div(self): self.assertEqual(division(10, 2), 5.0)
    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError): division(10, 0)
    
    def test_pow(self): self.assertEqual(puissance(2, 3), 8.0)
    def test_pow_neg(self):
        with self.assertRaises(ValueError): puissance(2, -1)
        
    def test_moy(self): self.assertEqual(moyenne([10, 20]), 15.0)
    def test_moy_vide(self):
        with self.assertRaises(ValueError): moyenne([])
