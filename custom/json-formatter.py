import lexer
import parser
import sys
import ast
import formatter

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:
        json = f.read()

    try:
        tokens = lexer.json_lexer.lex(json)
        json_parser = parser.JsonParser(tokens)
        parse_tree = json_parser.parse()
        abstract_syntax_tree = ast.from_parse_tree_to_ast(parse_tree)
        json_formatter = formatter.JsonFormatter(abstract_syntax_tree)
        json_formatter.print_formatted()
    except lexer.LexerException as e:
        print('Invalid JSON provided')
        print('Aborted lexing on line {} column {}'.format(e.line, e.column))
        sys.exit(1)
    except parser.ParseException as e:
        print('Invalid JSON provided')
        unexpected_token = tokens[e.position]
        print('Syntax error'.format(unexpected_token.line, unexpected_token.position_in_line))
        print(unexpected_token)
        sys.exit(1)
