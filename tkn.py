from enum import Enum

class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # #tag_ident_start
    IDENT = "IDENT"
    # #tag_ident_end
    INT = "INT"
    STR = "STR"

    # #tag_operators_start
    DBLEQL = "=="
    BANGEQL = "!="
    LTEQL = "<="
    GTEQL = ">="
    LANGLE = "<"
    RANGLE = ">"
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
    QUOTE = "'"
    DBL_QUOTE = '"'
    # #tag_delimiters_end

    # #tag_keywords_start
    FUNCTION = "FUNCTION"
    LET = "LET"
    VAR = "VAR"
    CONST = "CONST"
    IF  = "IF"
    FOR = "FOR"
    ELSE = "ELSE"
    RETURN = "RETURN"
    # #tag_keywords_end

NONRESERVED_TOKEN_TYPES = [
    TokenType.ILLEGAL,
    TokenType.EOF,
    TokenType.IDENT,
    TokenType.INT,
    TokenType.STR
]

RESERVED_TOKEN_TYPES = [
    TokenType.DBLEQL,
    TokenType.BANGEQL,
    TokenType.LTEQL,
    TokenType.GTEQL,
    TokenType.LANGLE,
    TokenType.RANGLE,
    TokenType.ASSIGN,
    TokenType.PLUS,
    TokenType.MINUS,
    TokenType.BANG,
    TokenType.ASTERISK,
    TokenType.SLASH,
    TokenType.COMMA,
    TokenType.SEMICOLON,
    TokenType.LPAREN,
    TokenType.RPAREN,
    TokenType.LBRACE,
    TokenType.RBRACE,
    TokenType.QUOTE,
    TokenType.DBL_QUOTE,
    TokenType.FUNCTION,
    TokenType.LET,
    TokenType.VAR,
    TokenType.CONST,
    TokenType.IF,
    TokenType.FOR,
    TokenType.ELSE,
    TokenType.RETURN
]


class Token:
    def __init__(self, type_: TokenType, literal: str):
        self.type = type_
        self.literal = literal

    def __repr__(self):
        return f"Token({self.type}, '{self.literal}')"