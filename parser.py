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



# Implementing statement types as classes makes more sense for how we think/talk about parsing
# (e.g. the parser 'sees' a let, and therefore the parser 'expects' a pattern of tokens following 
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
        self.tokens_consumed = 0
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
            self.tokens_consumed = 3
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
            
            self.tokens_consumed = 4

        return self
    
# TODO: define the pattern, and add to the parser registry
class IfStatement:
    def __init__(self):
        self.tokens_consumed
        self.condition
        self.then_block
        self.else_block
        return

    def __repr__(self):
        return f'IfStatement({self.condition}, {self.then_block}, {self.else_block})'
    
    def validate_pattern(self, tokens: list):
        return
    

class BlockStatement:
    def __init__(self):
        self.tokens_consumed = 1
        self.children = []
        return
    
    def __repr__(self):
        return f'BlockStatement({self.children})'
    
    def validate_pattern(self, tokens: list):
        potential_consumption = 0
        block_end_found = False
        for t in tokens:
            potential_consumption += 1
            if t.type.name == 'RBRACE':
                block_end_found = True
                break

        if block_end_found:
            self.tokens_consumed += potential_consumption
        else:
            # PROBLEM!
            return False
        
        # TODO: parse the block children
        if len(tokens) > 2:
            p = Parser(tokens[1:self.tokens_consumed])
            self.children = p.parse()
        return self


class Parser:

    def __init__(self, tokens: list):
        self.tokens = tokens

        self.ast = []

        self.NODE_TYPE_REGISTRY = {
            'LET': LetStatement,
            '{': BlockStatement
        }
        return

    def __repr__(self):
        return f"Parser({self.tokens})"
    
    def parse(self):
        while len(self.tokens) != 0:

            if self.tokens[0].literal in list(self.NODE_TYPE_REGISTRY.keys()):
                validated = self.expects_pattern(self.NODE_TYPE_REGISTRY[self.tokens[0].literal])
                if validated:
                    # add resulting node to the AST
                    self.ast.append(validated)
                    # consume tokens
                    self.consume(validated)
                    # continue
                else:
                    # illegal?
                    print(f"ERR: no matching statement pattern found in remaining tokens: {self.tokens}")
                    self.consume(override_count = 1)
            else:
                # print(f"WARN: pattern not yet defined to handle {self.tokens[0]}.")
                self.consume(override_count = 1)

        return self.ast
    
    def expects_pattern(self, node_type):
        node = node_type()
        if node.validate_pattern(self.tokens):
            return node
        else:
            return False
    
    def consume(self, validated_node = None, override_count = None):
        consume_count = 0
        if validated_node != None:
            consume_count = validated_node.tokens_consumed
        else:
            if override_count == None:
                print(f"ERR: must either provide a validated node or override_count to inform parser of how many tokens must be consumed.")
                return
            consume_count = override_count
        # print(f"consuming {consume_count} tokens...")
        self.tokens = list(self.tokens[consume_count:])
        # print(f"remaining tokens: {self.tokens}")
        return


