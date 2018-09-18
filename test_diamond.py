import unittest
from diamond import Diamond
from printer import Printer

class TestDiamond(unittest.TestCase):
    def test_A(self):
        output = "A"
        printer = Printer(Diamond('A').draw())
        self.assertEqual(output,printer.text)
    def test_B(self):
        output = """ A\nB B\n A"""
        printer = Printer(Diamond('B').draw())
        self.assertEqual(output, printer.text)
    def test_C(self):
        output = """  A\n B B\nC   C\n B B\n  A"""
        printer = Printer(Diamond('C').draw())
        self.assertEqual(output, printer.text)
    def test_E(self):
        output = """    A\n   B B\n  C   C\n D     D\nE       E\n D     D\n  C   C\n   B B\n    A"""
        printer = Printer(Diamond('E').draw())
        self.assertEqual(output, printer.text)
    def test_invalid(self):
        output = "Enter a valid letter in the Alphabet, looking at you Ben."
        printer = Printer(Diamond('$').draw())
        self.assertEqual(output, printer.text)
    def test_empty(self):
        output = "Enter a valid letter in the Alphabet, looking at you Ben."
        printer = Printer(Diamond('').draw())
        self.assertEqual(output, printer.text)
    def test_multi_chars(self):
        output = "Enter a valid letter in the Alphabet, looking at you Ben."
        printer = Printer(Diamond('AA').draw())
        self.assertEqual(output, printer.text)
        

