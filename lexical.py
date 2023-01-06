from char_def import CHAR_DEF

def validate_char(char):
    for cdef in CHAR_DEF:
        if CHAR_DEF[cdef].count(char) > 0:
            return (True, cdef)
    return (False, None)

def create_symbol_table(char_map_list):
    aux_str = ''
    table = []

    for char in char_map_list:
        curr_type = char.get('char-type')
        if curr_type != 'SPACE' and curr_type != 'BREAK-LINE':
            if curr_type == 'DIGIT':
                aux_str += char.get('lexeme')
            else:
                if len(aux_str) > 0:
                    table.append({
                        'lexeme': aux_str,
                        'type': 'DIGIT'
                    })
                    aux_str = ''
                    if curr_type == 'EOF': break
                    table.append(char)
        elif curr_type == 'BREAK-LINE':
            if len(aux_str) > 0:
                table.append({
                    'lexeme': aux_str,
                    'type': 'DIGIT'
                })
                aux_str = ''

    return table

def printtl(tl):
    for tk in tl:
        print(tk)

def lexical_analyzer(f):
    char_map_list = []
    token_list = []

    for line in f:
        for char in line:
            is_valid, char_type = validate_char(char)
        
            if is_valid:
                char_map_list.append({
                    "lexeme": char,
                    'char-type': char_type})
            else:
                raise Exception('\'' + char + '\' is not a valid character.')
        # print(char_map_list)
        token_list = create_symbol_table(char_map_list)
        printtl(token_list)