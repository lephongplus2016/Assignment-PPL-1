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


    # Visit a parse tree produced by BKITParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKITParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_type.
    def visitArray_type(self, ctx:BKITParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#value.
    def visitValue(self, ctx:BKITParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)



del BKITParser