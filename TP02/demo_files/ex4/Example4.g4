//define a tiny grammar with attributes for arith expressions with identifiers

grammar Example4;

full_expr: expr EOF ;

expr:
      OPAR expr CPAR expr
    | OBRA expr CBRA expr
    | ID
    |
    ;

OPAR : '(' ;
CPAR : ')' ;
OBRA : '[' ;
CBRA : ']' ;
ID : ('a'..'z'|'A'..'Z')+ ;
WS : ~[()[\]] -> skip ;
