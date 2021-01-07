import unittest

def twoNumberSum(array, targetSum):
    d = {}

    for i in range(len(array)):
        target = targetSum - array[i]

        if target in d:
            return [target, array[i]]
        else:
            d[array[i]] = i
    return []


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)