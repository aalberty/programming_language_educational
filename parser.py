# Consumes tokens from the lexer, and converts them into expressions/statements in an Abstract Syntax Tree (AST)
# 
# Consumes tokens in order
# Validates syntax
# Groups tokens into:
#     - statements
#     - expressions
# Handles operator precedence
# Builds AST nodes

from tkn import Token as token
from tkn import TokenType as token_type

class Identifier:

    def __init__(self, name):
        self.name = name
        return

    def __repr__(self):
        return f"Identifier({self.name})"




class Literal:

    def __init__(self, type: token_type, value):
        self.type = type
        self.value = value
        return

    def __repr__(self):
        return f"Literal({self.type.name}, {self.value})"




# TODO: remove?
# class Node:
#     def __init__(self, type: str):
#         self.type = type
#         self.children = []
#         return
    
#     def __repr__(self):
#         print(f"Node({self.type})")

# TODO: refac the different statement types as classes; makes more sense for how we think/talk about
# parsing (e.g. the parser 'sees' a let, and therefore the parser 'expects' a pattern of tokens following 
# grammar of a let statement in the list of tokens immediately following the let)
#
# the parser 'sees' `let`
# the parser 'expects' the pattern outlined by the 'LetStatement' class
# if the parser finds what it expects
# then the parser creates a Node(type='LetStatement')
# and consumes the used tokens
# finally continuing on to parse the next statement (should now be at the top of the token list)

class LetStatement:
    def __init__(self):
        self.name = None
        self.value = None
        return

    def __repr__(self):
        return f'LetStatement({self.name}, {self.value})'
    
    def validate_pattern(self, tokens: list):
        # ident is required next
        if tokens[1].type.name != 'IDENT':
            # PROBLEM!!!
            return False
        
        self.name = Identifier(tokens[1].literal)

        # after IDENT, expect either an assignment, or an end of statement
        if tokens[2].type.name != 'SEMICOLON' and tokens[2].type.name != 'ASSIGN':
            # PROBLEM!!!
            return False
        
        if tokens[2].type.name == 'SEMICOLON':
            self.value = None
            return self
        
        elif tokens[2].type.name == 'ASSIGN':
            # get the value; 'SEMICOLON' will delimit
            if tokens[3].type.name != 'STR' and tokens[3].type.name != 'INT':
                # PROBLEM!!!
                return False
            
            if tokens[3].type.name == 'STR':
                self.value = Literal(tokens[3].type, tokens[3].literal)
            
            elif tokens[3].type.name == 'INT':
                self.value = Literal(tokens[3].type, tokens[3].literal)

        return self
    
    

class Parser:

    def __init__(self, tokens: list):
        self.tokens = tokens

        self.NODE_TYPE_REGISTRY = {
            'LET': LetStatement
        }
        return

    def __repr__(self):
        return f"Parser({self.tokens})"
    
    def parse(self):
        if self.tokens[0].literal in list(self.NODE_TYPE_REGISTRY.keys()):
            validated = self.expects_pattern(self.NODE_TYPE_REGISTRY[self.tokens[0].literal])
            if validated:
                # consume and continue
                return validated
            else:
                # illegal?
                return False
        return False
    
    def expects_pattern(self, node_type):
        node = node_type()
        if node.validate_pattern(self.tokens):
            return node
        else:
            return False


