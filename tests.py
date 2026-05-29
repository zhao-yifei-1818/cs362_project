import unittest
from task import conv_num
from task import conv_endian


class TestCase(unittest.TestCase):

    def test_function1_valid(self):
        self.assertEqual(conv_num('12345'),12345)

    def test_function1_valid_neg(self):
        self.assertEqual(conv_num('-12345'),-12345)
    
    def test_function1_valid_neg2(self):
        self.assertEqual(conv_num('-123.45'),-123.45)

    def test_function1_valid_dec(self):
        self.assertEqual(conv_num('.45'),.45)

    def test_function1_valid_dec2(self):
        self.assertEqual(conv_num('123.'),123.0)

    def test_function1_valid_hexadec(self):
        self.assertEqual(conv_num('0xAD4'),2772)

    def test_function1_valid_lowercase(self):
        self.assertEqual(conv_num('0xad4'),2772)

    def test_function1_valid_neghexadec(self):
        self.assertEqual(conv_num('-0xAD4'),-2772)

    def test_function1_invalid_hexa(self):
        self.assertEqual(conv_num('0xAZ4'),None)

    def test_function1_invalid_str(self):
        self.assertEqual(conv_num('12345A'),None)
    
    def test_function1_invalid_deci(self):
        self.assertEqual(conv_num('12.3.45'),None)

    def test_function3_valid_big(self):
        self.assertEqual(conv_endian(954786, 'big'),'0E 91 A2')
    
    def test_function3_valid_no_value(self):
        self.assertEqual(conv_endian(954786),'0E 91 A2')

    def test_function3_valid_neg(self):
        self.assertEqual(conv_endian(-954786),'-0E 91 A2')

    def test_function3_valid_little(self):
        self.assertEqual(conv_endian(954786,'little'),'A2 91 0E')
    
    def test_function3_valid_little_neg(self):
        self.assertEqual(conv_endian(-954786,'little'),'-A2 91 0E')

    def test_function3_valid_declared(self):
        self.assertEqual(conv_endian(num=-954786, endian='little'),'-A2 91 0E')
    
    def test_function3_invalid(self):
        self.assertEqual(conv_endian(num=-954786, endian='small'),None)

if __name__ == '__main__':
    unittest.main()
