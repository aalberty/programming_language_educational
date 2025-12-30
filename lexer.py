from tkn import TokenType as token_type 
from tkn import Token as token

class Lexer:
    def __init__(self, source: str):
        self.current_position = 0
        self.source = source
        return
    
    def __repr__(self):
        return f"Lexer({self.current_position}, {len(self.source)})"
    
    # #tag_single_char_start
    def find_next_token(self):
        print(f"Finding next token in source: {self.source}")
        # first check our current_position to see if it's a token
        current_char = self.source[self.current_position]

        for t in token_type:
            print(f"Checking {t.value}")
            # check that source has enough chars left in the len to possibly contain the token_type.value
            if (len(self.source) - (self.current_position + len(t.value)) < 0):
                print(f"Not enough chars left in document to hold token '{t.value}'")
                continue
            
            # check if this token present starting at the current position
            start = self.current_position
            end = (self.current_position + len(t.value))
            print(f"start: {start}, end: {end}")

            print(f"start.type: {type(start)}, end.type: {type(end)}")
            if ((self.source[start:end]).upper() == t.value):
                print(f"'{t.value}'") 
                self.current_position = self.current_position + len(t.value)
                return token(t, t.value)
        
        self.current_position = self.current_position + 1
        return False

    # #tag_single_char_end
 #