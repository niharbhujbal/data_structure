class Tree:
    """
    An Binary Tree Data Structure
    """

    class Node:
        """
        An Tree node
        """

        def __init__(self, value):
            """
            Intitalisation Tree Node
            -------------
            Parameters
            -------------
            value : str
                value of the node
            """
            self.value = value
            self.left_child_node = None
            self.right_child_node = None

    def __init__(self):
        """
        Intitalisation Tree
        """
        self.root_node = None

    def insert(self, value):
        """
        Insert a node into tree
        -------------
        Parameters
        -------------
        value : str
            value of the node you want to insert
        """
        if self.root_node is None:
            self.root_node = self.Node(value)
        else:
            # we have to find the parant for our node first and then add the node to appropriate side
            current = self.root_node
            while True:
                if value < current.value:
                    if current.left_child_node is None:
                        current.left_child_node = self.Node(value)
                        break
                    else:
                        current = current.left_child_node
                else:
                    if current.right_child_node is None:
                        current.right_child_node = self.Node(value)
                        break
                    else:
                        current = current.right_child_node

    def find(self, value):
        """
        Check if the node is present in the tree
        -------------
        Parameters
        -------------
        value : str
            value of the node you want to check
        """
        if self.root_node is None:
            return False
        else:
            current = self.root_node
            while True:
                if value < current.value:
                    if current.left_child_node is None:
                        return False
                    else:
                        current = current.left_child_node
                elif value == current.value:
                    return True
                else:
                    if current.right_child_node is None:
                        return False
                    else:
                        current = current.right_child_node

    def traverse(self, method: str = "pre-order"):
        """
        Traverse the tree
        -----------
        Parameters
        -----------
        method - str
          Method we want to use for Traversal
          1. 'pre-order' = Depth-First,Pre-Order
          Root,Left,Right
          2. 'in-order' = Depth-First,In-Order
          Left, Root, Right
          3. 'post-order' = Depth-First,Post-Order
          Left, Right, Root
        """
        self._traverse(self.root_node, method)

    def _traverse(self, root, method):
        """
        Private method to impliment the traversal with recursion
        -----------
        Parameters
        -----------
        root - self.Node
            node from which we want traverse
        method - str
            Method we want to use for Traversal
        """
        # terminate condition for
        if root is None:
            return None
        if method == "pre-order":
            print(root.value)
            self._traverse(root.left_child_node, method)
            self._traverse(root.right_child_node, method)
        if method == "in-order":
            self._traverse(root.left_child_node, method)
            print(root.value)
            self._traverse(root.right_child_node, method)
        if method == "post-order":
            self._traverse(root.left_child_node, method)
            self._traverse(root.right_child_node, method)
            print(root.value)

    def height(self):
        """
        Returns the Height of Tree
        """
        if self.root_node is None:
            return -1
        return self._height(self.root_node)

    def _height(self, root):
        """
        Private method to impliment the height with recursion
        this method uses post order trversal
        -----------
        Parameters
        -----------
        root - self.Node
            node from which we want to find height
        """
        if root.left_child_node is None and root.right_child_node is None:
            return 0
        if root.left_child_node is not None and root.right_child_node is None:
            return 1 + self._height(root.left_child_node)
        if root.left_child_node is None and root.right_child_node is not None:
            return 1 + self._height(root.right_child_node)
        return 1 + max(
            self._height(root.left_child_node), self._height(root.right_child_node)
        )

    def equality(self, tree):
        """
        Check whether two trees are equal
        """
        if tree is None:
            return False
        return self._equality(self.root_node, tree.root_node)

    def _equality(self, first_node, second_node):
        """
        Private method to impliment the equality with recursion
        this method uses pre order trversal
        -----------
        Parameters
        -----------
        first_node - self.Node
            first node we want to companre against
        second_node - self.node
            second node we want to compare the node to
        """
        if first_node is None and second_node is None:
            return True
        if first_node is not None and second_node is not None:
            return (
                first_node.value == second_node.value
                and self._equality(
                    first_node.left_child_node, second_node.left_child_node
                )
                and self._equality(
                    first_node.right_child_node, second_node.right_child_node
                )
            )
        return False

    def isBinarySearchTree(self):
        """
        check if the tree is binary seach tree
        """
        if self.root_node is None:
            return True
        return self._isBinarySearchTree(self.root_node, float("-inf"), float("inf"))

    def _isBinarySearchTree(self, node, min_value, max_value):
        """
        Private method to impliment the check of binary seach tree with recursion
        -----------
        Parameters
        -----------
        node - self.Node
            node we want to check
        min_value - float
            min value that node should have to be a valid binary tree
        max_value - float
            max value that node should have to be a valid binary tree
        """
        if node.left_child_node is None and node.right_child_node is None:
            return True
        if (
            min_value < node.value < max_value
            and self._isBinarySearchTree(node.left_child_node, min_value, node.value)
            and self._isBinarySearchTree(node.right_child_node, node.value, max_value)
        ):
            return True
        return False

    def GetKthNode(self, k):
        """
        Get the value of k th node from root node
        -----------
        Parameters
        -----------
        k - int
            k th node from the root node
        """
        kth_node_list = []
        if self.root_node is None:
            return kth_node_list
        self._GetKthNode(k, self.root_node, kth_node_list)
        return kth_node_list

    def _GetKthNode(self, k, node, kth_node_list):
        """
        Private implementation of getting the kth node with recursion
        -----------
        Parameters
        -----------
        k - int
            k th node from the root node
        node - self.node
            node from which we want the kth value
        kth_node_list - list
            list of the kth distance nodes
        """
        if k == 0:
            kth_node_list.append(node.value)
        if node.left_child_node is not None:
            self._GetKthNode(k - 1, node.left_child_node, kth_node_list)
        if node.right_child_node is not None:
            self._GetKthNode(k - 1, node.right_child_node, kth_node_list)

    def traversalLevelOrder(self):
        """
        Level order traversal on the tree
        """
        list_ = []
        for i in range(self.height() + 1):
            list_.extend(self.GetKthNode(i))
        return list_


