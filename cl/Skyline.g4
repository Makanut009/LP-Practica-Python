grammar Skyline;

root : (assig | expr) EOF;

assig: VAR ':=' expr;

expr
    : simbol
    | skyline
    | PARES expr PARDR
    | MENYS expr
	| expr PER expr
    | expr MENYS expr
	| expr MES expr;    

simbol: VAR | NUM;

skyline: edifici | compost | random;

edifici: '(' NUM ',' NUM ',' NUM ')';

compost: '[' edifici (',' edifici)* ']';

random: '{' NUM ',' NUM ',' NUM ',' NUM ',' NUM '}';

PARES: '(';
PARDR: ')';
VAR: [a-z] ([a-z] | [0-9])*;
NUM : '-'? [0-9]+;
PER : '*';
MES : '+';
MENYS : '-';
WS : [ \r\n\t] + -> skip;
