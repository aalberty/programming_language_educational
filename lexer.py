from tkn import TokenType as token_type 
from tkn import Token as token

class Lexer:
    def __init__(self, source: str):
        self.current_position = 0
        self.source = source
        return
    
    def __repr__(self):
        return f"Lexer({self.current_position}, {len(self.source)})"
    
    def find_next_token(self):
        for t in token_type:
            # check that source has enough chars left in the len to possibly contain the token_type.value
            if (len(self.source) - (self.current_position + len(t.value)) < 0):
                continue
            
            # check if this token present starting at the current position
            start = self.current_position
            end = (self.current_position + len(t.value))

            if ((self.source[start:end]).upper() == t.value):
                self.current_position = self.current_position + len(t.value)
                return token(t, t.value)
        
        self.current_position = self.current_position + 1
        return False
    
    # #tag_ident_start
    # TODO: IDENT impl; after a 'LET' and before a '=' is the value for 'IDENT'
    def find_ident(self):
        # find '='
        # find ';'
        # whichever comes first is the 'end' delimiter for the ident
        # 'start' delimiter is self.current_position - AKA it's assumed this func is only called
        # after we find a 'LET'

        try:
            equal_index = self.source[self.current_position:].index("=")
        except:
            equal_index = -1
        
        try:
            semicolon_index = self.source[self.current_position:].index(";")
        except:
            semicolon_index = -1

        if (equal_index == -1) and (semicolon_index == -1):
            print("ERR: no IDENT delimiter found.")
            return False

        else:
            delimiter_index = False
            if (equal_index == -1):
                delimiter_index = semicolon_index
            elif (semicolon_index == -1):
                delimiter_index = equal_index
            elif (equal_index < semicolon_index):
                delimiter_index = equal_index
            else:
                delimiter_index = semicolon_index
        
        delimiter_index += self.current_position

        # strip whitespace
        ident_val = self.source[self.current_position:delimiter_index]
        ident_val = ident_val.strip()

        self.current_position = delimiter_index
        return token(token_type("IDENT"), ident_val)
    # #tag_ident_end


    # #tag_tokens_start
    def find_tokens(self):
        tokens = []
        while self.current_position < len(self.source):
            t = self.find_next_token()
            if t != False:
                tokens.append(t)
        return tokens
    # #tag_tokens_end

    # #tag_value_start
    def find_value(self):
        # since this function looks for the value, it can be implied that it's called
        # __after__ a `find_next_token` -> LET  &&  `find_ident` -> <some_identity>
        # meaning the lexer's position has been updated accordingly -- e.g.:
        #               'let x = 5;'
        #                     ^
        #                   just before the `=`; aka just in front of the delimiter 
        #                                                          used to find identity.

        delimiter = self.source[self.current_position]
        # 1. ident_delimiter = `;`
        if delimiter == ';':
            return

        # 2. ident_delimiter = `=`
        elif delimiter == '=':
            #TODO: impl logic to check for INT; >><0-9><<
                # NOTE: __may__ be delimited by whitespace, but not necessarily

            #TODO: impl logic to check for STR; ' ' or " "
                # NOTE: __may__ be delimited by whitespace, but not necessarily

        return
    # #tag_value_end



def _vprint(verbose_check: bool, msg: str):
    if (verbose_check == True):
        print(msg)

        