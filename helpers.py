import enum

class TokenType(enum.Enum):
    INTEGER = "INTEGER"
    OPERATOR = "OPERATOR"
    EOF = "EOF"
    PAREN = "PAREN"


Precedence = {
    "/" : (3,4),
    "*" : (3,4),
    "+" : (1,2),
    "-" : (1,2)
}
