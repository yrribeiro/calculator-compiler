class Token():
    def __init__(self, lexeme='', char_type=None):
        self.lexeme  = lexeme
        self.char_type  = char_type

class Node():
    def __init__(self, data, left=None, right=None, parent=None):
        self.data  = data
        self.left  = left
        self.right  = right
        self.parent = parent
