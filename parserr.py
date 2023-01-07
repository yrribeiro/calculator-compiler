import ast
from collections import deque

from Objects import Token
from lexical import printtl

global tokens, ops
ops = ('SUM-OP', '+', 'MINUS-OP', '-', 'DIV-OP', '/', 'MUL-OP', '*')
tokens = []

def has_higher_precedence(op_input, op_top_stack):
    reference =  {'(':6, '/':5, '*':4, '+':3, '-':2, '$':1}
    return reference.get(op_input) > reference.get(op_top_stack)

def make_node(operands, operators, curr_op=''):
    str_t = {}
    op = operators.popleft()
    right = operands.popleft()
    left = operands.popleft()

    str_t[op] = [left, right]
    operands.appendleft(str_t)
    if curr_op: operators.appendleft(curr_op)

def build_tree(operands, operators):
    for token in tokens:
        curr_type = token.char_type
        curr_lexeme = token.lexeme

        if curr_type == 'DIGIT':
            operands.appendleft(curr_lexeme)
        if curr_type in ops:
            if has_higher_precedence(curr_lexeme, operators[0]):
                operators.appendleft(curr_lexeme)
            else:
                make_node(operands, operators, curr_lexeme)
        # print(operands, operators)

    while len(operators) > 1:
        make_node(operands, operators)

    return operands[0]

# def print_tree(str_t):
#     for char in str_t:
#         if char in ops:


def parserr(f):
    operands, operators = deque(), deque()
    # operators.append(Token('$', 'EOF')) TODO
    operators.append('$')

    for line in f:
        tk_dict = ast.literal_eval(line)
        tokens.append(
            Token(
                tk_dict.get('lexeme'),
                tk_dict.get('char_type')
            )
        )

    printtl(out_type='PARSER')

    paren_stack = deque()
    for i in range(len(tokens)):
        curr_type = tokens[i].char_type
        if (i>0):
            if (curr_type in ops) and (tokens[i-1].char_type in ops):
                raise Exception('Cannot recognize pattern: Too many operators')
        if (i==0 and (curr_type != 'DIGIT' and curr_type != 'OPEN-PAR')):
            raise Exception('Cannot start with an arithmetic operator')
        if i==len(tokens)-1 and (curr_type != 'DIGIT' and curr_type != 'CLOSE-PAR'):
            raise Exception('Cannot end with an arithmetic operator')

        if curr_type == 'OPEN-PAR':
            paren_stack.appendleft(tokens[i].lexeme)
        elif curr_type == 'CLOSE-PAR':
            if len(paren_stack) > 0:
                paren_stack.popleft()
            else:
                raise Exception('No opening parenthesis left')

    if len(paren_stack) > 0:
        raise Exception('Too many opening parenthesis left')

    # print_tree(build_tree(operands, operators)) #TODO
    flatten_tree = build_tree(operands, operators)
    print(flatten_tree)

    PAR_OUTPUT_FILENAME = 'output_files/parser_out.txt'
    with open(PAR_OUTPUT_FILENAME, 'w') as output:
        output.write(str(build_tree(operands, operators)))

    return PAR_OUTPUT_FILENAME