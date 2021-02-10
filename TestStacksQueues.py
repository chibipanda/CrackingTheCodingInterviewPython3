import unittest
from DataStructures.StacksQueues import *

class TestStacksQueues(unittest.TestCase):

    def testArrayAsStack(self):
        stack = ArrayAsStack()
        stack.push(10, 1)
        stack.push(11, 1)
        stack.push(12, 0)
        stack.push(5, 2)
        self.assertEqual(stack.pop(1), 11)
        self.assertEqual(stack.pop(2), 5)
        self.assertEqual(stack.pop(2), None)
        self.assertEqual(stack.pop(0), 12)

    def testMinStacks(self):
        stack = StackWithMin()
        stack.push(5)
        self.assertEqual(stack.min(), 5)
        stack.push(6)
        self.assertEqual(stack.min(), 5)
        stack.push(3)
        self.assertEqual(stack.min(), 3)
        stack.push(7)
        self.assertEqual(stack.min(), 3)
        stack.push(1)
        self.assertEqual(stack.min(), 1)
        stack.pop()
        self.assertEqual(stack.min(), 3)

    def testAnimalShelter(self):
        shelter = AnimalShelter()
        shelter.enqueue("cat1", "cat")
        shelter.enqueue("cat2", "cat")
        shelter.enqueue("cat3", "cat")
        shelter.enqueue("dog1", "dog")

        self.assertEqual(shelter.dequeueAny().value, "cat1")
        self.assertEqual(shelter.dequeueDog().value, "dog1")


if __name__ == '__main__':
    unittest.main()
