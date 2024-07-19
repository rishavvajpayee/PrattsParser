from helpers import TokenType, Precedence
from iterator import Iterator

def calculate(operator_value, left, right):
    """
    Rather than building the AST we directly calculate
    """
    match (operator_value):
        case '+': return left + right
        case '-': return left - right
        case '*': return left * right
        case '/': return left / right
        case _  : return SyntaxError("Invalid operator")


def parse(tokens: Iterator, precedence: int):
    left_type, left = tokens.next()
    if left_type == TokenType.PAREN and left == "(":
        left = parse(tokens, 0)
        k, v = tokens.next()
        if k != TokenType.PAREN or v!=")":
            raise SyntaxError("Expected ), got" + repr(v))

    elif left_type != TokenType.INTEGER:
        raise Exception(f"Expected Number got : {repr(left)}")

    while True:
        operator_type, operator_value = tokens.peek()
        if operator_type in (TokenType.EOF,TokenType.PAREN):
            break
        if operator_type != TokenType.OPERATOR:
            raise SyntaxError(
                "Expected one of " + ", ".join(Precedence.keys())
                + "got " + repr(operator_value)
            )
        l, r = Precedence[operator_value]
        if l < precedence:
            break
        tokens.next()
        right = parse(tokens, r)
        left = calculate(operator_value, left, right)
        if type(left) == SyntaxError:
            raise left
    return left