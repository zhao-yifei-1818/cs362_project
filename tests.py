import unittest
from task import conv_num
from task import conv_endian
from task import my_datetime


class TestCase(unittest.TestCase):
    def test_function1_valid(self):
        self.assertEqual(conv_num("12345"), 12345)

    def test_function1_valid_neg(self):
        self.assertEqual(conv_num("-12345"), -12345)

    def test_function1_valid_neg2(self):
        self.assertEqual(conv_num("-123.45"), -123.45)

    def test_function1_valid_dec(self):
        self.assertEqual(conv_num(".45"), 0.45)

    def test_function1_valid_dec2(self):
        self.assertEqual(conv_num("123."), 123.0)

    def test_function1_valid_hexadec(self):
        self.assertEqual(conv_num("0xAD4"), 2772)

    def test_function1_valid_lowercase(self):
        self.assertEqual(conv_num("0xad4"), 2772)

    def test_function1_valid_neghexadec(self):
        self.assertEqual(conv_num("-0xAD4"), -2772)

    def test_function1_invalid_hexa(self):
        self.assertEqual(conv_num("0xAZ4"), None)

    def test_function1_invalid_str(self):
        self.assertEqual(conv_num("12345A"), None)

    def test_function1_invalid_deci(self):
        self.assertEqual(conv_num("12.3.45"), None)

    def test_function2_valid_my_datetime_start(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test_function2_valid_my_datetime_example1(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test_function2_valid_my_datetime_example2(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

    def test_function2_epoch(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test_function2_one_day(self):
        self.assertEqual(my_datetime(86400), "01-02-1970")

    def test_function2_end_of_january(self):
        self.assertEqual(my_datetime(30 * 86400), "01-31-1970")

    def test_function2_start_of_february(self):
        self.assertEqual(my_datetime(31 * 86400), "02-01-1970")

    def test_function2_end_of_year(self):
        self.assertEqual(my_datetime(364 * 86400), "12-31-1970")

    def test_function2_start_of_next_year(self):
        self.assertEqual(my_datetime(365 * 86400), "01-01-1971")

    def test_function2_valid_my_datetime_example3(self):
        self.assertEqual(my_datetime(201653971200), "02-29-8360")

    def test_function3_valid_big(self):
        self.assertEqual(conv_endian(954786, "big"), "0E 91 A2")

    def test_function3_valid_no_value(self):
        self.assertEqual(conv_endian(954786), "0E 91 A2")

    def test_function3_valid_neg(self):
        self.assertEqual(conv_endian(-954786), "-0E 91 A2")

    def test_function3_valid_little(self):
        self.assertEqual(conv_endian(954786, "little"), "A2 91 0E")

    def test_function3_valid_little_neg(self):
        self.assertEqual(conv_endian(-954786, "little"), "-A2 91 0E")

    def test_function3_valid_declared(self):
        self.assertEqual(conv_endian(num=-954786, endian="little"), "-A2 91 0E")

    def test_function3_invalid(self):
        self.assertEqual(conv_endian(num=-954786, endian="small"), None)


if __name__ == "__main__":
    unittest.main()
