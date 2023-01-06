import ast
from collections import sta

from Token import Token
from lexical import printtl

def next():
    return tokens[curr_pos+1]

def expect(tk):
    if next(cu)

def make_leaf(d):


def factor(operators, operands):
    '''
    factor → [0-9] | ( expr ) | $
    '''
    if tokens[curr_pos].char_type == 'DIGIT':
        operands.append(tokens[curr_pos].lexeme)
        curr_pos = curr_pos + 1
    if tokens[curr_pos].lexeme == '(':
        operands.append(tokens[curr_pos])
        curr_pos = curr_pos + 1
        expr(operators, operands)
        


def term(operators, operands):
    '''
    term → factor * term | factor / termo | factor
    '''
    factor(operators, operands)
    

def expr(operators, operands):
    '''
    expr →  term + expr | term - expr | term
    '''
    term(operators, operands)
    

def parserr(f):
    operators, operands = [], []

    operators.append(Token('$', 'EOF'))
    global tokens, curr_pos
    curr_pos = 0
    tokens = []

    for line in f:
        tk_dict = ast.literal_eval(line)
        tokens.append(
            Token(
                tk_dict.get('lexeme'),
                tk_dict.get('char_type')
            )
        )
    expr(operators, operands)

    # for token in tokens:
    #     print(token.lexeme)

    # PAR_OUTPUT_FILENAME = 'output_files/parser_out.txt'
        # with open(PAR_OUTPUT_FILENAME, 'w') as output:
            # output.write(str(token_list))

    return '' #PAR_OUTPUT_FILENAME

    
