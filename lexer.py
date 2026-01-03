from tkn import TokenType as token_type 
from tkn import Token as token
from tkn import RESERVED_TOKEN_TYPES, NONRESERVED_TOKEN_TYPES

WHITESPACE_CHARS = [
    ' ',
    '\t',
    '\n',
    'else',
]

class Lexer:
    def __init__(self, source: str):
        self.current_position = 0
        self.source = source
        return
    
    def __repr__(self):
        return f"Lexer({self.current_position}, {len(self.source)})"
    
    def tokenize(self):
        tokens = []
        while self.current_position < len(self.source):
            new_position = self.current_position + 1
            # skip whitespace
            if self.source[self.current_position] in WHITESPACE_CHARS:
                self.current_position = new_position
                continue

            found = False
            for t in RESERVED_TOKEN_TYPES:
                start_index = self.current_position
                end_index = len(t.value) + start_index
                # RESERVED TOKENS 
                # check for tkn.RESERVED_TOKEN_TYPES; tokens which have a static defined literal
                # e.g. ';', or 'LET'
                if self.source[start_index:end_index].upper() == t.value:

                    # STR DELIMITER HANDLING: `'` and `"` 
                    if t.value == "'" or t.value == '"':
                        str_start = self.current_position
                        seeker = self.current_position + 1
                        while self.source[seeker] != t.value:
                            seeker += 1
                        str_end = seeker
                        str_literal = self.source[str_start:str_end]
                        str_literal = str_literal.strip().strip(t.value)
                        tokens.append(token(t.STR, f'"{str_literal}"'))
                        new_position = str_end + 1
                        found = True
                    else:
                        # BASE CASE: exact match on operator/keyword
                        tokens.append(token(t, t.value))
                        new_position = end_index
                        found = True
                        break


            current_char = self.source[self.current_position]
            if not found:
                # IDENT
                if current_char == "_" or current_char.isalpha():
                    ident_start = self.current_position
                    seeker = self.current_position + 1
                    while self.source[seeker] == "_" or self.source[seeker].isalnum():
                        seeker += 1
                    ident_end = seeker
                    tokens.append(token(token_type.IDENT, self.source[ident_start:ident_end]))
                    new_position = ident_end 
                    found = True
            
            if not found:
                # VALUE
                if current_char.isnumeric():
                    val_start = self.current_position
                    seeker = self.current_position + 1
                    while self.source[seeker].isnumeric():
                        seeker += 1
                    val_end = seeker
                    tokens.append(token(token_type.INT, self.source[val_start:val_end]))
                    new_position = val_end
                    found = True


            self.current_position = new_position
        tokens.append(token(token_type.EOF, 'EOF'))
        return tokens