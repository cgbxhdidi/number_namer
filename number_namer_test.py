##by Didi She

import unittest
from number_namer import *

class TestNumberName(unittest.TestCase):

    def tell_about(self, fun, x, y = None, s_b = ''):
        result = fun(x) if y == None else fun(x, y)
        if result == s_b:
            return
        else:
            self.fail("Result should not be " + result)
        
    def test_name_of_digit(self):
        self.tell_about(name_of_digit, 0, s_b = 'zero')
        self.tell_about(name_of_digit, 5, s_b = 'five')

    def test_name_of_tens(self):
        self.tell_about(name_of_tens, 1, s_b = 'ten')
        self.tell_about(name_of_tens, 5, s_b = 'fifty')

    def test_name_of_teens(self):
        self.tell_about(name_of_teens, 10, s_b = 'ten')
        self.tell_about(name_of_teens, 19, s_b = 'nineteen')

    def test_name_of_short_int(self):
        self.tell_about(name_of_short_int, 10, s_b = 'ten')
        self.tell_about(name_of_short_int, 487, s_b = 'four hundred eighty seven')
        self.tell_about(name_of_short_int, 107, s_b = 'one hundred seven')
        self.tell_about(name_of_short_int, 20, s_b = 'twenty')
        self.tell_about(name_of_short_int, 57, s_b = 'fifty seven')
        self.tell_about(name_of_short_int, 150, s_b = 'one hundred fifty')

    def test_name_of_integer(self):
        self.tell_about(name_of_integer, 999999999,
                        s_b = 'nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine')
        self.tell_about(name_of_integer, 569009, s_b = 'five hundred sixty nine thousand nine')
        self.tell_about(name_of_integer, 99, s_b = 'ninety nine')
        self.tell_about(name_of_integer, 569000090, s_b = 'five hundred sixty nine million ninety')
        self.tell_about(name_of_integer, 1214717, s_b = 'one million two hundred fourteen thousand seven hundred seventeen')
        self.tell_about(name_of_integer, 119119000, s_b = 'one hundred nineteen million one hundred nineteen thousand')
        self.tell_about(name_of_integer, 10000008, s_b = 'ten million eight')

    def test_name_of_fraction(self):
        self.tell_about(name_of_fraction, (17, 100), s_b = 'seventeen hundredths')
        self.tell_about(name_of_fraction, (1, 10), s_b = 'one tenth')
        self.tell_about(name_of_fraction, (0, 10), s_b = 'zero tenths')
        self.tell_about(name_of_fraction, (0, 1000), s_b = 'zero thousandths')
       
    def test_name_of_decimal(self):
        self.tell_about(name_of_decimal, 98, (7, 10), s_b = 'ninety eight and seven tenths')
        self.tell_about(name_of_decimal, 0, (1, 10), s_b = 'one tenth')
        self.tell_about(name_of_decimal, 0, (1, 100), s_b = 'one one hundredth')
        self.tell_about(name_of_decimal, 0, (1, 1000), s_b = 'one one thousandth')
        self.tell_about(name_of_decimal, 0, (70, 1000), s_b = 'seventy thousandths')
        self.tell_about(name_of_decimal, 0, (0, 0), s_b = 'zero')
        self.tell_about(name_of_decimal, 10, (0, 0), s_b = 'ten')

    def test_name_in_dollars(self):
        self.tell_about(name_in_dollars, 12, 7, s_b = 'twelve dollars and seven cents')
        self.tell_about(name_in_dollars, 0, 7, s_b = 'seven cents')
        self.tell_about(name_in_dollars, 1, 0, s_b = 'one dollar')
        self.tell_about(name_in_dollars, 7, 0, s_b = 'seven dollars')
        self.tell_about(name_in_dollars, 0, 1, s_b = 'one cent')
        self.tell_about(name_in_dollars, 0, 0, s_b = 'zero dollars')

    def test_name_of_number(self):
        self.tell_about(name_of_number, '12', s_b = 'twelve')
        self.tell_about(name_of_number, '98.7', s_b = 'ninety eight and seven tenths')       
        self.tell_about(name_of_number, '$12.5', s_b = 'twelve dollars and five cents')
        self.tell_about(name_of_number, '0.338', s_b = 'three hundred thirty eight thousandths')
        self.tell_about(name_of_number, '1.30', s_b = 'one and thirty hundredths')
        self.tell_about(name_of_number, '00123', s_b = 'one hundred twenty three')

    def test_namify_sentence(self):
        self.tell_about(namify_sentence, 'I have $2, what about you?', s_b = 'I have two dollars, what about you?')
        self.tell_about(namify_sentence, "It's -20 degrees!", s_b = "It's -twenty degrees!")
        self.tell_about(namify_sentence, '22nd century', s_b = 'twenty twond century')
        self.tell_about(namify_sentence, 'Today is Wednesday, September 9, 2015.', s_b = 'Today is Wednesday, September nine, two thousand fifteen.')
       
unittest.main()
