import datetime
from DataStructures.LinkedLists import *

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    # Stack: Last In First Out
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top == None:
            return None
        current_top = self.top
        self.top = self.top.next
        return current_top

    def push(self, value):
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def push_node(self, node):
        node.next = self.top
        self.top = node

    def peek(self):
        return self.top

    def isEmpty(self):
        if self.top == None:
            return True
        return False

class Queue:
    # Queue: First In First Out
    def __init__(self):
        self.first = None
        self.last = self.first

    def enqueue(self, value):
        new_last = Node(value)
        if self.first == None:
            self.first = new_last
            self.last = new_last
        else:
            self.last.next = new_last
            self.last = new_last

    def enqueue_node(self, node):
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        if self.first == None:
            return None
        to_return = self.first
        self.first = self.first.next
        return to_return

    def peek(self):
        return self.first

    def is_empty(self):
        if self.first == None:
            return True
        return False


# Three in One: Use an array to implement 3 stacks
class ArrayAsStack:
    def __init__(self):
        self.container_array = []
        self.container_array.insert(0, [])
        self.container_array.insert(1, [])
        self.container_array.insert(2, [])

    def push(self, value, stack_number):
        # invalid stack number
        if stack_number < 0 or stack_number > 2:
            return
        # Basically, check if there's anything that's empty in the myriad of things we have
        if None in self.container_array:
            insertion_index = self.container_array.index(None)
            self.container_array[stack_number].append(insertion_index)
            self.container_array[insertion_index] = value
        else:
            insertion_index = len(self.container_array)
            self.container_array[stack_number].append(insertion_index)
            self.container_array.insert(insertion_index, value)

    def pop(self, stack_number):
        # invalid stack number
        if stack_number < 0 or stack_number > 2:
            return None
        if len(self.container_array[stack_number]) == 0:
            return None
        pop_index = self.container_array[stack_number][-1]
        item_to_return = self.container_array[pop_index]
        self.container_array[pop_index] = None
        # cut off the last item in the index for the appropriate stack number
        self.container_array[stack_number] = self.container_array[stack_number][:-1]
        return item_to_return

# Stack Min: find min element, need to run in O(1)
class NodeWithMin:
    def __init__(self, value):
        self.min = value
        self.value = value
        self.next = None

class StackWithMin:
    def __init__(self):
        self.top = None

    def min(self):
        return self.top.min

    def push(self, value):
        new_top = NodeWithMin(value)
        if self.top == None:
            new_top.min = value
        else:
            new_top.min = min(value, self.top.min)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        old_top = self.top
        self.top = self.top.next
        return old_top

# Stack of Plates: start a new stack when the old stack gets too many items


# queue via stacks
class QueueViaStack:
    def __init__(self):
        self.first = None
        self.last = None

# sort stack: stack that is sorted, can not use any other data structure type
class SortedStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        pass

# animal shelter
class AnimalShelterNode:
    def __init__(self, value, type):
        self.value = value
        self.type = type
        self.next = None
        self.timestamp = datetime.datetime.now()

class AnimalShelterQueue:
    def __init__(self):
        self.first = None
        self.last = self.first

    def enqueue(self, value, type):
        new_last = AnimalShelterNode(value, type)
        if self.first == None:
            self.first = new_last
            self.last = new_last
        else:
            self.last.next = new_last
            self.last = new_last

    def dequeue(self):
        old_first = self.first
        self.first = old_first.next
        return old_first

    def peek(self):
        return self.first

    def is_empty(self):
        if self.first == None:
            return True
        return False

class AnimalShelter:
    def __init__(self):
        self.dog_queue = AnimalShelterQueue()
        self.cat_queue = AnimalShelterQueue()

    def enqueue(self, value, type):
        if type == 'cat':
            self.cat_queue.enqueue(value, type)
        elif type == 'dog':
            self.dog_queue.enqueue(value, type)

    def dequeueAny(self):
        if self.dog_queue.is_empty():
            return self.cat_queue.dequeue()
        if self.cat_queue.is_empty():
            return self.dog_queue.dequeue()
        dog_timestamp = self.dog_queue.peek().timestamp
        cat_timestamp = self.cat_queue.peek().timestamp
        if dog_timestamp < cat_timestamp:
            return self.dog_queue.dequeue()
        else:
            return self.cat_queue.dequeue()

    def dequeueDog(self):
        return self.dog_queue.dequeue()

    def dequeueCat(self):
        return self.cat_queue.dequeue()
