import unittest
from task import conv_num
from task import conv_endian
from task import _is_leap_year
from task import _seconds_to_days
from task import _get_year_and_day_of_year
from task import _get_month_and_day
from task import _format_date
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

    def test_function2_invalid_leapyear_normal_year(self):
        self.assertEqual(_is_leap_year(2023), False)

    def test_function2_invalid_leapyear_century_year(self):
        self.assertEqual(_is_leap_year(1900), False)

    def test_function2_valid_leapyear_four_hundred_year(self):
        self.assertEqual(_is_leap_year(2000), True)

    def test_function2_valid_seconds_to_days_zero(self):
        self.assertEqual(_seconds_to_days(0), 0)

    def test_function2_valid_seconds_to_days_less_than_one_day(self):
        self.assertEqual(_seconds_to_days(86399), 0)

    def test_function2_valid_seconds_to_days_one_day(self):
        self.assertEqual(_seconds_to_days(86400), 1)

    def test_function2_valid_get_year_start(self):
        self.assertEqual(_get_year_and_day_of_year(0), (1970, 0))

    def test_function2_valid_get_year_end_of_1970(self):
        self.assertEqual(_get_year_and_day_of_year(364), (1970, 364))

    def test_function2_valid_get_year_start_of_1971(self):
        self.assertEqual(_get_year_and_day_of_year(365), (1971, 0))

    def test_function2_valid_month_day_normal_year(self):
        self.assertEqual(_get_month_and_day(1970, 31), (2, 1))

    def test_function2_valid_month_day_leap_day(self):
        self.assertEqual(_get_month_and_day(1972, 59), (2, 29))

    def test_function2_valid_format_date(self):
        self.assertEqual(_format_date(1, 1, 1970), "01-01-1970")

    def test_function2_valid_my_datetime_start(self):
        self.assertEqual(my_datetime(0), "01-01-1970")

    def test_function2_valid_my_datetime_example1(self):
        self.assertEqual(my_datetime(123456789), "11-29-1973")

    def test_function2_valid_my_datetime_example2(self):
        self.assertEqual(my_datetime(9876543210), "12-22-2282")

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
