from helpers import Precedence, TokenType

def tokenise(text: str):
    curr = 0
    result = []
    while curr < len(text):
        if text[curr].isdigit():
            v = ""
            while curr < len(text)  and text[curr].isdigit():
                v += text[curr]
                curr += 1
            curr -= 1
            result.append((TokenType.INTEGER, int(v)))

        elif text[curr] in Precedence.keys():
            result.append((TokenType.OPERATOR, text[curr]))

        elif text[curr] in "()":
            result.append((TokenType.PAREN, text[curr]))

        else: pass
        curr += 1
    return result