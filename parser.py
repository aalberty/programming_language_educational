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
        self.length_in_tokens = 0
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
            self.length_in_tokens = 3
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
            
            self.length_in_tokens = 4

        return self
    
class Condition:
    def __init__(self):
        self.value = token(token_type('STR'), "<CONDITION_PLACEHOLDER>")
        self.length_in_tokens = 1
        return

    def __repr__(self):
        return f"Condition({self.value})"



# TODO: define the pattern, and add to the parser registry
class IfStatement:
    def __init__(self):
        self.length_in_tokens = 1
        self.condition = None
        self.then_block = None
        self.else_block = None
        return

    def __repr__(self):
        return f'IfStatement({self.condition}, {self.then_block}, {self.else_block})'
    
    def validate_pattern(self, tokens: list):
        potential_consumption = 0
        condition_start = _seek_token_type(tokens, token_type('('))
        if condition_start == False:
            print(f"WARN: IF condition missing '('.")
            return False
        potential_consumption += 1

        condition_end = _seek_token_type(tokens[condition_start:], token_type(')'))
        if condition_end == False:
            print(f"WARN: IF condition missing ')'.")
            return False
        potential_consumption += 1
        
        # using a placeholder rn
        condition = Condition()
        print(f"INFO: got <PLACEHOLDER_CONDITION>.")
        potential_consumption += condition.length_in_tokens

        then_block_start = _seek_token_type(tokens, token_type('{'))
        if then_block_start == False:
            print(f"WARN: missing THEN_BLOCK left_brace.")
            return False

        then_block_end = _seek_token_type(tokens[then_block_start:], token_type('}'))
        if then_block_end == False:
            print(f"WARN: missing THEN_BLOCK right_brace.")
            return False
        
        then_block = BlockStatement().validate_pattern(tokens[then_block_start:])
        if then_block == False:
            print(f"WARN: missing THEN_BLOCK.")
            return False
        potential_consumption += then_block.length_in_tokens
        
        else_block_start = _seek_token_type(tokens[potential_consumption:], token_type('{'))
        if else_block_start == False:
            print(f"WARN: missing ELSE_BLOCK left_brace.")
            return False
        
        else_block_end = _seek_token_type(tokens[else_block_start:], token_type('}'))
        if else_block_end == False:
            print(f"WARN: missing ELSE_BLOCK right_brace.")
            return False
        
        else_block = BlockStatement().validate_pattern(tokens[else_block_start:])
        if else_block == False:
            print(f"WARN: missing ELSE_BLOCK.")
            return False
        potential_consumption += else_block.length_in_tokens

        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
        return self

    def _validate_pattern(self, tokens: list):
        # IF __ '(' __ <CONDITION>__ ')'__ '{' __ <THEN_STMT> __ '}' __ 'ELSE' __ '{' __<ELSE_STMT>__ '}'
        # 
        # e.g.:
        #
        # if (this) {
        #     do that
        # } else {
        #     do this other thing
        # }
        p = Parser(tokens)

        # rules = {
        #     1 : '(',
        #     2 : '<CONDITION_PLACEHOLDER>',
        #     3 : ')',
        #     4 : '{'
        #     5 : 'Statement(IfStatement.then_statement)',
        #     6 : '}',
        #     7 : '{',
        #     8 : 'Statement(IfStatement.else_statement)',
        #     9 : '}' 
        # }
        
        then_statement_valid = BlockStatement().validate_pattern(tokens[4:])
        z = 0
        if then_statement_valid:
            z = then_statement_valid.length_in_tokens

        else_statement_valid = BlockStatement().validate_pattern(tokens[4 + z + 2:])
        if else_statement_valid != False:
            z += else_statement_valid.length_in_tokens

        validated =  tokens[1].type.name == 'LPAREN' and tokens[2].literal == "<CONDITION_PLACEHOLDER>" and tokens[3].type.name == 'RPAREN' and  tokens[4].type.name == 'LBRACE'  and then_statement_valid != False and tokens[4 + then_statement_valid.length_in_tokens].type.name == 'RBRACE' and tokens[4 + z + 1].type.name == 'LBRACE'and else_statement_valid != False and tokens[4 + z + 2].type.name == 'RBRACE'
        
        if validated:
            self.condition = '<CONDITION_PLACEHOLDER>'
            self.then_block = then_statement_valid,
            self.else_block = else_statement_valid

        return self
    

class BlockStatement:
    def __init__(self):
        self.length_in_tokens = 1
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
            self.length_in_tokens += potential_consumption
        else:
            # PROBLEM!
            return False
        
        if len(tokens) > 2:
            p = Parser(tokens[1:self.length_in_tokens])
            self.children = p.parse()
        return self


class Parser:

    def __init__(self, tokens: list):
        self.tokens = tokens

        self.ast = []

        self.NODE_TYPE_REGISTRY = {
            'LET': LetStatement,
            'IF': IfStatement,
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
            consume_count = validated_node.length_in_tokens
        else:
            if override_count == None:
                print(f"ERR: must either provide a validated node or override_count to inform parser of how many tokens must be consumed.")
                return
            consume_count = override_count
        # print(f"consuming {consume_count} tokens...")
        self.tokens = list(self.tokens[consume_count:])
        # print(f"remaining tokens: {self.tokens}")
        return


def _seek_token_type(tokens: list, type: token_type):
    found_at = 0
    for t in tokens:
        if t.type == type:
            return found_at
        found_at += 1
    return False

# TODO: pprint the AST so you can tell what the hell is going on
def pp_ast(ast: list):
    return