class AVLTrre(Tree):
    """
    An AVL (Adelson-Velsky and Landis) Tree Data Structure
    """

    class AVLNode(Tree.Node):
        """
        An AVL Node
        """

        def __init__(self, value):
            """
            Intitalisation Node
            -------------
            Parameters
            -------------
            value : int
                value of the node
            """
            super().__init__(value)
            self.left_height = 0
            self.right_height = 0

    def __init__(self):
        """
        Intitalisation Tree
        """
        super().__init__()

    def insert(self, value):
        """
        insert a node into tree
        -------------
        Parameters
        -------------
        value : int
            value of the node
        """
        self.root_node = self._insert(self.root_node, value)

    def _insert(self, root, value):
        """
        Private method to insert a node into tree
        -------------
        Parameters
        -------------
        root - self.AVLNode
            node where you want to insert the value
        value : int
            value of the node
        """
        if root is None:
            return self.AVLNode(value)
        elif value < root.value:
            root.left_child_node = self._insert(root.left_child_node, value)
            root.left_height += 1
        else:
            root.right_child_node = self._insert(root.right_child_node, value)
            root.right_height += 1

        root = self._balance(root)

        return root

    def _balance_factor(self, node):
        """
        Private method to calculate balance factor = left height - right height
        -------------
        Parameters
        -------------
        node - self.AVLNode
            node for which you want to calculate balance factor for
        """
        return node.left_height - node.right_height

    def _balance(self, root):
        """
        Private method to balance tree
        -------------
        Parameters
        -------------
        root - self.AVLNode
            root node on which you want balance the tree
        """
        # we have to perform right rotation
        if self._balance_factor(root) > 1:
            # if this satisfies then we have to do LR
            if self._balance_factor(root.left_child_node) == -1:
                self._left_rotate(root.left_child_node)
            root = self._right_rotate(root)
        # we have to perform left rotation
        if self._balance_factor(root) < -1:
            # if this satisfies then we have to do RL
            if self._balance_factor(root.right_child_node) == 1:
                root = self._right_rotate(root.right_child_node)
            root = self._left_rotate(root)

        return root

    def _right_rotate(self, root):
        """
        Private method to perform right rotation
        -------------
        Parameters
        -------------
        node - self.AVLNode
            node for which you want to perform rotation
        """
        new_root = root.left_child_node
        root.left_child_node = new_root.right_child_node
        new_root.right_child_node = root

        # reset the height of root
        root = self._height_reset(root)
        root = self._height_reset(new_root)

        return new_root

    def _left_rotate(self, root):
        """
        Private method to perform left rotation
        -------------
        Parameters
        -------------
        node - self.AVLNode
            node for which you want to perform rotation
        """
        new_root = root.right_child_node
        root.right_child_node = new_root.left_child_node
        new_root.left_child_node = root

        # reset the height of root
        root = self._height_reset(root)
        new_root = self._height_reset(new_root)

        return new_root

    def _height_reset(self, node):
        """
        Private method to reset all left and right heights
        -------------
        Parameters
        -------------
        node - self.AVLNode
            node for you want to reset heights
        """
        if node.left_child_node is not None:
            node.left_height = self._height(node.left_child_node) + 1
        else:
            node.left_height = 0
        if node.right_child_node is not None:
            node.right_height = self._height(node.right_child_node) + 1
        else:
            node.right_height = 0

        return node


