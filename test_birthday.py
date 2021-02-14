from unittest import TestCase
from main import Birthday_candles

class TestBirthdayCakeCandles(TestCase):
    def tests_if_birthday_candles_exist(self):
        if Birthday_candles([]):
            return

    def tests_if_birthday_candles_is_recieving_a_parameter(self):
        assert result.arr == [1, 2, 3, 3]

    def tests_if_counting_tallest_exists(self):
        if result.counting_tallest():
            return

    def tests_counting_tallest(self):
        assert result.counting_tallest() == 2

result = Birthday_candles([1, 2, 3, 3])
