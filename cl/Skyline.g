grammar Skyline;

root : instruccio EOF ;

instruccio: assig | expr;
assig: VAR ':=' expr;

expr:
    | '(' expr ')'
	| expr PER expr
	| expr MES expr
	| expr MENYS expr
	| simbol;

simbol: VAR | NUM;

VAR: [a-z]+;
NUM : [0-9]+;
PER : '*';
MES : '+' ;
MENYS : '-' ;
WS : [ \n]+ -> skip;
// WS: [ \n\r]+ -> skip;
