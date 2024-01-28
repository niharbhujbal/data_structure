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
