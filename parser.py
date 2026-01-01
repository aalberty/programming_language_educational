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
    def __init__(self, tokens: list):
        self.name
        self.value
        self.tokens = tokens
        return

    def __repr__(self):
        print(f'LetStatement(name, value)')
        return
    
    def validate_pattern(self):
        return False
    
    

class Parser:

    def __init__(self, tokens: list):
        self.NODE_TYPE_REGISTRY = {
            'LET': LetStatement
        }
        return

    def __repr__(self):
        print(f"Parser({self.tokens})")
        return
    
    def parse(self):
        if self.tokens[0] in list(self.NODE_TYPE_REGISTRY.keys()):
            validated = self.expects_pattern(self.NODE_TYPE_REGISTRY[self.tokens[0]])
            if validated:
                # consume and continue
            else:
                # illegal?
        return
    
    def expects_pattern(self, node_type):
        node = node_type(tokens)
        if node.validate_pattern():
            return node
        else:
            return False


