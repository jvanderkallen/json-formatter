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

NUMBER: '-'? [0-9]+ (('.' | 'e' | 'E') [0-9]+)?;
STRING: '"' (~('"' | '\n' | '\r') | '\\"')* '"';
BOOLEAN: 'true' | 'false';
DELIMITER: ',';
NULL: 'null';

WS: [ \r\n\t]+ -> skip;

