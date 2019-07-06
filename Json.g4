grammar Json;

json: obj | array;
expression: obj | array | primitive;

obj: '{' ((member)* lastMember)? '}';
member: key ':' value DELIMITER;
lastMember: key ':' value;
key: STRING;
value: expression;

array: '[' ((element)* lastElement)? ']';
element: expression DELIMITER;
lastElement: expression;
primitive: NUMBER | STRING | BOOLEAN | NULL;

NUMBER: MINUS? INT FRAC? EXP?;

fragment INT: '0' | NON_ZERO_DIGIT DIGIT*;
fragment DIGIT: [0-9];
fragment NON_ZERO_DIGIT: [1-9];
fragment E: 'e' | 'E';
fragment FRAC: '.' DIGIT+;
fragment MINUS: '-';
fragment PLUS: '+';
fragment EXP: E (MINUS | PLUS)? DIGIT+;

STRING: '"' (~('"' | '\n' | '\r') | '\\"')* '"';
BOOLEAN: 'true' | 'false';
DELIMITER: ',';
NULL: 'null';

WS: [ \r\n\t]+ -> skip;

