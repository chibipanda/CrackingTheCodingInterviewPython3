import unittest
import time

# Recursive does not work, for some reason
def recursive(input_set):
    if len(input_set) == 0:
        return [[]]
    old_subsets = recursive(input_set[:-1])
    new_subsets = old_subsets.copy()
    for i in old_subsets:
        # add the extra item
        temp = i.copy()
        temp.append(input_set[-1])
        new_subsets.append(temp)
    new_subsets.sort()
    return new_subsets

def iterative(input_set):
    if len(input_set) == 0:
        return None
    set_to_return = [[]]
    for i in input_set:
        current_set = []
        for j in set_to_return:
            temp = j.copy()
            temp.append(i)
            current_set.append(temp)
        set_to_return.extend(current_set)
    set_to_return.sort()
    return set_to_return


# Test Class. Too lazy to start a new file
class TestPowerSet(unittest.TestCase):
    def testRecursion(self):
        self.assertEqual(recursive([1, 2]), [[], [1], [2], [1, 2]])
        self.assertEqual(recursive([1, 2, 3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def testIterative(self):
        self.assertEqual(iterative([1, 2]), [[], [1], [2], [1, 2]])
        self.assertEqual(iterative([1, 2, 3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

if __name__ == '__main__':
    unittest.main()