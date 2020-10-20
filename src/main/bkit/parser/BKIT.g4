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
ENDFOR: 'EndFor';
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

//Operator
ASSIGN: '=';
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
EQUAL: '==';
IS_NOT_EQUAL: '!=';
LESS: '<';
MORE_THAN: '>';
LESS_OR_EQUAL: '<=';
MORE_OR_EQUAL: '>=';
NOT_EQUAL_FLOAT: '=/=';  
LESS_FLOAT: '<.';
MORE_FLOAT: '>.';
LESS_OR_EQUAL_FLOAT: '<=.';
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

fragment  BASE10: ([1-9][0-9]*);
fragment BASE16: ('0x'[1-9A-F][0-9A-F]*| '0X'[1-9A-F][0-9A-F]*);
fragment BASE8: ('0o'[1-7][0-7]*| '0O'[1-7][0-7]*);


fragment EXPONENT: 	('E'|'e') '-'? [0-9]+;
FLOAT
	: [0-9]+ EXPONENT
	| [0-9]+ '.' ([0-9]* EXPONENT)?
	| [0-9]+ '.' ([0-9]+ EXPONENT?)?
	;

BOOLEAN: TRUE
        | FALSE;


//String
fragment EscapeSequence
	: '\\' [bfrnt'"\\] 
	| ('\'"')
	| '\\b'
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
fragment LITERALS: INTEGER| FLOAT| STRING| BOOLEAN | ARRAY|;

ARRAY: LEFT_CURLY_BRACKET WS*LITERALS(WS*',' WS*LITERALS)*WS* RIGHT_CURLY_BRACKET

{
	self.text = self.text.replace(" ","")	
	self.text = self.text.replace("\"","")	
	self.text = self.text.replace("\n","")	
	self.text = self.text.replace("\t","")	
	self.text = self.text.replace("\r","")	
}

		;

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

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

BLOCK_COMMENT
	:	'**'.*? '**'		-> skip
	;

UNTERMINATED_COMMENT: '**' ('*'~'*'|~'*')* ;

ERROR_CHAR
	:	.
	;

// ParxerSuite
program : declaration EOF;

declaration: var_list* function_list+ 
			;

var_list: ('Var: ' many_var SEMI ) ;

many_var: id_list  ; 

// Function Declaration
function_list: FUNCTION COLON function_name param? function_body ;

function_name: ID;

function_body: BODY COLON var_list* (statement)* ENDBODY DOT;

param: (PARAMETER COLON one_param many_param) 
		;

many_param: (COMMA one_param many_param)? 
			;

one_param:  (ID|array_index) (COMMA (ID|array_index))*;

id_list: (ID|array_index| ID ASSIGN exp| ID ASSIGN (TRUE|FALSE)) (COMMA (ID|array_index| ID ASSIGN exp| ID ASSIGN (TRUE|FALSE) ))*;

// Statement
statement: assign| if_statement| white_statement| for_statement| do_white_statement 
			 | break_statement| continue_statement| call_statement | function_call| return_statement;
// type value
primitive_type: INTEGER|BOOLEAN| FLOAT| STRING;

array_type: LEFT_CURLY_BRACKET (value (COMMA value)*) RIGHT_CURLY_BRACKET;

value: array_type|INTEGER|BOOLEAN| FLOAT| STRING; 



integer_arithmetic_type : SUB |ADD| MUL| DIVISION
			| MOD;
integer_relation_type :	 EQUAL| IS_NOT_EQUAL
			| LESS| MORE_THAN| LESS_OR_EQUAL| MORE_OR_EQUAL ;

float_arithmetic_type: ADD_FLOAT| SUB_FLOAT| MUL_FLOAT| DIVISION_FLOAT
			;
float_relation_type:	 NOT_EQUAL_FLOAT| LESS_FLOAT
			| MORE_FLOAT| MORE_OR_EQUAL_FLOAT| LESS_OR_EQUAL_FLOAT ;

bool_type: NEGATIVE| AND| OR ;

function_call: function_name LEFT_ROUND_BRACKET (exp(COMMA exp)*)? RIGHT_ROUND_BRACKET ;
			// id_list

array_index: ID (LEFT_SQUARE_BRACKET (exp2|array_index) RIGHT_SQUARE_BRACKET)+ ;

index:  (LEFT_SQUARE_BRACKET (exp2|array_index) RIGHT_SQUARE_BRACKET)+ ;

assign: (ID|array_index) ASSIGN exp SEMI
		| (ID|array_index) ASSIGN (TRUE|FALSE) SEMI;

if_statement: IF exp THEN statement*
				( ELSEIF exp THEN statement*)*
				( ELSE (exp| return_statement| statement) )? ENDIF DOT;

for_statement: FOR LEFT_ROUND_BRACKET ID ASSIGN exp COMMA exp COMMA INTEGER RIGHT_ROUND_BRACKET
			DO statement* ENDFOR  DOT;

white_statement: WHILE exp DO statement* ENDWHILE DOT;

do_white_statement: DO statement* WHILE exp ENDDO DOT;

break_statement: BREAK SEMI;

continue_statement: CONTINUE SEMI; // khai bao trung ten voi token lexer se bi loi

call_statement: ID LEFT_ROUND_BRACKET (exp(COMMA exp)*)? RIGHT_ROUND_BRACKET SEMI;

return_statement: RETURN exp SEMI 
				| RETURN call_statement	
				| RETURN assign;


// Expressions

exp: exp1 EQUAL exp1
	| exp1 IS_NOT_EQUAL exp1
	| exp1 LESS exp1
	| exp1 MORE_THAN exp1
	| exp1 LESS_OR_EQUAL exp1
	| exp1 MORE_OR_EQUAL exp1
	| exp1 NOT_EQUAL_FLOAT exp1
	| exp1 LESS_FLOAT exp1
	| exp1 MORE_FLOAT exp1
	| exp1 LESS_OR_EQUAL_FLOAT exp1
	| exp1 MORE_OR_EQUAL_FLOAT exp1 
	| exp1;

exp1: exp1 AND exp2
	| exp1 OR exp2
	| exp2
	;

exp2: exp2 ADD exp3
	| exp2 ADD_FLOAT exp3
	| exp2 SUB exp3
	| exp2 SUB_FLOAT exp3
	| exp3 ;

exp3: exp3 MUL exp5
	| exp3 MUL_FLOAT exp5
	| exp3 DIVISION exp5
	| exp3 DIVISION_FLOAT exp5
	| exp3 MOD exp5
	| exp5
	;

exp5: NEGATIVE exp5 
	| exp6 ;

exp6: SUB exp6 // sign 
	| SUB_FLOAT exp6 //sign float 
	| exp7 ;

exp7: exp7 index 
	| exp8 ;

exp8: function_call exp8 
	| call_statement exp8
	| exp9; 

exp9: LEFT_ROUND_BRACKET exp RIGHT_ROUND_BRACKET
	|INTEGER| FLOAT| STRING| BOOLEAN| ID | function_call| array_index| ARRAY;

// COERIONS
int_of_float: 'int_of_float' LEFT_ROUND_BRACKET FLOAT RIGHT_ROUND_BRACKET ;

float_to_int: 'float_to_int' LEFT_ROUND_BRACKET INTEGER RIGHT_ROUND_BRACKET ;

int_of_string: 'int_of_string' LEFT_ROUND_BRACKET STRING RIGHT_ROUND_BRACKET ;

string_of_int: 'string_of_int' LEFT_ROUND_BRACKET INTEGER RIGHT_ROUND_BRACKET ;

float_to_string: 'float_to_string' LEFT_ROUND_BRACKET STRING RIGHT_ROUND_BRACKET ;

string_of_float: 'string_of_float' LEFT_ROUND_BRACKET FLOAT RIGHT_ROUND_BRACKET ;

bool_of_string: 'bool_of_string' LEFT_ROUND_BRACKET STRING RIGHT_ROUND_BRACKET ;

string_of_bool: 'string_of_bool' LEFT_ROUND_BRACKET BOOLEAN RIGHT_ROUND_BRACKET ;



