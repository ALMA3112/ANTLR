grammar LabeledExpr;

prog:   stat+ ;

stat:   asignar
    |   imprimirExpr
    ;

asignar: ID '=' expr NEWLINE ;
imprimirExpr: expr NEWLINE ;

expr
    :   expr op=('*'|'/') expr    # MultiplicarDividir
    |   expr op=('+'|'-') expr    # SumarRestar
    |   NUM                       # Entero
    |   ID                        # Identificador
    |   '(' expr ')'              # Parentesis
    |   funcion '(' expr ')'      # LlamadaFuncion
    |   expr '!'                  # Factorial
    |   ('+'|'-') expr            # SignoUnario
    ;

funcion
    : 'sin' | 'cos' | 'tan' | 'sqrt' | 'ln' | 'log' | 'rad' | 'deg'
    ;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

ID  : [a-zA-Z]+ ;
NUM : [0-9]+('.'[0-9]+)? ;   // soporta enteros y decimales
NEWLINE:'\r'? '\n' ;
WS  : [ \t]+ -> skip ;
