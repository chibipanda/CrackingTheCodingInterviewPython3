import unittest

'''
A = [2, 3, 4]
B = [1, 3, 1] ([100, 200, 300])
C = [2, 1, 1] ([1000, 2000])
A = [1, 2, 3, 4,         5, 6, 7, 8,         9, 10, 11, 12,      13, 14, 15, 16,     17, 18, 19, 20, 21, 22, 23, 24]
B = [100, 100, 100, 100, 200, 200, 200, 200, 300, 300, 300, 300, 100, 100, 100, 100, 200, 200, 200, ...
C = [1000, 1000, 1000, 1000, 1000, 1000,
'''

def add_broadcast(shape_1, input_1, shape_2, input_2):
    # Basically, shape_1 can be chopped from the front and recursed on the last 2 elements.
    # Check if needs replication.
    # If the second element of the shape array is 1, we need to copy the input array (the second element of
    # the other shape array) times
    # Same thing with shape_2
    # Base case:
    # 1. if there is only 1 element in shape_1 (and shape_2), add them like normal array
    # 2. if there is more than 1 element, add them pairwise

    if len(shape_1) == 1 and len(shape_2) == 1:
        result = []
        for i in range(len(input_1)):
            result.append(input_1[i] + input_2[i])
        return result

    # Otherwise, check if needs replication
    replicated_1 = input_1.copy()
    replicated_2 = input_2.copy()
    if shape_1[1] == 1:
        # Get number of replication
        rep = shape_2[1]
        replicated_1 = []
        for j in range(rep):
            replicated_1.extend(input_1)

    if shape_2[1] == 1:
        # Get number of replication
        rep = shape_1[1]
        replicated_2 = []
        for j in range(rep):
            replicated_2.extend(input_2)

    # Need to chop up the array and recurse
    divide_by_1 = shape_1[0]
    divide_by_2 = shape_2[0]
    next_shape_1 = shape_1[1:]
    next_shape_2 = shape_2[1:]
    next_length_1 = len(input_1) // divide_by_1
    next_length_2 = len(input_2) // divide_by_2
    sum = []
    for i in range(max(divide_by_1, divide_by_2)):
        next_input_1 = input_1[i * next_length_1: (i+1) * next_length_1]
        next_input_2 = input_2[i * next_length_2: (i+1) * next_length_2]
        sum.extend(add_broadcast(next_shape_1, next_input_1, next_shape_2, next_input_2))




def can_broadcast(shape_1, shape_2):
    padded_1 = shape_1.copy()
    padded_2 = shape_2.copy()
    # Pad the shorter arrays with 1
    if len(shape_1) > len(shape_2):
        difference = len(shape_1) - len(shape_2)
        padded_2 = [1 for x in range(difference)]
        padded_2.extend(shape_2)
    if len(shape_2) > len(shape_1):
        difference = len(shape_2) - len(shape_1)
        padded_1 = [1 for x in range(difference)]
        padded_1.extend(shape_1)
    # Compare 2 array one by one
    for i in range(len(padded_1)):
        if padded_1[i] == 1 or padded_2[i] == 1:
            continue
        if padded_1[i] != padded_2[i]:
            return False
    return True


class TestBroadcast(unittest.TestCase):
    def testCanBroadcast(self):
        self.assertTrue(can_broadcast([1], [1]))
        self.assertTrue(can_broadcast([2, 3, 4], [4]))
        self.assertTrue(can_broadcast([2, 3, 4], [3, 4]))

    def testIllegalBroadcast(self):
        self.assertFalse(can_broadcast([2], [3]))
        self.assertFalse(can_broadcast([2, 3, 4], [5]))
