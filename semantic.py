from lexical import printtl

def semantic(f):
    printtl(out_type='SEMANTIC')

    flat_tree = ''
    for line in f:
        for char in line:
            flat_tree += char

    print(flat_tree)