class Heap:
    """
    An Heap Data Structure
    """

    def __init__(self):
        """
        Intitalisation of Heap
        """
        self.items = []
        self.size = 0

    def insert(self, value):
        """
        insert a value into heap
        -------------
        Parameters
        -------------
        value : int
            value to be inserted
        """
        self.items.append(value)
        self.size += 1
        self._bubble_up()

    def _bubble_up(self):
        """
        Private method to bubble up the large value at the top of the heap
        """
        child_index = self.size - 1
        # in last iterations index changes to -1 and executs one more time to avoid that we have to check if index is greater than zero
        while (
            child_index > 0
            and self.items[child_index]
            > self.items[self._get_parent_index(child_index)]
        ):
            parent_index = self._get_parent_index(child_index)
            # swap
            self.items[child_index], self.items[parent_index] = (
                self.items[parent_index],
                self.items[child_index],
            )
            # change indexes
            child_index = parent_index

    def _get_parent_index(self, index):
        """
        Private method to get parent index
        """
        return (index - 1) // 2

    def remove(self):
        """
        Remove top node from heap
        """
        if self.size == 0:
            raise Exception("Heap is Empty")
        self.size -= 1
        removed_item = self.items[0]
        self.items[0] = self.items[-1]
        self.items = self.items[: self.size]
        self._bubble_down()
        return removed_item

    def _bubble_down(self):
        """
        Private method to get the second larget value at the top of heap after deleting
        """
        index = 0
        while (index <= self.size) and not (self._is_valid_parent(index)):
            if self._get_left_child(index) is None:
                larger_child_index = self._get_right_child_index(index)
            if self._get_right_child(index) is None:
                larger_child_index = self._get_left_child_index(index)
            # they have both child
            else:
                if self._get_left_child(index) > self._get_right_child(index):
                    larger_child_index = self._get_left_child_index(index)
                else:
                    larger_child_index = self._get_right_child_index(index)
            # swap
            self.items[index], self.items[larger_child_index] = (
                self.items[larger_child_index],
                self.items[index],
            )

            index = larger_child_index

    def _get_left_child_index(self, parent_index):
        """
        get left child index
        """
        return (parent_index * 2) + 1

    def _get_right_child_index(self, parent_index):
        """
        get right child index
        """
        return (parent_index * 2) + 2

    def _get_left_child(self, index):
        """
        get left child
        """
        if self._get_left_child_index(index) >= self.size:
            return None
        else:
            return self.items[self._get_left_child_index(index)]

    def _get_right_child(self, index):
        """
        get right child
        """
        if self._get_right_child_index(index) >= self.size:
            return None
        return self.items[self._get_right_child_index(index)]

    def _is_valid_parent(self, index):
        """
        check if the parent is valid
        """
        if self._get_left_child(index) is None and self._get_right_child(index) is None:
            return True
        elif self._get_left_child(index) is None:
            return self.items[index] >= self._get_right_child(index)
        elif self._get_right_child(index) is None:
            return self.items[index] >= self._get_left_child(index)
        else:
            return (self.items[index] >= self._get_left_child(index)) and (
                self.items[index] >= self._get_right_child(index)
            )


class PriorityQueue(Heap):
    """
    An priority queue class using heap data structure
    """

    def __init__(self):
        """
        Intitalisation Priority Queue
        """
        super().__init__()

    def eneueue(self, item):
        """
        add the item in the queue
        -------------
        Parameters
        -------------
        item : int
            item to be inserted
        """
        self.insert(item)

    def dequeue(self):
        """
        get the first value from the queue
        """
        return self.remove()

    def isEmpty(self):
        """
        check if the queue is empty
        """
        return len(self.items) == 0


def heapify(array):
    """
    We arrange the values in the array like heap would given an array
    -------------
    Parameters
    -------------
    array : list
        array to be converted
    """
    for i in range(len(array)):
        array = heapify_bubble_down(array, i)
    return array


