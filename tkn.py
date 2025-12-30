from enum import Enum

class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    IDENT = "IDENT"
    INT = "INT"

    # #tag_single_char_start
    # #tag_operators_start
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    # #tag_operators_end

    # #tag_delimiters_start
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    # #tag_delimiters_end
    # #tag_single_char_end

    # #tag_keywords_start
    FUNCTION = "FUNCTION"
    LET = "LET"
    IF  = "IF"
    FOR = "FOR"
    ELSE = "ELSE"
    RETURN = "RETURN"
    # #tag_keywords_end

class Token:
    def __init__(self, type_: TokenType, literal: str):
        self.type = type_
        self.literal = literal

    def __repr__(self):
        return f"Token({self.type}, '{self.literal}')"