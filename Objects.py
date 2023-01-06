class Token():
    def __init__(self, lexeme='', char_type=None):
        self.lexeme  = lexeme
        self.char_type  = char_type

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