def heapify_bubble_down(array, index):
    """
    bubble down method for heapify algorithm
    -------------
    Parameters
    -------------
    array : list
        array to be converted
    index : int
        inedx from which you want to bubble down
    """
    large_index = index
    left_child_index = index * 2 + 1
    right_child_index = index * 2 + 2
    if left_child_index < len(array) and array[left_child_index] > array[large_index]:
        large_index = left_child_index
    elif (
        right_child_index < len(array) and array[right_child_index] > array[large_index]
    ):
        large_index = right_child_index

    if index == large_index:
        return array
    else:
        array[index], array[large_index] = array[large_index], array[index]
        array = heapify_bubble_down(array, large_index)
        return array


class Tries:
    """
    An Tries Data Structure
    """

    class Node:
        """
        An Tries Node
        """

        def __init__(self, char):
            """
            Intitalisation Node
            -------------
            Parameters
            -------------
            char : str
                value of the node
            """
            self.value = char
            self.childeren = {}
            self.is_end_of_word = None

        def has_child(self, char):
            """
            check if the child node with the char is present
            -------------
            Parameters
            -------------
            char : str
                value of the node
            """
            return char in self.childeren.keys()

    def __init__(self):
        """
        Intitalisation Tries
        """
        self.root = self.Node(" ")

    def insert(self, word):
        """
        insert a word into tries
        -------------
        Parameters
        -------------
        word : str
            word that we want to insert
        """
        current = self.root
        for char in word:
            if not current.has_child(char):
                current.childeren[char] = self.Node(char)
            current = current.childeren[char]
        current.is_end_of_word = True

    def contains(self, word):
        """
        check if the word is present in the tries
        -------------
        Parameters
        -------------
        word : str
            word that we want to check
        """
        if word is None:
            return False
        current = self.root
        for char in word:
            if current.has_child(char):
                current = current.childeren[char]
            else:
                return False
        else:
            return current.is_end_of_word

    def traversal(self, method):
        """
        traverse the tries
        -------------
        Parameters
        -------------
        method : str
            type of traversal
            pre-order = pre order traversal
            post-order = post order traversal
        """
        self._traversal(self.root, method)

    def _traversal(self, node, method="pre-order"):
        """
        private method to traverse the tries
        -------------
        Parameters
        -------------
        method : str
            type of traversal
        """
        if method == "pre-order":
            print(node.value)
        for key, value in node.childeren.items():
            self._traversal(value)
        if method == "post-order":
            print(node.value)

    def remove(self, word):
        """
        remove the word from tries
        -------------
        Parameters
        -------------
        word : str
            word we want to remove
        """
        self._remove(self.root, word, 0)

    def _remove(self, node, word, index):
        """
        private method to remove the word from tries
        -------------
        Parameters
        -------------
        node : self.Node
            type of traversal
        word : str
            word we want to remove
        index : int
            index of the word for matching with node
        """
        if index == len(word) or word is None:
            return None
        char = word[index]
        child_node = node.childeren[char]
        if child_node is None:
            return None

        self._remove(child_node, word, index + 1)
        # dosen't have any childern
        if (
            len(child_node.childeren) == 0 and not child_node.is_end_of_word
        ) or index == len(word) - 1:
            del node.childeren[char]

    def find_auto_complete_words(self, prefix):
        """
        find words from tries to auto complete
        -------------
        Parameters
        -------------
        prefix : str
            prefix of words to auto complete
        """
        last_node = self._find_last_node(prefix)
        return self._find_auto_complete_words(prefix, last_node)

    def _find_auto_complete_words(self, prefix, node):
        """
        Private method to find words from tries to auto complete
        -------------
        Parameters
        -------------
        prefix : str
            prefix of words to auto complete
        node : self.Node
            last node of the auto complete
        """
        word_list = []
        for char, child_node in node.childeren.items():
            if child_node.is_end_of_word:
                word_list.append(prefix + char)
            child_word_list = self._find_auto_complete_words(prefix + char, child_node)
            word_list.extend(child_word_list)
        return word_list

    def _find_last_node(self, prefix):
        """
        private method to find the last node for auto complete
        -------------
        Parameters
        -------------
        prefix : str
            prefix of words to auto complete
        """
        index = 0
        node = self.root
        for char in prefix:
            itr_obj = node.childeren.items()
            for child_char, child_node in itr_obj:
                if child_char == char:
                    node = child_node

        return node


