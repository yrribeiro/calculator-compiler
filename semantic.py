from collections import deque
from lexical import printtl


class BinaryTreeNode(object):
    def __init__(self, data):
        """
        Initialize the tree with user expression(algebraic expression)

        Args:
            data(str): string representation of math expression
        """
        self.data = data
        self.right = None
        self.left = None
        self.operator = False


    def __repr__(self) -> str:
        """Return a string representation of this parse tree node."""
        return 'ParseTreeNode({!r})'.format(self.data)

    def is_leaf(self) -> bool:
        """Return True if this node is a leaf(that is operand)."""
        return self.left is None and self.right is None


class BinaryExpressionTree(object):
    def __init__(self, expression: str = None):
        """
        Initialize the tree with user expression(math expression)

        Args:
            expression(str): string representation of algebraic expression
        """
        self.root = None
        self.size = 0

        if expression is not None:
            self.insert(expression)

    def __repr__(self) -> str:
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self) -> bool:
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def insert(self, expression: str):
        """
        Insert the postfix expression into the tree using stack
        """
        postfix_exp = self.infix_to_postfix(expression)
        stack = deque()
        char = postfix_exp[0]
        node = BinaryTreeNode(char)

        stack.appendleft(node)

        i = 1
        while len(stack) != 0:
            char = postfix_exp[i]
            if '.' in char or char.isdigit():
                node = BinaryTreeNode(char)
                stack.appendleft(node)
            else:
                operator_node = BinaryTreeNode(char)
                operator_node.operator = True
                right_child = stack.popleft()
                left_child = stack.popleft()
                operator_node.right = right_child
                operator_node.left = left_child
                stack.appendleft(operator_node)
                if len(stack) == 1 and i == len(postfix_exp) - 1:
                    self.root = stack.popleft()
            i += 1
            self.size += 1

    def items_in_order(self) -> list:
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            self._traverse_in_order_recursive(self.root, items.append)
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """
        Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) we are visiting each node
        Memory usage: O(n) when node is visited we are adding new item to list
        """

        if(node):
            self._traverse_in_order_recursive(node.left, visit)

            visit(node.data)
            self._traverse_in_order_recursive(node.right, visit)

    def evaluate(self, node=None) -> float:
        """
        Calculate this tree expression recursively
        Args:
            node(BinaryTreeNode): starts at the root node
        """
        # initialize

        if node is None:
            node = self.root

        # empty tree
        if node is None:
            return 0

        # check if we are at the leaf, it means it is a operand
        if node.is_leaf():
            val = float(node.data)

            return val

        left_value = self.evaluate(node.left)
        right_value = self.evaluate(node.right)

        # addition
        if node.data == "+":

            return left_value + right_value
        # subtraction
        elif node.data == "-":
            return left_value - right_value
        # division
        elif node.data == "/":
            return left_value / right_value
        # multiplication
        elif node.data == "*":
            return left_value * right_value
        # power
        else:
            return left_value ** right_value

    def infix_to_postfix(self, infix_input: list) -> list:
        """
        Converts infix expression to postfix.
        Args:
            infix_input(list): infix expression user entered
        """

        precedence_order = {'+': 0, '-': 0, '*': 1, '/': 1}
        associativity = {'+': "LR", '-': "LR", '*': "LR", '/': "LR"}


        i = 0
        postfix = []
        operators = "+-/*^"
        stack = deque()
        while i < len(infix_input):

            char = infix_input[i]
            # print(f"char: {char}")
            # check if char is operator
            if char in operators:
                if len(stack) == 0 or stack[0] == '(':
                    stack.appendleft(char)
                    i += 1
                else:
                    top_element = stack[0]
                    if precedence_order[char] == precedence_order[top_element]:
                        if associativity[char] == "LR":
                            popped_element = stack.popleft()
                            postfix.append(popped_element)
                        elif associativity[char] == "RL":
                            stack.appendleft(char)
                            i += 1
                    elif precedence_order[char] > precedence_order[top_element]:
                        stack.appendleft(char)
                        i += 1
                    elif precedence_order[char] < precedence_order[top_element]:
                        popped_element = stack.popleft()
                        postfix.append(popped_element)
            elif char == '(':
                stack.appendleft(char)
                i += 1
            elif char == ')':
                top_element = stack[0]
                while top_element != '(':
                    popped_element = stack.popleft()
                    postfix.append(popped_element)
                    top_element = stack[0]
                stack.popleft()
                i += 1
            else:
                postfix.append(char)
                i += 1
            #     print(postfix)
            # print(f"stack: {stack}")

        if len(stack) > 0:
            for i in range(len(stack)):
                postfix.append(stack.popleft())
        # while len(stack) > 0:
        #     postfix.append(stack.popleft())

        return postfix


def semantic():
    printtl(out_type='SEMANTIC')
    user_input = "5+(2*8)"

    tree_obj = BinaryExpressionTree(user_input)

    # print(f"Tree: {tree_obj}")
    # print(tree_obj.items_in_order())
    print(f'Valor da expressão = {tree_obj.evaluate()}')