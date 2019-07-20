import sys
import re

class TokenType:
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = re.compile(pattern)

class Token:
    def __init__(self, index, token_type, lexeme_position, lexeme, line, position_in_line):
        self.index = index
        self.token_type = token_type
        self.lexeme_position = lexeme_position
        self.lexeme = lexeme
        self.line = line
        self.position_in_line = position_in_line

    def __repr__(self):
        return "[@{},{}:{}='{}',<{}>,{}:{}]".format(self.index, self.lexeme_position, self.lexeme_position + (len(self.lexeme) - 1), self.lexeme, self.token_type, self.line, self.position_in_line)

class LexerException(BaseException):
    def __init__(self, tokens, line, column):
        self.tokens = tokens
        self.line = line
        self.column = column

class Lexer:
    def __init__(self, token_types, skip):
        self.token_types = token_types
        self.skip = skip

    def calc_current_line(self, text):
        return text.count('\n') + 1

    def calc_current_pos_in_line(self, text):
        return len(text) - text.rfind('\n') - 1

    def match(self, token_type, text):
        res = token_type.pattern.match(text)
        if res is not None:
            return res[0]
        return None

    def lex(self, text):
        tokens = []

        current_position = 0
        length_of_text = len(text)
        tokens_found = 0
        while current_position < length_of_text:
            match = self.match(self.skip, text[current_position:])
            if match is not None:
                current_position += len(match)
                continue

            found_token = False

            for token_type in self.token_types:
                match = self.match(token_type, text[current_position:])
                if match is not None:
                    tokens.append(Token(tokens_found, token_type.name, current_position, match, self.calc_current_line(text[:current_position]), self.calc_current_pos_in_line(text[:current_position])))
                    current_position += len(match)
                    tokens_found += 1
                    found_token = True
                    break

            if not found_token:
                raise LexerException(tokens, self.calc_current_line(text[:current_position]), self.calc_current_pos_in_line(text[:current_position]))

        tokens.append(Token(tokens_found, 'EOF', current_position, '', self.calc_current_line(text[:current_position]), self.calc_current_pos_in_line(text[:current_position])))
        return tokens

whitespace = TokenType('WS', r'[ \r\n\t]+')

token_types = [
    TokenType('NUMBER', '-?(0|[1-9][0-9]*)(.([0-9]+))?((E|e)(-|\+)?([0-9]+))?'),
    TokenType('STRING', r'"([\u0020-\u0021]|[\u0023-\u005B]|[\u005D-\u10FFFF]|(\\("|\|/|b|f|n|r|t|(u([0-9][A-F]{4})))))*"'),
    TokenType('ARRAY_OPEN', '\['),
    TokenType('ARRAY_CLOSE', '\]'),
    TokenType('OBJECT_OPEN', '{'),
    TokenType('OBJECT_CLOSE', '}'),
    TokenType('BOOLEAN', 'true|false'),
    TokenType('DELIMITER', ','),
    TokenType('COLON', ':'),
    TokenType('NULL', 'null')
]

json_lexer = Lexer(token_types, whitespace)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        json = f.read()

    def print_tokens(tokens):
        for token in tokens:
            print(token)

    try:
        tokens = json_lexer.lex(json)
        print_tokens(tokens)
    except LexerException as e:
        print_tokens(e.tokens)
        print('Invalid JSON provided')
        print('Aborted lexing on line {} column {}'.format(e.line, e.column))
        sys.exit(1)
