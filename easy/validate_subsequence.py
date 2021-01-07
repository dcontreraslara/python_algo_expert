def isValidSubsequence(array, sequence):
    i = len(array) - 1
    j = len(sequence) - 1

    while i >= 0:
        if array[i] == sequence[j]:
            j = j - 1
        if j == -1:
            return True
        i = i - 1

    return False


import unittest

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))
