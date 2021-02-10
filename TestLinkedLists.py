import unittest
from DataStructures.LinkedLists import *

class TestLinkedLists(unittest.TestCase):
    def testReverse(self):
        list = LinkedList(1)
        list.append_to_head(2)
        list.append_to_head(10)
        list.append_to_head(5)
        list.append_to_head(8)
        list.append_to_head(5)
        list.append_to_head(3)
        self.assertEqual(list.to_string(), '3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1')
        self.assertEqual(list.reverse().to_string(), '1 -> 2 -> 10 -> 5 -> 8 -> 5 -> 3')

    def testRemoveDupe(self):
        list = LinkedList(10)
        list.append_to_tail(10)
        list.append_to_tail(5)
        list.append_to_tail(100)
        list_no_dupe_with_hash = remove_dupes_hash_table(list)
        list_no_dupe_no_temp = remove_dupes_no_temp(list)
        self.assertEqual(list_no_dupe_with_hash.to_string(), '10 -> 5 -> 100')
        self.assertEqual(list_no_dupe_no_temp.to_string(), '10 -> 5 -> 100')

    def testReturnKthNodeFromLast(self):
        list = LinkedList(10)
        list.append_to_tail(7)
        list.append_to_tail(5)
        list.append_to_tail(100)
        self.assertEqual(return_kth_to_last(list, 2).value, 5)

    def testDeleteNode(self):
        list = LinkedList(10)
        list.append_to_tail(7)
        list.append_to_tail(5)
        list.append_to_tail(100)
        node = list.head.next.next
        delete_node_with_access_to_only_node(node)
        self.assertEqual(list.to_string(), '10 -> 7 -> 100')

    def testPartition(self):
        list = LinkedList(1)
        list.append_to_head(2)
        list.append_to_head(10)
        list.append_to_head(5)
        list.append_to_head(8)
        list.append_to_head(5)
        list.append_to_head(3)
        self.assertEqual(list.to_string(), '3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1')
        partitioned_list = partition(list, 5)
        self.assertEqual(partitioned_list.to_string(), '3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10')

    def testSumLists(self):
        list1 = LinkedList(6)
        list1.append_to_head(1)
        list1.append_to_head(7)
        list2 = LinkedList(2)
        list2.append_to_head(9)
        list2.append_to_head(5)
        self.assertEqual(sum_lists_reversed_order_to_int(list1, list2).to_string(), '2 -> 1 -> 9')
        self.assertEqual(sum_lists_reversed_order_no_int(list1, list2).to_string(), '2 -> 1 -> 9')

        list1 = LinkedList(6)
        list1.append_to_tail(1)
        list1.append_to_tail(7)
        list2 = LinkedList(2)
        list2.append_to_tail(9)
        list2.append_to_tail(5)
        self.assertEqual(sum_lists_forward_order_to_int(list1, list2).to_string(), '9 -> 1 -> 2')

    def testIsPalindrome(self):
        list1 = LinkedList(6)
        list1.append_to_head(1)
        list1.append_to_head(7)
        self.assertFalse(is_palindrome(list1))

        list1 = LinkedList(6)
        list1.append_to_head(1)
        list1.append_to_head(7)
        list1.append_to_tail(1)
        list1.append_to_tail(7)
        self.assertTrue(is_palindrome(list1))

    def testIntersection(self):
        list1 = LinkedList(6)
        list1.append_to_head(1)
        list1.append_to_head(7)

        list2 = LinkedList(6)
        list2.append_to_head(1)
        list2.append_to_head(7)
        list2.append_to_tail(9)
        list2.append_to_tail(5)

        node1 = Node(10)
        node2 = Node(11)
        node3 = Node(12)
        node1.next = node2
        node2.next = node3

        list1_node = list1.head
        while list1_node.next != None:
            list1_node = list1_node.next
        list1_node.next = node1

        list2_node = list2.head
        while list2_node.next != None:
            list2_node = list2_node.next
        list2_node.next = node1

        self.assertEqual(intersection(list1, list2), node1)



if __name__ == '__main__':
    unittest.main()
