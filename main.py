from lexical import lexical_analyzer
from parserr import parserr
from semantic import semantic

filename = './example.txt'
print('')

flex = open(filename, 'r')
filename = lexical_analyzer(flex)
if filename != '$':
    fpar = open(filename, 'r')
    filename  = parserr(fpar)

    semantic()
else:
    raise Exception('Empty input.')
print('')