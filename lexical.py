from char_def import CHAR_DEF
# import Objects

def validate_char(char):
    for cdef in CHAR_DEF:
        if CHAR_DEF[cdef].count(char) > 0:
            return (True, cdef)
    return (False, None)

def create_symbol_table(char_map_list):
    aux_str = ''
    aux_str2 = ''
    table = []

    for char in char_map_list:
        curr_type = char.get('char_type')
        if curr_type != 'BREAK-LINE':
            if curr_type == 'DIGIT':
                aux_str += char.get('lexeme')
            else:
                if len(aux_str) > 0:
                    table.append({
                        'lexeme': aux_str,
                        'char_type': 'DIGIT'
                    })
                    aux_str = ''
                    
                if curr_type == 'EOF': break
                else:
                    table.append(char)
        elif curr_type == 'BREAK-LINE':
            if len(aux_str) > 0:
                table.append({
                    'lexeme': aux_str,
                    'char_type': 'DIGIT'
                })
                aux_str = ''
        

    return table

def printtl(tl=[], out_type=''):
    print(f'-------------------------------\n~> {out_type}\n')
    if len(tl)>0:
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
                    'char_type': char_type})
            else:
                raise Exception('\'' + char + '\' is not a valid character.')
        # print(char_map_list)
        token_list = create_symbol_table(char_map_list)

        LEX_OUTPUT_FILENAME = 'output_files/lex_out.txt'
        with open(LEX_OUTPUT_FILENAME, 'w') as output:
            for tk in token_list:
                output.write(str(tk) + '\n')

        printtl(token_list, 'LEXICAL')
        return LEX_OUTPUT_FILENAME