import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append_to_tail(self, value):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = Node(value)

    def append_to_head(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def delete_node_with_value(self, value):
        curr_node = self.head
        while curr_node.next != None:
            if curr_node.next.value == value:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def delete_node(self, node):
        curr_node = self.head
        while curr_node.next != None:
            if curr_node.next == node:
                curr_node.next = node.next
                return
            curr_node = curr_node.next

    def to_string(self):
        to_return = ''
        curr_node = self.head
        while curr_node.next != None:
            to_return += str(curr_node.value) + ' -> '
            curr_node = curr_node.next
        to_return += str(curr_node.value)
        return to_return

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self

    def get_size(self):
        item_count = 1
        current = self.head
        while current.next != None:
            item_count += 1
            current = current.next
        return item_count

    def get_tail(self):
        current = self.head
        while current.next != None:
            current = current.next
        return current

# Remove Dupes
def remove_dupes_hash_table(list):
    vals = {}
    list_copy = copy.deepcopy(list)
    curr_node = list_copy.head
    while curr_node.next != None:
        if curr_node.value in vals:
            list_copy.delete_node(curr_node)
        vals[curr_node.value] = 1
        curr_node = curr_node.next
    return list_copy

def remove_dupes_no_temp(list):
    list_copy = copy.deepcopy(list)
    curr_node = list_copy.head
    comparison_node = curr_node.next
    while curr_node.next != None:
        while comparison_node.next != None:
            if curr_node.value == comparison_node.value:
                list_copy.delete_node(comparison_node)
            comparison_node = comparison_node.next
        curr_node = curr_node.next
    return list_copy

# Return K-th to Last
def return_kth_to_last(list, k):
    curr_node = list.head
    forward_node = list.head
    for i in range(k - 1):
        if forward_node.next == None:
            return None
        forward_node = forward_node.next
    while forward_node.next != None:
        curr_node = curr_node.next
        forward_node = forward_node.next
    return curr_node

# Delete Middle Node
def delete_node_with_access_to_only_node(node):
    node.value = node.next.value
    node.next = node.next.next

# Partition
def partition(list, value):
    curr_node = list.head
    left_part = LinkedList(curr_node.value)
    right_part = LinkedList(curr_node.value)
    left_has_begun = False
    right_has_begun = False
    while curr_node != None:
        if curr_node.value < value:
            if left_has_begun:
                left_part.append_to_tail(curr_node.value)
            else:
                left_part.head.value = curr_node.value
                left_has_begun = True
        else:
            if right_has_begun:
                right_part.append_to_tail(curr_node.value)
            else:
                right_part.head.value = curr_node.value
                right_has_begun = True
        curr_node = curr_node.next
    end_of_left_node = left_part.head
    while end_of_left_node.next != None:
        end_of_left_node = end_of_left_node.next
    end_of_left_node.next = right_part.head
    return left_part

# Sum Lists
def sum_lists_reversed_order_to_int(list1, list2):
    number1 = 0
    number2 = 0
    curr_node_1 = list1.head
    curr_exp = 0
    while curr_node_1 != None:
        number1 += curr_node_1.value * (10 ** curr_exp)
        curr_exp += 1
        curr_node_1 = curr_node_1.next
    curr_node_2 = list2.head
    curr_exp = 0
    while curr_node_2 != None:
        number2 += curr_node_2.value * (10 ** curr_exp)
        curr_exp += 1
        curr_node_2 = curr_node_2.next
    sum = number1 + number2
    return_list = LinkedList(sum % 10)
    sum = sum // 10
    while sum > 0:
        return_list.append_to_tail(sum % 10)
        sum = sum // 10
    return return_list

def sum_lists_reversed_order_no_int(list1, list2):
    curr_node_1 = list1.head
    curr_node_2 = list2.head
    carry = 0
    return_list = LinkedList(curr_node_1.value)
    return_list_started = False
    while curr_node_1 != None and curr_node_2 != None:
        sum = curr_node_2.value + curr_node_1.value + carry
        remainder = sum % 10
        carry = sum // 10
        if not return_list_started:
            return_list.head.value = remainder
            return_list_started = True
        else:
            return_list.append_to_tail(remainder)
        curr_node_1 = curr_node_1.next
        curr_node_2 = curr_node_2.next
    while curr_node_1 != None:
        sum = curr_node_1.value + carry
        remainder = sum % 10
        carry = sum // 10
        return_list.append_to_tail(remainder)
        curr_node_1 = curr_node_1.next
    while curr_node_2 != None:
        sum = curr_node_2.value + carry
        remainder = sum % 10
        carry = sum // 10
        return_list.append_to_tail(remainder)
        curr_node_2 = curr_node_2.next
    return return_list


def sum_lists_forward_order_to_int(list1, list2):
    number1 = 0
    number2 = 0
    curr_node_1 = list1.head
    while curr_node_1 != None:
        number1 *= 10
        number1 += curr_node_1.value
        curr_node_1 = curr_node_1.next
    curr_node_2 = list2.head
    while curr_node_2 != None:
        number2 *= 10
        number2 += curr_node_2.value
        curr_node_2 = curr_node_2.next
    sum = number1 + number2
    return_list = LinkedList(sum % 10)
    sum = sum // 10
    while sum > 0:
        return_list.append_to_head(sum % 10)
        sum = sum // 10
    return return_list

def sum_lists_forward_order_no_int(list1, list2):
    number1 = 0
    number2 = 0
    curr_node_1 = list1.head
    while curr_node_1 != None:
        number1 *= 10
        number1 += curr_node_1.value
        curr_node_1 = curr_node_1.next
    curr_node_2 = list2.head
    while curr_node_2 != None:
        number2 *= 10
        number2 += curr_node_2.value
        curr_node_2 = curr_node_2.next
    sum = number1 + number2
    return_list = LinkedList(sum % 10)
    sum = sum // 10
    while sum > 0:
        return_list.append_to_head(sum % 10)
        sum = sum // 10
    return return_list

# Palindrome
def is_palindrome(list):
    reverse_list = copy.deepcopy(list).reverse()
    curr_node = list.head
    reverse_node = reverse_list.head
    while curr_node != None:
        if reverse_node == None:
            return False
        if curr_node.value != reverse_node.value:
            return False
        curr_node = curr_node.next
        reverse_node = reverse_node.next
    if curr_node == None and reverse_node != None:
        return False
    return True

# Intersection
def intersection(list1, list2):
    tail1 = list1.get_tail()
    tail2 = list2.get_tail()
    if tail1 != tail2:
        return None
    size1 = list1.get_size()
    size2 = list2.get_size()
    size_difference = abs(size1 - size2)
    longer_list = list1
    shorter_list = list2
    if size1 < size2:
        longer_list = list2
        shorter_list = list1
    longer_list_pointer = longer_list.head
    shorter_list_pointer = shorter_list.head
    for i in range(size_difference):
        longer_list_pointer = longer_list_pointer.next
    while longer_list_pointer != None and shorter_list_pointer != None:
        if longer_list_pointer == shorter_list_pointer:
            return longer_list_pointer
        longer_list_pointer = longer_list_pointer.next
        shorter_list_pointer = shorter_list_pointer.next
    return None

# Loop Detection
def loop_detection(list):
    pass