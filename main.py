"""
Entry point of application
"""

import enum

class TOKEN(enum.Enum):
    ADD = 'ADD'
    MULTIPLY = 'MULTIPLY'
    SUBSTRACT = 'SUBSTRACT'
    DIVIDE = 'DIVIDE'
    IDENTIDIER = 'IDENTIDIER'

def parser(expr: str) -> str:
    returnable = ''
    for i in expr:
        returnable+=f'{i} : ' + str(tokeniser(i)) + '\n'
    return returnable

def tokeniser(value: str):
    match (value):
        case '+': return TOKEN.ADD
        case '-': return TOKEN.SUBSTRACT
        case '*': return TOKEN.MULTIPLY
        case '/': return TOKEN.DIVIDE
        case _ :  return TOKEN.IDENTIDIER

def entrypoint():
    close = False
    while not close:
        expr = str(input('> '))
        if expr == 'quit':
            close = True
            break
        resp = parser(expr)
        response = f": \n{resp}"
        print(response)

if __name__ == "__main__":
    try:
        print("Rolling up Parser ...")
        entrypoint()
        
    except Exception as error:
        print(error)