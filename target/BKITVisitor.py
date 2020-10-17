# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#declaration.
    def visitDeclaration(self, ctx:BKITParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_var.
    def visitMany_var(self, ctx:BKITParser.Many_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_list.
    def visitFunction_list(self, ctx:BKITParser.Function_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_name.
    def visitFunction_name(self, ctx:BKITParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_body.
    def visitFunction_body(self, ctx:BKITParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#many_param.
    def visitMany_param(self, ctx:BKITParser.Many_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#one_param.
    def visitOne_param(self, ctx:BKITParser.One_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#id_list.
    def visitId_list(self, ctx:BKITParser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKITParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_type.
    def visitArray_type(self, ctx:BKITParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#value.
    def visitValue(self, ctx:BKITParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#integer_arithmetic_type.
    def visitInteger_arithmetic_type(self, ctx:BKITParser.Integer_arithmetic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#integer_relation_type.
    def visitInteger_relation_type(self, ctx:BKITParser.Integer_relation_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_arithmetic_type.
    def visitFloat_arithmetic_type(self, ctx:BKITParser.Float_arithmetic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_relation_type.
    def visitFloat_relation_type(self, ctx:BKITParser.Float_relation_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_type.
    def visitBool_type(self, ctx:BKITParser.Bool_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_index.
    def visitArray_index(self, ctx:BKITParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index.
    def visitIndex(self, ctx:BKITParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign.
    def visitAssign(self, ctx:BKITParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#white_statement.
    def visitWhite_statement(self, ctx:BKITParser.White_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_white_statement.
    def visitDo_white_statement(self, ctx:BKITParser.Do_white_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp8.
    def visitExp8(self, ctx:BKITParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp9.
    def visitExp9(self, ctx:BKITParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_of_float.
    def visitInt_of_float(self, ctx:BKITParser.Int_of_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_to_int.
    def visitFloat_to_int(self, ctx:BKITParser.Float_to_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_of_string.
    def visitInt_of_string(self, ctx:BKITParser.Int_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_int.
    def visitString_of_int(self, ctx:BKITParser.String_of_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_to_string.
    def visitFloat_to_string(self, ctx:BKITParser.Float_to_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_float.
    def visitString_of_float(self, ctx:BKITParser.String_of_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_of_string.
    def visitBool_of_string(self, ctx:BKITParser.Bool_of_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_of_bool.
    def visitString_of_bool(self, ctx:BKITParser.String_of_boolContext):
        return self.visitChildren(ctx)



del BKITParser