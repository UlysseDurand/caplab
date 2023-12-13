grammar Arit;

// MIF08@Lyon1 and CAP@ENSL, arit evaluator

@header {
# header - mettre les déclarations globales
import sys
idTab = {};

def valeur(idtext):
    if idtext not in idTab: # Always true, for now
        raise UnknownIdentifier(idtext)
    else:
        return idTab[idtext]

class UnknownIdentifier(Exception):
    pass

class DivByZero(Exception):
    pass

}



prog: expr {print(str($expr.text))+" + " + str($expr.res;)} ;

expr returns [int res]:
    $e0=expr PLUS $t0=term {$res = $e0.res + $t0.res;}
    | $t0=term {$res = $t0.res;}
    ;

term returns [int res]:
    $t0=term TIMES $f0=form {$res = $t0.res * $f0.res;}
    | $f0=form {$res = $f0.res;}
    ;

form returns [int res]:
    $i0=ID {$res = valeur($i0.text);}
    | $i0=INT {$res = int($i0.text);}
    | LPAR $e0=expr RPAR {$res = $e0.res;}
    ;


COMMENT
 : '//' ~[\r\n]* -> skip
 ;

ID : ('a'..'z'|'A'..'Z')+;
PLUS : '+';
TIMES : '*';
LPAR : '(';
RPAR : ')';
INT: '0'..'9'+;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
