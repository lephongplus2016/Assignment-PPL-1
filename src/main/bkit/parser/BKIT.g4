/*
Name: Le Hong Phong
ID: 1813518
*/
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}
//LexerSuite
ID: [a-z][a-zA-Z0-9_]*;

BODY: 'Body';
ELSE: 'Else';
ENDFOR: 'Endfor';
IF: 'If';
VAR: 'Var';
ENDDO: 'EndDo';
BREAK: 'Break';
ELSEIF: 'ElseIf';
ENDWHILE: 'EndWhile';
PARAMETER: 'Parameter';
WHILE: 'While';
CONTINUE: 'Continue';
ENDBODY: 'EndBody';
FOR: 'For';
RETURN: 'Return';
TRUE: 'True';
DO: 'Do';
ENDIF: 'EndIf';
FUNCTION: 'Function';
THEN: 'Then';
FALSE: 'False';

KEYWORDS: BODY| ELSE| ENDFOR| IF| VAR| ENDDO| BREAK| ELSEIF| ENDWHILE| PARAMETER| WHILE| CONTINUE| ENDBODY| FOR| RETURN| TRUE| DO| ENDIF| FUNCTION| THEN| FALSE;

//Operators
ADD: '+';
ADD_FLOAT: '+.'; 
SUB: '-';
SUB_FLOAT: '-.';
MUL: '*';
MUL_FLOAT: '*.';
DIVISION: '\\';
DIVISION_FLOAT: '\\.';
MOD: '%';
NEGATIVE: '!';
AND: '&&';
OR: '||';
COMPARE: '==';
IS_NOT_EQUAL: '!=';
LESS: '<';
MORE_THAN: '>';
LESS_OR_EQUAL: '<=';
MORE_OR_EQUAL: '>=';
NOT_EQUAL_FLOAT: '=/=';  
LESS_FLOAT: '<.';
MORE_FLOAT: '>.';
ESS_OR_EQUAL_FLOAT: '<=.';
MORE_OR_EQUAL_FLOAT: '>=.';

//Separators
LEFT_ROUND_BRACKET: '(';
RIGHT_ROUND_BRACKET: ')';
LEFT_SQUARE_BRACKET: '[';
RIGHT_SQUARE_BRACKET: ']';
LEFT_CURLY_BRACKET: '{';
RIGHT_CURLY_BRACKET: '}';
COLON: ':';
DOT: '.';
COMMA: ',';

//Literals

INTEGER: BASE10|BASE16|BASE8|'0';
//([1-9][0-9]*| '0x'[1-9A-F][0-9A-F]*| '0X'[1-9A-F][0-9A-F]*| '0o'[1-7][0-7]*| '0O'[1-7][0-7]*| '0');
fragment  BASE10: ([1-9][0-9]*);
fragment BASE16: ('0x'[1-9A-F][0-9A-F]*| '0X'[1-9A-F][0-9A-F]*);
fragment BASE8: ('0o'[1-7][0-7]*| '0O'[1-7][0-7]*);


fragment EXPONENT: 	('E'|'e') '-'? [0-9]+;
FLOAT
	: [0-9]+ EXPONENT
	| [0-9]+ '.' ([0-9]* EXPONENT)?
	| [0-9]* '.' [0-9]+ EXPONENT?
	;

BOOLEAN: TRUE
        | FALSE;


//string
/*STRING
	:	'"' Character*? '"'
	;

fragment
Character
	:	~["\\\n]
	|	EscapeSequence
	;
fragment
EscapeSequence
	:	'\\'[bfrnt'\\]
	;        
*/

//String
fragment EscapeSequence
	: '\\' [bfrnt'"\\] 
	| ('\'"')
	;
fragment Character
	:	~["\\\n]
	|	EscapeSequence
	;
STRING
 	: '"' (EscapeSequence | ~[\n\r'"\\])* '"'
	{
		self.text = self.text[1:-1]
	}
   	; 

//array
fragment LITERALS: INTEGER| FLOAT| STRING| BOOLEAN | ARRAY;
ARRAY: LEFT_CURLY_BRACKET (' ')*LITERALS((' ')*',' (' ')*LITERALS)*(' ')* RIGHT_CURLY_BRACKET
//ARRAY: LEFT_CURLY_BRACKET (' ')* (INTEGER| FLOAT | STRING| BOOLEAN | ARRAY) ((' ')*',' (' ')* (INTEGER| FLOAT | STRING| BOOLEAN | ARRAY))* (' ')* RIGHT_CURLY_BRACKET
// {
// dummy = str(self.text)
// var = ""
// for i in range(len(dummy)):
// 	if dummy[i] != " ":
// 		var += dummy[i]



// self.text = var
// }

//kieu boolean co van de

// {
// 	self.text = self.text[1:-1]
// }

{
	self.text = self.text.replace(" ","")	
	self.text = self.text.replace("\"","")	
}


		;
// ARRAY_2
// 		: ARRAY
// 		| LEFT_CURLY_BRACKET (' ')*ARRAY*((' ')*',' (' ')*ARRAY)*(' ')* RIGHT_CURLY_BRACKET
		
// {
// 	dummy = str(self.text)
// 	var = ""
// 	for i in range(len(dummy)):
// 		if dummy[i] != " ":
// 			var += dummy[i]
	
// 	self.text = var
//}
//		;
	//self.text = self.text + ""
		//self.text = self.text.replace(" ","")	
//ERROR
UNCLOSE_STRING
	:	'"' Character*
	{
		raise UncloseString(self.text[1:])
	}
	;

ILLEGAL_ESCAPE
	:	'"' Character* ('\\' ~[bfrnt'\\])
	{
		raise IllegalEscape(self.text[1:])
	}
	;




program  : VAR COLON ID SEMI EOF ;

//ID: [a-z]+ ; 

SEMI: ';' ;

//COLON: ':' ;

//VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

BLOCK_COMMENT
	:	'**'.*?'**'		-> skip
	;


UNTERMINATED_COMMENT: '**' ('*'~'*'|~'*')* ;

ERROR_CHAR
	:	.
	;

// ParxerSuite
//mainprogram : declaration + EOF;

//declaration: var_list
//			| function_list 
//			;

//var_list: ()? ;
