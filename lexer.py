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
    
    def find_tokens(self):
        tokens = []
        while self.current_position < len(self.source):
            t = self.find_next_token()
            if t != False:
                tokens.append(t)
        return tokens