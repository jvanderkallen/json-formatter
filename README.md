# JSON Formatter
Lexer and parser are based on [RFC 4627](https://www.ietf.org/rfc/rfc4627.txt).

## Installation
``` sh
$ pip3 install -r requirements.txt
```

## Development
``` sh
$ antlr4 -Dlanguage=Python3 Json.g4
```

## Usage
``` sh
$ python3 json-formatter.py file.json
```
