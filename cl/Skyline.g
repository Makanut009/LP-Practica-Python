grammar Skyline;

root : instruccio EOF;

instruccio: (assig | expr);
assig: VAR ':=' expr;

expr
    : simbol
	| expr PER expr
	| expr MES expr
	| expr MENYS expr
    | LPAREN expr RPAREN
    | MENYS simbol;

simbol: edifici | VAR | NUM;

edifici: '(' NUM ',' NUM ',' NUM ')';


LPAREN: '(';
RPAREN: ')';
VAR: [a-z]+;
NUM : [0-9]+;
PER : '*';
MES : '+';
MENYS : '-';
WS : [ \r\n\t] + -> skip;
