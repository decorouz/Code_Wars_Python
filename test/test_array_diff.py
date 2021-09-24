import unittest

from solutions import array_diff, spinning_words, high_and_low


class TestArrayDiff(unittest.TestCase):
    def test_array_diff(self):
        self.assertEquals(array_diff([1, 2], [1]), [
            2], "a was [1,2], b was [1], expected [2]")
        self.assertEquals(array_diff([1, 2, 2], [1]), [
            2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEquals(array_diff([1, 2, 2], [2]), [
            1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEquals(array_diff([1, 2, 2], []), [
            1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEquals(array_diff([], [1, 2]), [],
                          "a was [], b was [1,2], expected []")
        self.assertEquals(array_diff([1, 2, 3], [1, 2]), [
            3], "a was [1,2,3], b was [1, 2], expected [3]")
        self.assertEquals(spinning_words("Welcome"), "emocleW")


class TestHighAndLow(unittest.TestCase):
    def test_high_and_low(self):
        self.assertEquals(high_and_low(high_and_low(
            "8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9"))


if __name__ == '__main__':
    unittest.main()
