from token import TokenType as token_type 

class Lexer:
    def __init__(self, source: str):
        self.current_position = 0
        self.source = source
        return
    
    def __repr__(self):
        return f"Lexer({self.current_position}, {len(self.source)})"
    
    def find_next_token(self):
        # first check our current_position to see if it's a token
        current_char = self.source[self.current_position]
        if (current_char):


        # iter forward in the source until we hit a (possible) token
        
        pass