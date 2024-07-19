import enum

class TOKEN(enum.Enum):
    ADD = '+'
    MULTIPLY = '*'
    SUBSTRACT = '-'
    DIVIDE = '/'


def parser(expr: str) -> str:
    returnable = ''
    for i in expr:
        returnable+=tokeniser(i)


def tokeniser(value: str):
    if value in TOKEN._value_:
        return f'{value} : {TOKEN.value} \n'
    else:
        return f'{value} : IDENTIFIER \n'