class Graph:
    """
    An Graph Data Structure
    """

    class Node:
        """
        Graph Node
        """

        def __init__(self, label):
            """
            Intitalisation of graph node
            """
            self.label = label

    def __init__(self):
        """
        Intitalisation of graph
        """
        self.nodes = {}
        self.adjacency_list = {}

    def add_node(self, label):
        """
        add a node into graph
        -------------
        Parameters
        -------------
        label : str
            label value on the node
        """
        node = self.Node(label)
        self.nodes[label] = node
        self.adjacency_list[node] = []

    def add_edge(self, from_label, to_label):
        """
        add an edge into graph
        -------------
        Parameters
        -------------
        from_label : str
            node label for the orignation node
        to_label : str
            node label for the edge ending node
        """
        if from_label in self.nodes.keys():
            from_node = self.nodes[from_label]
        else:
            raise Exception("Node not present in Graph")
        if to_label in self.nodes.keys():
            to_node = self.nodes[to_label]
        else:
            raise Exception("Node not present in Graph")
        self.adjacency_list[from_node].append(to_node)

    def remove_node(self, label):
        """
        remove node from graph
        -------------
        Parameters
        -------------
        label : str
            label value on the node
        """
        # remove from nodes hashmap
        try:
            node = self.nodes[label]
            del self.nodes[label]
        except:
            raise Exception("Node not present in Graph")
        # remove from every node
        del self.adjacency_list[node]
        for key, value in self.adjacency_list.items():
            if node in value:
                value.remove(node)

    def remove_edge(self, from_label, to_label):
        """
        remove an edge from graph
        -------------
        Parameters
        -------------
        from_label : str
            node label for the orignation node
        to_label : str
            node label for the edge ending node
        """
        if from_label in self.nodes.keys():
            from_node = self.nodes[from_label]
        else:
            raise Exception("Node not present in Graph")
        if to_label in self.nodes.keys():
            to_node = self.nodes[to_label]
        else:
            raise Exception("Node not present in Graph")
        self.adjacency_list[from_node].remove(to_node)

    def traverse_depth_first(self, root_node_label):
        """
        traverse graph with depth first algorithm
        -------------
        Parameters
        -------------
        root_node_label : str
            starting node from which you want start depth first algorithm
        """
        if root_node_label in self.nodes.keys():
            self._traverse_depth_first(self.nodes[root_node_label], set())
        else:
            return None

    def _traverse_depth_first(self, node, traveled_set):
        """
        Private method to implememnt traverse_depth_first
        """
        if node.label not in traveled_set:
            print(node.label)
            traveled_set.add(node.label)
        for child_node in self.adjacency_list[node]:
            traveled_set = self._traverse_depth_first(child_node, traveled_set)
        return traveled_set

    def traverse(self, node_label, traverse_type="depth-first"):
        """
        traverse graph with depth first algorithm
        -------------
        Parameters
        -------------
        node_label : str
            starting node from which you want start traverse algorithm
        traverse_type : str
            type of traverse we want to do
            depth-first = depth first traversal
            breadth-first = breadth first traversal
        """
        node = self.nodes[node_label]
        stack_queue = []
        visited = set()
        stack_queue.append(node)

        while not len(stack_queue) == 0:
            # we use stack for depth
            if traverse_type == "depth-first":
                current = stack_queue[-1]
                stack_queue = stack_queue[:-1]
            # we use queue for breadth first
            elif traverse_type == "breadth-first":
                current = stack_queue[0]
                stack_queue = stack_queue[1:]
            if current in visited:
                continue
            print(current.label)
            visited.add(current)

            for neighbour in self.adjacency_list[current]:
                if neighbour not in visited:
                    stack_queue.append(neighbour)

    def topological_sorting(self):
        """
        Topological sorting of the graph
        """
        stack = []
        visited = set()
        for node in self.nodes.values():
            visited, stack = self._topological_sorting(node, visited, stack)

        sorted_list = [node.label for node in stack]
        return sorted_list

    def _topological_sorting(self, node, visited, stack):
        """
        Private method to implememnt topological_sorting
        """
        if node in visited:
            return visited, stack

        visited.add(node)

        for neighbours in self.adjacency_list[node]:
            visited, stack = self._topological_sorting(neighbours, visited, stack)

        stack.append(node)
        return visited, stack

    def has_cycle(self):
        """
        check if the graph has cycle in it
        """
        for node in self.nodes.values():
            visiting = set()
            if self._has_cycle(node, visiting):
                return True
        return False

    def _has_cycle(self, node, visiting):
        """
        Private method to implememnt has_cycle
        """
        if node in visiting:
            return True
        visiting.add(node)
        for neighbour in self.adjacency_list[node]:
            if self._has_cycle(neighbour, visiting):
                return True
            visiting.remove(neighbour)
        return False
