grammar Skyline;

root : instruccio+ EOF;

instruccio: (assig | expr) NL;
assig: VAR ':=' expr;

expr:
    | edifici
    //| '(' expr ')'
	| expr PER expr
	| expr MES expr
	| expr MENYS expr
	| simbol;

simbol: VAR | NUM;

edifici: '(' NUM ',' NUM ',' NUM ')';

VAR: [a-z]+;
NUM : [0-9]+;
PER : '*';
MES : '+' ;
MENYS : '-' ;
//WS : [ \n]+ -> skip;
NL : '\n' ;
// WS: [ \n\r]+ -> skip;
