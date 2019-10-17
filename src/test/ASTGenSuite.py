import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_vardecl(self):
        input = """ int a; """
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_vardecl_multi_var(self):
        input = """ float a, b; """
        expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_vardecl_arraytype(self):
        input = """ boolean a, b[1]; """
        expect = str(Program([VarDecl("a",BoolType()),VarDecl("b",ArrayType(IntLiteral(1),BoolType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_vardecl_more(self):
        input = """ string a, b[1], c, d[5]; """
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",ArrayType(IntLiteral(1),StringType())),VarDecl("c",StringType()),VarDecl("d",ArrayType(IntLiteral(5),StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_multi_vardecl(self):
        input = """
                int x,y,arr[5];
                string str;
                boolean bool[10];
                //temp = 1;
                float d1,d2;
                """
        expect = str(Program([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("arr",ArrayType(IntLiteral(5),IntType())),VarDecl("str",StringType()),VarDecl("bool",ArrayType(IntLiteral(10),BoolType())),VarDecl("d1",FloatType()),VarDecl("d2",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_void_func(self):
        input = """void _func() {}"""
        expect = str(Program([FuncDecl(Id("_func"),[],VoidType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_boolean_func(self):
        input = """boolean _func() {}"""
        expect = str(Program([FuncDecl(Id("_func"),[],BoolType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_string_func(self):
        input = """string _func() {}"""
        expect = str(Program([FuncDecl(Id("_func"),[],StringType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_int_func(self):
        input = """int _func() {}"""
        expect = str(Program([FuncDecl(Id("_func"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_arraytypepoint_func(self):
        input = """int[] _func() {}"""
        expect = str(Program([FuncDecl(Id("_func"),[],ArrayPointerType(IntType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    def test_vardecl_vs_func(self):
        input = """
                int i,arr[5];
                int _func() {}
                string str;
                """
        expect = str(Program([VarDecl("i",IntType()),VarDecl("arr",ArrayType(IntLiteral(5),IntType())),FuncDecl(Id("_func"),[],IntType(),Block([])),VarDecl("str",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_func_with_one_param_primtype(self):
        input = """
                float func(int x) {
                    int a;
                }
                """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("x",IntType())],FloatType(),Block([VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_func_with_param_arraytype(self):
        input = """
                float func(float d[]){
                    int a;
                }
                """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("d",ArrayPointerType(FloatType()))],FloatType(),Block([VarDecl("a",IntType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_func_with_multi_param(self):
        input = """
                float func(int x,float d[],string str, boolean status){}
                """
        expect = str(Program([FuncDecl(Id("func"),[VarDecl("x",IntType()),VarDecl("d",ArrayPointerType(FloatType())),VarDecl("str",StringType()),VarDecl("status",BoolType())],FloatType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_func_vardecl_in_blockstmt(self):
        input = """
                int main(){
                    int x,y;
                    float d[5];
                    string str;
                    boolean status;
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),VarDecl("y",IntType()),VarDecl("d",ArrayType(IntLiteral(5),FloatType())),VarDecl("str",StringType()),VarDecl("status",BoolType())]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_ifstmt_simple_with_block(self):
        input = """
                int main() {
                    if(i>0){}
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(0)),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_ifstmt_simple_with_block(self):
        input = """
                int main() {
                    if(i==1){
                        int x;
                    }
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("==",Id("i"),IntLiteral(1)),Block([VarDecl("x",IntType())]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_ifstmt_with_vardecl(self):
        input = """
                int main() {
                    int x;
                    if(i==1){
                        y = 10;
                    }
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("x",IntType()),If(BinaryOp("==",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("y"),IntLiteral(10))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_ifstmt_else(self):
        input = """
                int main() {
                    boolean status;
                    if(i==1){
                        status = true;
                    }else{
                        status = false;
                    }
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("status",BoolType()),If(BinaryOp("==",Id("i"),IntLiteral(1)),Block([BinaryOp("=",Id("status"),BooleanLiteral("true"))]),Block([BinaryOp("=",Id("status"),BooleanLiteral("false"))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_if_ANDOP(self):
        input = """
                int main() {
                    if(x > 0 && x < 10){}
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp(">",Id("x"),IntLiteral(0)),BinaryOp("<",Id("x"),IntLiteral(10))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_if_OROP(self):
        input = """
                int main() {
                    if(x <= 0 || x > 10){}
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("<=",Id("x"),IntLiteral(0)),BinaryOp(">",Id("x"),IntLiteral(10))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_if_EQUAOP(self):
        input = """
                int main() {
                    if(x == 1 || x != 10){}
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("==",Id("x"),IntLiteral(1)),BinaryOp("!=",Id("x"),IntLiteral(10))),Block([]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_dowhile_simple(self):
        input = """
                int main(){
                do {
                    int a ;
                    a = a + 1; 
                }
                while( a == b ) ;
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],BinaryOp("==",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_dowhile_operators(self):
        input = """
                int main(){
                do {
                    int a,b[2];
                    x = x+ 1;
                    k = arr[1];
                    j = (x*k)-1;
                }
                while( a < 10 || status == true ) ;
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Dowhile([Block([VarDecl("a",IntType()),VarDecl("b",ArrayType(IntLiteral(2),IntType())),BinaryOp("=",Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),BinaryOp("=",Id("k"),ArrayCell(Id("arr"),IntLiteral(1))),BinaryOp("=",Id("j"),BinaryOp("-",Id("x"),IntLiteral(1)))])],BinaryOp("||",BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("==",Id("status"),BooleanLiteral("true"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))