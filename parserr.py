import ast
from collections import deque

from Objects import Token, Node
from lexical import printtl

global tokens
tokens = []

def push_on_precedence(op_input, op_top_stack):
    '''
    (  >  *  ==  /  >  +  ==  -  >  $
    '''
    reference =  {'(':3, '*':2, '/':2, '+':1, '-':1, '$':0}
    if reference.get(op_input) > reference.get(op_top_stack):
        pass

def buildTree():
    auxList = deque()
    root=Node()
    lastNode=Node()
    flag=0
    leng= len(tokens)
    ops = ('SUM-OP', 'MINUS-OP', 'DIV-OP', 'MUL-OP')
     
    for token in tokens:
        node = Node(token.lexeme)
        if token.char_type == 'DIGIT':
            auxList.appendleft(node)
        if token.char_type in ops:
            node.left=auxList.popleft()
            if(flag==0):
                root = node
                flag = 1
                lastNode=node
            else:
                lastNode.right=node
                lastNode=node

    lastNode.right=Node(tokens[len(tokens-1)].lexeme)

    for node in auxList:
        print(node.data)


def parserr(f):
    operators, operands = deque(), deque()
    operators.append(Token('$', 'EOF'))

    for line in f:
        tk_dict = ast.literal_eval(line)
        tokens.append(
            Token(
                tk_dict.get('lexeme'),
                tk_dict.get('char_type')
            )
        )
    
    paren_stack = deque()
    for i in range(len(tokens)):
        ops = ('SUM-OP', 'MINUS-OP', 'DIV-OP', 'MUL-OP')
        curr_type = tokens[i].char_type
        if (i>0):
            if (curr_type in ops) and (tokens[i-1].char_type in ops):
                raise Exception('erro 1 - dois operadores juntos')
        if (i==0 and (curr_type != 'DIGIT' and curr_type != 'OPEN-PAR')):
            raise Exception('erro 2 - começando com operador')
        
        if curr_type == 'OPEN-PAR':
            paren_stack.appendleft(tokens[i].lexeme)
        elif curr_type == 'CLOSE-PAR':
            if len(paren_stack) > 0:
                paren_stack.popleft()
            else:
                raise Exception('erro 3 - tentando tirar parenteses sem ter')
    
    if len(paren_stack) > 0:
        raise Exception('erro 4 - sobrou parenteses')

    buildTree()
    
    # for token in tokens:
    #     print(token.lexeme)

    # PAR_OUTPUT_FILENAME = 'output_files/parser_out.txt'
        # with open(PAR_OUTPUT_FILENAME, 'w') as output:
            # output.write(str(token_list))

    return '' #PAR_OUTPUT_FILENAME