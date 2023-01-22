from unittest import TestCase
from main import multipy, subtraction, addition


class Test(TestCase):
    def test_multipy(self):

        class TestCase:
            def __init__(self, arr1, arr2, arr_res):
                self.arr1 = arr1
                self.arr2 = arr2
                self.arr_res = arr_res

        for case in [
            TestCase([[2]], [[3]], [[6]]),

            TestCase([[1, 2], [3, 4]], [[1, 2], [3, 4]], [[7, 10], [15, 22]]),

            TestCase([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                     [[30, 36, 42, 0], [66, 81, 96, 0], [102, 126, 150, 0], [0, 0, 0, 0]]),

            TestCase([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                     [[3, 3, 3, 0], [3, 3, 3, 0], [3, 3, 3, 0], [0, 0, 0, 0]])
        ]:
            self.assertEqual(case.arr_res, multipy(case.arr1, case.arr2))

    def test_subtraction(self):
        arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr_res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.assertEqual(arr_res, subtraction(arr1, arr2))

    def test_addition(self):
        arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        arr_res = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
        self.assertEqual(arr_res, addition(arr1, arr2))
