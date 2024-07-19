from iterator import Iterator
from parser import parse
from tokeniser import tokenise

if __name__ == "__main__":
    try:
        print("Rolling up Parser ...")
        close = False
        while not close:
            expr = str(input('> '))
            if expr == 'quit':
                close = True
                break
            tokens = tokenise(expr)
            iterated = Iterator(tokens)
            resp = parse(iterated, 0)
            print(resp)


    except Exception as error:
        print(error)