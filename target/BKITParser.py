# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\b\2\2\5\6\7\67\2\2\6\7\7\3\2\2\7")
        buf.write("\b\7B\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Else'", "'Endfor'", 
                     "'If'", "'Var'", "'EndDo'", "'Break'", "'ElseIf'", 
                     "'EndWhile'", "'Parameter'", "'While'", "'Continue'", 
                     "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", 
                     "'EndIf'", "'Function'", "'Then'", "'False'", "<INVALID>", 
                     "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", 
                     "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", 
                     "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "':'", "'.'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "ID", "BODY", "ELSE", "ENDFOR", "IF", 
                      "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", 
                      "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", 
                      "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "KEYWORDS", 
                      "ADD", "ADD_FLOAT", "SUB", "SUB_FLOAT", "MUL", "MUL_FLOAT", 
                      "DIVISION", "DIVISION_FLOAT", "MOD", "NEGATIVE", "AND", 
                      "OR", "COMPARE", "IS_NOT_EQUAL", "LESS", "MORE_THAN", 
                      "LESS_OR_EQUAL", "MORE_OR_EQUAL", "NOT_EQUAL_FLOAT", 
                      "LESS_FLOAT", "MORE_FLOAT", "ESS_OR_EQUAL_FLOAT", 
                      "MORE_OR_EQUAL_FLOAT", "LEFT_ROUND_BRACKET", "RIGHT_ROUND_BRACKET", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", 
                      "RIGHT_CURLY_BRACKET", "COLON", "DOT", "COMMA", "INTEGER", 
                      "FLOAT", "BOOLEAN", "STRING", "LITERALS", "ARRAY", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "SEMI", "WS", 
                      "BLOCK_COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    BODY=2
    ELSE=3
    ENDFOR=4
    IF=5
    VAR=6
    ENDDO=7
    BREAK=8
    ELSEIF=9
    ENDWHILE=10
    PARAMETER=11
    WHILE=12
    CONTINUE=13
    ENDBODY=14
    FOR=15
    RETURN=16
    TRUE=17
    DO=18
    ENDIF=19
    FUNCTION=20
    THEN=21
    FALSE=22
    KEYWORDS=23
    ADD=24
    ADD_FLOAT=25
    SUB=26
    SUB_FLOAT=27
    MUL=28
    MUL_FLOAT=29
    DIVISION=30
    DIVISION_FLOAT=31
    MOD=32
    NEGATIVE=33
    AND=34
    OR=35
    COMPARE=36
    IS_NOT_EQUAL=37
    LESS=38
    MORE_THAN=39
    LESS_OR_EQUAL=40
    MORE_OR_EQUAL=41
    NOT_EQUAL_FLOAT=42
    LESS_FLOAT=43
    MORE_FLOAT=44
    ESS_OR_EQUAL_FLOAT=45
    MORE_OR_EQUAL_FLOAT=46
    LEFT_ROUND_BRACKET=47
    RIGHT_ROUND_BRACKET=48
    LEFT_SQUARE_BRACKET=49
    RIGHT_SQUARE_BRACKET=50
    LEFT_CURLY_BRACKET=51
    RIGHT_CURLY_BRACKET=52
    COLON=53
    DOT=54
    COMMA=55
    INTEGER=56
    FLOAT=57
    BOOLEAN=58
    STRING=59
    LITERALS=60
    ARRAY=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    SEMI=64
    WS=65
    BLOCK_COMMENT=66
    UNTERMINATED_COMMENT=67
    ERROR_CHAR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





