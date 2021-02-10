from queue import Queue

class DirectedGraphNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False

class DirectedGraph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, value):
        self.root = BinaryTreeNode(value)

    def insert_to_node(self, node, value):
        if value <= node.value:
            if node.left_child != None:
                self.insert_to_node(node.left_child, value)
            else:
                node.left_child = BinaryTreeNode(value)
        if value > node.value:
            if node.right_child != None:
                self.insert_to_node(node.right_child, value)
            else:
                node.right_child = BinaryTreeNode(value)

    def insert(self, value):
        self.insert_to_node(self.root, value)

    def search_from_node(self, node, value):
        if node.value == value:
            return node
        if value <= node.value:
            if node.left_child != None:
                return self.search_from_node(node.left_child, value)
            else:
                return None
        else:
            if node.right_child != None:
                return self.search_from_node(node.right_child, value)
            else:
                return None

    def search(self, value):
        return self.search_from_node(self.root, value)

    def preorder_traversal(self, node):
        print(node.value + "\n")
        if node.left_child != None:
            self.preorder_traversal(node.left_child)
        if node.right_child != None:
            self.preorder_traversal(node.right_child)

    def inorder_traversal(self, node):
        if node.left_child != None:
            self.preorder_traversal(node.left_child)
        print(node.value + "\n")
        if node.right_child != None:
            self.preorder_traversal(node.right_child)

    def postorder_traversal(self, node):
        if node.left_child != None:
            self.preorder_traversal(node.left_child)
        if node.right_child != None:
            self.preorder_traversal(node.right_child)
        print(node.value + "\n")

    def breadth_first_traversal(self, node):
        queue = Queue()
        queue.put(node)

        while not queue.empty():
            element = queue.get()
            print(element.value)
            if element.left_child != None:
                queue.put(element.left_child)
            if element.right_child != None:
                queue.put(element.right_child)

    def get_height_of_node(self, node):
        levels = 0
        current = [node]
        while len(current) > 0:
            levels += 1
            parents = current
            current = []
            for parent in parents:
                if parent.left_child != None:
                    current.append(parent.left_child)
                if parent.right_child != None:
                    current.append(parent.right_child)
        return levels

    def get_tree_height(self):
        return self.get_height_of_node(self.root)


# Route between Nodes
def does_route_exists(graph, source, destination):
    if source == destination:
        return True
    node_queue = Queue()
    source.visited = True
    node_queue.put(source)

    while not node_queue.empty():
        element = node_queue.get()
        if element == destination:
            return True
        else:
            for child in element.children:
                if not child.visited:
                    node_queue.put(child)
                    child.visited = True
    return False

# Minimal Tree
def construct_balanced_tree(input_list):
    if len(input_list) == 0:
        return None
    middle_of_the_list = len(input_list) // 2
    first_half = input_list[:middle_of_the_list]
    last_half = input_list[middle_of_the_list:]
    tree = BinaryTree(last_half[0])
    last_half = last_half[1:]
    left_half = construct_balanced_tree(first_half)
    right_half = construct_balanced_tree(last_half)
    if left_half != None:
        tree.root.left_child = construct_balanced_tree(first_half).root
    if right_half != None:
        tree.root.right_child = construct_balanced_tree(last_half).root
    return tree

# List of Nodes At Depth
def list_of_nodes_per_level(tree):
    levels = []
    current = [tree.root]
    while len(current) > 0:
        levels.append(current)
        parents = current
        current = []
        for parent in parents:
            if parent.left_child != None:
                current.append(parent.left_child)
            if parent.right_child != None:
                current.append(parent.right_child)
    return levels

# Check Balanced
def check_balanced(tree):
    pass




