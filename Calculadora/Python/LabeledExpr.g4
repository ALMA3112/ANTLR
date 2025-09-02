grammar LabeledExpr;

prog:   stat+ EOF ;

stat:   expr NEWLINE?              
    |   ID '=' expr NEWLINE?       
    |   NEWLINE                   
    ;

expr:   expr op=('*'|'/') expr    
    |   expr op=('+'|'-') expr    
    |   ID '(' exprList? ')'      
    |   INT                       
    |   ID                        
    |   '(' expr ')'              
    ;

exprList: expr (',' expr)* ;

ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
NEWLINE: '\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
