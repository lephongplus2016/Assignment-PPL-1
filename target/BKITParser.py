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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("w\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\2\3\3\7\3#\n\3\f\3\16\3&\13\3")
        buf.write("\3\3\6\3)\n\3\r\3\16\3*\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\5\6\67\n\6\3\6\3\6\3\7\3\7\3\7\5\7>\n\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\tL\n\t")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13U\n\13\f\13\16\13")
        buf.write("X\13\13\3\13\3\13\7\13\\\n\13\f\13\16\13_\13\13\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\7\rg\n\r\f\r\16\rj\13\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16s\n\16\3\17\3\17\3\17\2\2\20")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\3\3\2<?\2t\2\36")
        buf.write("\3\2\2\2\4$\3\2\2\2\6,\3\2\2\2\b\60\3\2\2\2\n\62\3\2\2")
        buf.write("\2\f:\3\2\2\2\16B\3\2\2\2\20K\3\2\2\2\22M\3\2\2\2\24O")
        buf.write("\3\2\2\2\26`\3\2\2\2\30b\3\2\2\2\32r\3\2\2\2\34t\3\2\2")
        buf.write("\2\36\37\5\4\3\2\37 \7\2\2\3 \3\3\2\2\2!#\5\6\4\2\"!\3")
        buf.write("\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%(\3\2\2\2&$\3\2")
        buf.write("\2\2\')\5\n\6\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2")
        buf.write("\2+\5\3\2\2\2,-\7\3\2\2-.\5\b\5\2./\7C\2\2/\7\3\2\2\2")
        buf.write("\60\61\5\24\13\2\61\t\3\2\2\2\62\63\7\27\2\2\63\64\79")
        buf.write("\2\2\64\66\7\4\2\2\65\67\5\16\b\2\66\65\3\2\2\2\66\67")
        buf.write("\3\2\2\2\678\3\2\2\289\5\f\7\29\13\3\2\2\2:;\7\5\2\2;")
        buf.write("=\79\2\2<>\5\34\17\2=<\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7")
        buf.write("\21\2\2@A\7:\2\2A\r\3\2\2\2BC\7\16\2\2CD\79\2\2DE\5\22")
        buf.write("\n\2EF\5\20\t\2F\17\3\2\2\2GH\7;\2\2HI\5\22\n\2IJ\5\20")
        buf.write("\t\2JL\3\2\2\2KG\3\2\2\2KL\3\2\2\2L\21\3\2\2\2MN\5\24")
        buf.write("\13\2N\23\3\2\2\2OV\7\4\2\2PQ\7;\2\2QR\7\4\2\2RS\7\33")
        buf.write("\2\2SU\t\2\2\2TP\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2")
        buf.write("W]\3\2\2\2XV\3\2\2\2YZ\7;\2\2Z\\\7\4\2\2[Y\3\2\2\2\\_")
        buf.write("\3\2\2\2][\3\2\2\2]^\3\2\2\2^\25\3\2\2\2_]\3\2\2\2`a\t")
        buf.write("\2\2\2a\27\3\2\2\2bc\7\67\2\2ch\5\32\16\2de\7;\2\2eg\5")
        buf.write("\32\16\2fd\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2")
        buf.write("\2\2jh\3\2\2\2kl\78\2\2l\31\3\2\2\2ms\5\30\r\2ns\7<\2")
        buf.write("\2os\7>\2\2ps\7=\2\2qs\7?\2\2rm\3\2\2\2rn\3\2\2\2ro\3")
        buf.write("\2\2\2rp\3\2\2\2rq\3\2\2\2s\33\3\2\2\2tu\7\4\2\2u\35\3")
        buf.write("\2\2\2\13$*\66=KV]hr")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Var: '", "<INVALID>", "'Body'", "'Else'", 
                     "'Endfor'", "'If'", "'Var'", "'EndDo'", "'Break'", 
                     "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
                     "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", 
                     "'Do'", "'EndIf'", "'Function'", "'Then'", "'False'", 
                     "<INVALID>", "'='", "'+'", "'+.'", "'-'", "'-.'", "'*'", 
                     "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
                     "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "':'", "'.'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "BODY", "ELSE", "ENDFOR", 
                      "IF", "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", 
                      "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
                      "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", 
                      "FALSE", "KEYWORDS", "EQ", "ADD", "ADD_FLOAT", "SUB", 
                      "SUB_FLOAT", "MUL", "MUL_FLOAT", "DIVISION", "DIVISION_FLOAT", 
                      "MOD", "NEGATIVE", "AND", "OR", "COMPARE", "IS_NOT_EQUAL", 
                      "LESS", "MORE_THAN", "LESS_OR_EQUAL", "MORE_OR_EQUAL", 
                      "NOT_EQUAL_FLOAT", "LESS_FLOAT", "MORE_FLOAT", "ESS_OR_EQUAL_FLOAT", 
                      "MORE_OR_EQUAL_FLOAT", "LEFT_ROUND_BRACKET", "RIGHT_ROUND_BRACKET", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", 
                      "RIGHT_CURLY_BRACKET", "COLON", "DOT", "COMMA", "INTEGER", 
                      "FLOAT", "BOOLEAN", "STRING", "ARRAY", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "SEMI", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_var_list = 2
    RULE_many_var = 3
    RULE_function_list = 4
    RULE_function_body = 5
    RULE_param = 6
    RULE_many_param = 7
    RULE_one_param = 8
    RULE_id_list = 9
    RULE_primitive_type = 10
    RULE_array_type = 11
    RULE_value = 12
    RULE_statement = 13

    ruleNames =  [ "program", "declaration", "var_list", "many_var", "function_list", 
                   "function_body", "param", "many_param", "one_param", 
                   "id_list", "primitive_type", "array_type", "value", "statement" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    BODY=3
    ELSE=4
    ENDFOR=5
    IF=6
    VAR=7
    ENDDO=8
    BREAK=9
    ELSEIF=10
    ENDWHILE=11
    PARAMETER=12
    WHILE=13
    CONTINUE=14
    ENDBODY=15
    FOR=16
    RETURN=17
    TRUE=18
    DO=19
    ENDIF=20
    FUNCTION=21
    THEN=22
    FALSE=23
    KEYWORDS=24
    EQ=25
    ADD=26
    ADD_FLOAT=27
    SUB=28
    SUB_FLOAT=29
    MUL=30
    MUL_FLOAT=31
    DIVISION=32
    DIVISION_FLOAT=33
    MOD=34
    NEGATIVE=35
    AND=36
    OR=37
    COMPARE=38
    IS_NOT_EQUAL=39
    LESS=40
    MORE_THAN=41
    LESS_OR_EQUAL=42
    MORE_OR_EQUAL=43
    NOT_EQUAL_FLOAT=44
    LESS_FLOAT=45
    MORE_FLOAT=46
    ESS_OR_EQUAL_FLOAT=47
    MORE_OR_EQUAL_FLOAT=48
    LEFT_ROUND_BRACKET=49
    RIGHT_ROUND_BRACKET=50
    LEFT_SQUARE_BRACKET=51
    RIGHT_SQUARE_BRACKET=52
    LEFT_CURLY_BRACKET=53
    RIGHT_CURLY_BRACKET=54
    COLON=55
    DOT=56
    COMMA=57
    INTEGER=58
    FLOAT=59
    BOOLEAN=60
    STRING=61
    ARRAY=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    SEMI=65
    WS=66
    BLOCK_COMMENT=67
    UNTERMINATED_COMMENT=68
    ERROR_CHAR=69

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(BKITParser.DeclarationContext,0)


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
            self.state = 28
            self.declaration()
            self.state = 29
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_listContext,i)


        def function_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Function_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Function_listContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = BKITParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.T__0:
                self.state = 31
                self.var_list()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.function_list()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.FUNCTION):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def many_var(self):
            return self.getTypedRuleContext(BKITParser.Many_varContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(BKITParser.T__0)
            self.state = 43
            self.many_var()
            self.state = 44
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(BKITParser.Id_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_var" ):
                return visitor.visitMany_var(self)
            else:
                return visitor.visitChildren(self)




    def many_var(self):

        localctx = BKITParser.Many_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_many_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def function_body(self):
            return self.getTypedRuleContext(BKITParser.Function_bodyContext,0)


        def param(self):
            return self.getTypedRuleContext(BKITParser.ParamContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_list" ):
                return visitor.visitFunction_list(self)
            else:
                return visitor.visitChildren(self)




    def function_list(self):

        localctx = BKITParser.Function_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(BKITParser.FUNCTION)
            self.state = 49
            self.match(BKITParser.COLON)
            self.state = 50
            self.match(BKITParser.ID)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 51
                self.param()


            self.state = 54
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def statement(self):
            return self.getTypedRuleContext(BKITParser.StatementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = BKITParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(BKITParser.BODY)
            self.state = 57
            self.match(BKITParser.COLON)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ID:
                self.state = 58
                self.statement()


            self.state = 61
            self.match(BKITParser.ENDBODY)
            self.state = 62
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def one_param(self):
            return self.getTypedRuleContext(BKITParser.One_paramContext,0)


        def many_param(self):
            return self.getTypedRuleContext(BKITParser.Many_paramContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKITParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(BKITParser.PARAMETER)
            self.state = 65
            self.match(BKITParser.COLON)
            self.state = 66
            self.one_param()
            self.state = 67
            self.many_param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def one_param(self):
            return self.getTypedRuleContext(BKITParser.One_paramContext,0)


        def many_param(self):
            return self.getTypedRuleContext(BKITParser.Many_paramContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_many_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_param" ):
                return visitor.visitMany_param(self)
            else:
                return visitor.visitChildren(self)




    def many_param(self):

        localctx = BKITParser.Many_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_many_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.COMMA:
                self.state = 69
                self.match(BKITParser.COMMA)
                self.state = 70
                self.one_param()
                self.state = 71
                self.many_param()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_list(self):
            return self.getTypedRuleContext(BKITParser.Id_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_one_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_param" ):
                return visitor.visitOne_param(self)
            else:
                return visitor.visitChildren(self)




    def one_param(self):

        localctx = BKITParser.One_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_one_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.EQ)
            else:
                return self.getToken(BKITParser.EQ, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER)
            else:
                return self.getToken(BKITParser.INTEGER, i)

        def BOOLEAN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.BOOLEAN)
            else:
                return self.getToken(BKITParser.BOOLEAN, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.FLOAT)
            else:
                return self.getToken(BKITParser.FLOAT, i)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.STRING)
            else:
                return self.getToken(BKITParser.STRING, i)

        def getRuleIndex(self):
            return BKITParser.RULE_id_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId_list" ):
                return visitor.visitId_list(self)
            else:
                return visitor.visitChildren(self)




    def id_list(self):

        localctx = BKITParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_id_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(BKITParser.ID)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 78
                    self.match(BKITParser.COMMA)
                    self.state = 79
                    self.match(BKITParser.ID)
                    self.state = 80
                    self.match(BKITParser.EQ)
                    self.state = 81
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.STRING))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87
                    self.match(BKITParser.COMMA)
                    self.state = 88
                    self.match(BKITParser.ID) 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKITParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTEGER) | (1 << BKITParser.FLOAT) | (1 << BKITParser.BOOLEAN) | (1 << BKITParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_CURLY_BRACKET(self):
            return self.getToken(BKITParser.LEFT_CURLY_BRACKET, 0)

        def RIGHT_CURLY_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_CURLY_BRACKET, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ValueContext)
            else:
                return self.getTypedRuleContext(BKITParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKITParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKITParser.LEFT_CURLY_BRACKET)

            self.state = 97
            self.value()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 98
                self.match(BKITParser.COMMA)
                self.state = 99
                self.value()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(BKITParser.RIGHT_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(BKITParser.Array_typeContext,0)


        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = BKITParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        try:
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LEFT_CURLY_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.array_type()
                pass
            elif token in [BKITParser.INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.match(BKITParser.INTEGER)
                pass
            elif token in [BKITParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(BKITParser.BOOLEAN)
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 110
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 111
                self.match(BKITParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





