from helpers import TokenType

class Iterator:
    def __init__(self, value: list):
        self.value = value

    def next(self):
        try: return self.value.pop(0)
        except: return (TokenType.EOF, None)

    def peek(self):
        try: return self.value[0]
        except: return (TokenType.EOF, None)