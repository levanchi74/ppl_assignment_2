
# Name: Le Van Chi 
# MSSV: 1510289

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

def flatten(lst):
    flat = []
    for i in lst:
        if(isinstance(i,list)):
            for j in i:
                flat.append(j)
        else:
            flat.append(i)
    return flat

class ASTGeneration(MCVisitor):
    #program : decl+ EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(flatten([self.visit(x) for x in ctx.decl()]))

    #decl : vardecl | funcdecl;
    def visitDecl(self,ctx:MCParser.DeclContext):
        return self.visit(ctx.getChild(0))

    #vardecl : primtype varlist SEMI;
    #varlist : var (COMMA var)*;
    #var: ID (LS INLIT RS)?;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        result = []
        for x in self.visit(ctx.varlist()):
            if(isinstance(x,tuple)):
                result += [(x[0].getText(), ArrayType(IntLiteral(x[1]), self.visit(ctx.primtype())))]
            else:
                result += [(x.getText(), self.visit(ctx.primtype()))]
        return [VarDecl(a,b) for (a,b) in result]

    def visitVarlist(self,ctx:MCParser.VarlistContext):
        return [self.visit(x) for x in ctx.var()]

    def visitVar(self,ctx:MCParser.VarContext):
        return (ctx.ID(),ctx.INTLIT()) if ctx.INTLIT() else ctx.ID()

    #primtype : BOOLEANTYPE | INTTYPE | FLOATTYPE | STRINGTYPE ;
    def visitPrimtype(self,ctx:MCParser.PrimtypeContext):
        if ctx.BOOLEANTYPE():
            return BoolType()
        if ctx.INTTYPE():
            return IntType()
        if ctx.FLOATTYPE():
            return FloatType()
        return StringType()

    #funcdecl: returntype ID LB paralist? RB blockstmt;
    def visitFuncdecl(self,ctx:MCParser.FuncdeclContext):
        return FuncDecl(Id(ctx.ID().getText()),
                        self.visit(ctx.paralist()) if ctx.paralist() else [],
                        self.visit(ctx.returntype()),
                        self.visit(ctx.blockstmt()))

    #returntype: primtype | VOIDTYPE | arrptrtype;
    def visitReturntype(self, ctx:MCParser.ReturntypeContext):
        if(ctx.VOIDTYPE()):
            return VoidType()
        return self.visit(ctx.getChild(0))

    #arrptrtype : primtype LS RS;
    def visitArrptrtype(self,ctx:MCParser.ArrptrtypeContext):
        return ArrayPointerType(self.visit(ctx.primtype()))

    #paralist: para (COMMA para)*;
    def visitParalist(self,ctx:MCParser.ParalistContext):
        return flatten([self.visit(x) for x in ctx.para()])

    #para: primtype ID (LS RS)?;
    def visitPara(self,ctx:MCParser.ParaContext):
        paraid = ctx.ID().getText()
        paratype = ArrayPointerType(self.visit(ctx.primtype())) if ctx.LS() else self.visit(ctx.primtype())
        return VarDecl(paraid, paratype)

    #blockstmt: LP vardecl_stmt* RP;
    #vardecl_stmt: vardecl | stmt ;
    def visitBlockstmt(self,ctx:MCParser.ParaContext):
        return Block(flatten([self.visit(x) for x in ctx.vardecl_stmt()]))
    def visitVardecl_stmt(self,ctx:MCParser.Vardecl_stmtContext):
        return self.visit(ctx.getChild(0))

    #stmt: ifstmt | dowhilestmt | forstmt | breakstmt | contistmt | returnstmt | expstmt | blockstmt;
    def visitStmt(self,ctx:MCParser.StmtContext):
        return self.visit(ctx.getChild(0))

    #ifstmt: IF LB exp RB stmt (ELSE stmt)?;
    def visitIfstmt(self,ctx:MCParser.IfstmtContext):
        expr = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.stmt(0))
        if(ctx.ELSE()):
            elseStmt = self.visit(ctx.stmt(1))
            return If(expr,thenStmt,elseStmt)
        else:
            return If(expr,thenStmt)

    #dowhilestmt: DO stmt+ WHILE exp SEMI;
    def visitDowhilestmt(self,ctx:MCParser.DowhilestmtContext):
        stmtList = flatten([self.visit(x) for x in ctx.stmt()])
        expr = self.visit(ctx.exp())
        return Dowhile(stmtList, expr)

    #forstmt: FOR LB exp SEMI exp SEMI exp RB stmt;
    def visitForstmt(self,ctx:MCParser.ForstmtContext):
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        exp3 = self.visit(ctx.exp(2))
        loop = self.visit(ctx.stmt())
        return For(exp1,exp2,exp3,loop)

    #breakstmt:   BREAK SEMI;
    def visitBreakstmt(self,ctx:MCParser.BreakstmtContext):
        return Break();

    #contistmt:   CONTINUE SEMI;
    def visitContistmt(self,ctx:MCParser.ContistmtContext):
        return Continue();

    #returnstmt:  RETURN exp? SEMI;
    def visitReturnstmt(self,ctx:MCParser.ReturnstmtContext):
        return Return(self.visit(ctx.exp())) if ctx.exp() else Return()

    #expstmt: exp SEMI;
    def visitExpstmt(self,ctx:MCParser.ExpstmtContext):
        return self.visit(ctx.exp())

    #exp : exp1 ASSIGN exp  | exp1;
    def visitExp(self,ctx:MCParser.ExpContext):
        if(ctx.ASSIGN()):
            op = ctx.ASSIGN().getText()
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.getChild(0))

    #exp1: exp1 OROP exp2  | exp2;
    def visitExp1(self,ctx:MCParser.Exp1Context):
        if(ctx.OROP()):
            op = ctx.OROP().getText()
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.getChild(0))

    #exp2: exp2 ANDOP exp3 | exp3;
    def visitExp2(self,ctx:MCParser.Exp2Context):
        if(ctx.ANDOP()):
            op = ctx.ANDOP().getText()
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            return BinaryOp(op,left,right)
        else :
            return self.visit(ctx.getChild(0))

    #exp3: exp4 EQUALOP exp4 | exp4;
    def visitExp3(self,ctx:MCParser.Exp3Context):
        if(ctx.EQUALOP()):
            op = ctx.EQUALOP().getText()
            left = self.visit(ctx.exp4(0))
            right = self.visit(ctx.exp4(1))
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.getChild(0))

    #exp4: exp5 COMPOP exp5 | exp5;
    def visitExp4(self,ctx:MCParser.Exp4Context):
        if(ctx.COMPOP()):
            op = ctx.COMPOP().getText()
            left = self.visit(ctx.exp5(0))
            right = self.visit(ctx.exp5(1))
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.getChild(0))

    #exp5: exp5 (ADDOP | SUBOP) exp6 | exp6;
    def visitExp5(self,ctx:MCParser.Exp5Context):
        if(ctx.getChildCount() == 3):
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp5())
            right = self.visit(ctx.exp6())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.getChild(0))

    #exp6: exp6 (MULOP | DIVOP | MODOP) exp7 | exp7;
    def visitExp6(self,ctx:MCParser.Exp6Context):
        if(ctx.getChildCount() == 3):
            op = ctx.getChild(1).getText()
            left = self.visit(ctx.exp6())
            right = self.visit(ctx.exp7())
            return BinaryOp(op,left,right)
        else:
            return self.visit(ctx.getChild(0))

    #exp7: (SUBOP | NEGOP) exp7 | exp8;    // ?
    def visitExp7(self,ctx:MCParser.Exp7Context):
        if(ctx.getChildCount() == 2):
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.exp7())
            return UnaryOp(op,body)
        else:
            return self.visit(ctx.getChild(0))

    #exp8:   LB exp RB | literal | ID | funcall | elearray;
    def visitExp8(self,ctx:MCParser.Exp8Context):
        if(ctx.getChildCount() == 3):
            return self.visit(ctx.exp())
        elif(ctx.literal()):
            return self.visit(ctx.literal())
        elif(ctx.ID()):
            return Id(ctx.ID().getText())
        elif(ctx.funcall()):
            return self.visit(ctx.funcall())
        else:
            return self.visit(ctx.elearray())


    #funcall : ID LB (exp (COMMA exp)*)? RB;
    def visitFuncall(self,ctx:MCParser.FuncallContext):
        method = Id(ctx.ID().getText())  # Id
        param = flatten([self.visit(x) for x in ctx.exp()]) if ctx.exp() else []
        return CallExpr(method,param)

    #elearray: ( ID | funcall | literal) LS exp RS;
    def visitElearray(self,ctx:MCParser.ElearrayContext):
        idx = self.visit(ctx.exp())
        if(ctx.ID()):
            arr = Id(ctx.ID().getText())
        elif(ctx.funcall()):
            arr = self.visit(ctx.funcall())
        else:
            arr = self.visit(ctx.literal())
        return ArrayCell(arr, idx)

    #literal: INTLIT | FLOATLIT | BOOLEANLIT | STRINGLIT ;
    def visitLiteral(self,ctx:MCParser.LiteralContext):
        if(ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif(ctx.FLOATLIT()):
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif(ctx.BOOLEANLIT()):
            return BooleanLiteral(True if ctx.BOOLEANLIT().getText().lower()=="true" else False)
        else:
            return StringLiteral(ctx.STRINGLIT().getText())