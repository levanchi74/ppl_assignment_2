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
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([VarDecl(a,IntType),VarDecl(b,ArrayType(IntType,IntLiteral(2))),BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1))),BinaryOp(=,Id(k),ArrayCell(Id(arr),IntLiteral(1))),BinaryOp(=,Id(j),BinaryOp(-,BinaryOp(*,Id(x),Id(k)),IntLiteral(1)))])],BinaryOp(||,BinaryOp(<,Id(a),IntLiteral(10)),BinaryOp(==,Id(status),BooleanLiteral(true))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_for_stmt1(self):
        """ Test For Statement """
        input = """
                void main(){
                    for (a=1; a < 10; a=a+1){}
                      
                }
                """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("a"),IntLiteral(1)),BinaryOp("<",Id("a"),IntLiteral(10)),BinaryOp("=",Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),Block([]))]))]))
        #expect = """Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_for_stmt2(self):
        input = """
                void main(){
                    int a;
                    int b;
                    boolean c;
                    for (a=1; a < 10; a=a+1){
                        if (a % 2 == 0){
                            c = false;
                            b = b + 1;
                        }
                    }
                }
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([BinaryOp(=,Id(c),BooleanLiteral(false)),BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_for_stmt3(self):
        input = """
                void main(){
                    int a;
                    int b;
                    boolean c;
                    for (a=1; a < 10; a=a+1){
                        for (b=0; b != 10; b=b+1){
                            c = b;
                        }
                        b = a + 1;
                    }
                }
                """
        #expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([BinaryOp(=,Id(c),Id(b))])),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])"
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,BoolType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([BinaryOp(=,Id(c),Id(b))])),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_for_stmt4(self):
        input = """
                void main(){
                    x = b*10 ;
                    y = b/10;
                    z = b%10;
                }
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(x),BinaryOp(*,Id(b),IntLiteral(10))),BinaryOp(=,Id(y),BinaryOp(/,Id(b),IntLiteral(10))),BinaryOp(=,Id(z),BinaryOp(%,Id(b),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_for_stmt4(self):
        """ Test For Statement """
        input = r"""void main(){
            for (a=1;a<10;a=a+1){
                for(b=2;b%10==0;b=b+1){
                    int c;
                    float d;
                    c = b;
                    d = a;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,BinaryOp(%,Id(b),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(c,IntType),VarDecl(d,FloatType),BinaryOp(=,Id(c),Id(b)),BinaryOp(=,Id(d),Id(a))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_for_stmt5(self):
        """ Test For Statement """
        input = """
                void main(){
                    int a;
                    float b;
                    string c;
                    for (a=1; a % 10 == 0; a=a+1){
                        if (a % 2 == 0){
                            for (b=0; b != 1;b=b+2){
                                int a;
                                float b;
                                b = a;
                            }
                        }
                    }
                }
                """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,FloatType),BinaryOp(=,Id(b),Id(a))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_for_stmt6(self):
        input = r"""void main(){
            int a;
            float b;
            string c;
            for (a=1; a % 10 == 0; a=a+1){
                if (a % 2 == 0){
                    for (b=0; b != 1;b=b+2){
                        int a;
                        float b;
                        b = a;
                        for (b=1;b==10;b=b+1){
                            string c;
                            c = b;
                            if (c){
                                float a;
                                string d;
                                d = c;
                            }
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,StringType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(10)),IntLiteral(0));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)),Block([For(BinaryOp(=,Id(b),IntLiteral(0));BinaryOp(!=,Id(b),IntLiteral(1));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,FloatType),BinaryOp(=,Id(b),Id(a)),For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([VarDecl(c,StringType),BinaryOp(=,Id(c),Id(b)),If(Id(c),Block([VarDecl(a,FloatType),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(c))]))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_for_stmt7(self):
        """ Test For Statement """
        input = r"""void main(){
            int a,b,c;
            for (a=1;a<100;a=a+1){
                for(b=1;b<10;b=b+1){
                    for(c=1;c<50;c=c+1){
                        if (c){
                            string rlt;
                            rlt = c;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(100));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(1));BinaryOp(<,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([For(BinaryOp(=,Id(c),IntLiteral(1));BinaryOp(<,Id(c),IntLiteral(50));BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)));Block([If(Id(c),Block([VarDecl(rlt,StringType),BinaryOp(=,Id(rlt),Id(c))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_for_stmt8(self):
        """ Test For Statement """
        input = r"""void main(){
            for (a=1;a<10;a=a*2){
                for(b=2;b==10;b=b*2){
                    for(c=100;c!=0;c=c%2){
                        for(d=1000;d>0;d=d%10){
                            int e;
                            e = d;
                            string d;
                            d = e;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_for_stmt9(self):
        input = r"""void main(){
            for (a=1;a<10;a=a*2){
                for(b=2;b==10;b=b*2){
                    int a;
                    string b;
                    b = a + 1;
                }
            }
            for(c=100;c!=0;c=c%2){
                for(d=1000;d>0;d=d%10){
                    int e;
                    e = d;
                    string d;
                    d = e;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,StringType),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))])),For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_for_stmt10(self):
        """ Test For Statement """
        input = r"""void main(){
            for (a=1;a<10;a=a*2){
                for(b=2;b==10;b=b*2){
                    int a;
                    string b;
                    b = a + 1;
                }
            }
            for(d=1;d!=1;d=d+1){
                int e;
                e = d;
            }
            for(c=100;c!=0;c=c%2){
                for(d=1000;d>0;d=d%10){
                    int e;
                    e = d;
                    string d;
                    d = e;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,StringType),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))])),For(BinaryOp(=,Id(d),IntLiteral(1));BinaryOp(!=,Id(d),IntLiteral(1));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d))])),For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_break_stmt1(self):
        input = r"""void main(){
            break;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_break_stmt2(self):
        input = r"""void main(){
            break;
            break;
            break;
            break;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Break(),Break(),Break(),Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_break_stmt3(self):
        """ Test Break Statement """
        input = r"""void main(){
            for(i=1;i<10;i=i+1){
                if (true)
                    break;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BooleanLiteral(true),Break())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_break_stmt4(self):
        """ Test Break Statement """
        input = r"""void main(){
            int a;
            for(i=1;i<10;i=i+1){
                for(j=i;j<5;j=j+1){
                    if (true)
                        break;
                    else
                        a = a * 2;
                }
                if (a == 10)
                    break;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),Id(i));BinaryOp(<,Id(j),IntLiteral(5));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([If(BooleanLiteral(true),Break(),BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2))))])),If(BinaryOp(==,Id(a),IntLiteral(10)),Break())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_break_stmt5(self):
        input = r"""void main(){
            for(i=1;i<10;i=i+1){
                if (true)
                    break;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BooleanLiteral(true),Break())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_continue_stmt1(self):
        input = r"""void main(){
            for(a=1;a<10;a=a+1){
                if (true)
                    continue;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BooleanLiteral(true),Continue())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_continue_stmt2(self):
        """ Test Continue Statement """
        input = r"""void main(){
            for(a=1;a<10;a=a+1){
                if (true){
                    continue;
                    continue;
                    continue;
                }
                continue;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BooleanLiteral(true),Block([Continue(),Continue(),Continue()])),Continue()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_continue_stmt3(self):
        """ Test Continue Statement """
        input = r"""void main(){
            for(a=1;a<10;a=a+1){
                for (b=2;b/2==0; b=b+1){
                    if (b%2 == 0)
                        continue;
                    else
                        break;
                }
                continue;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,BinaryOp(/,Id(b),IntLiteral(2)),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(b),IntLiteral(2)),IntLiteral(0)),Continue(),Break())])),Continue()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_continue_stmt4(self):
        """ Test Continue Statement """
        input = r"""void main(){
            for(a=1;a<10;a=a+1){
                for (b=2;b/2==0; b=b+1){
                    for(c=3;c!=0;c=c-1){
                        continue;
                    }
                    continue;
                }
                continue;
            }
            break;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,BinaryOp(/,Id(b),IntLiteral(2)),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([For(BinaryOp(=,Id(c),IntLiteral(3));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(-,Id(c),IntLiteral(1)));Block([Continue()])),Continue()])),Continue()])),Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_continue_stmt5(self):
        """ Test Continue Statement """
        input = r"""void main(){
            for(a=1;a<10;a=a+1){
                for (b=2;b/2==0; b=b+1){
                    for(c=3;c!=0;c=c-1){
                        continue;
                    }
                    do {
                        if (c != 1)
                            continue;
                    }while true;
                    continue;
                }
                continue;
            }
            break;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,BinaryOp(/,Id(b),IntLiteral(2)),IntLiteral(0));BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)));Block([For(BinaryOp(=,Id(c),IntLiteral(3));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(-,Id(c),IntLiteral(1)));Block([Continue()])),Dowhile([Block([If(BinaryOp(!=,Id(c),IntLiteral(1)),Continue())])],BooleanLiteral(true)),Continue()])),Continue()])),Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_return_voidtype_stmt1(self):
        """ Test Return Void Type Statement """
        input = r"""void main(){
            return;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_return_voidtype_stmt2(self):
        """ Test Return Void Type Statement """
        input = r"""void main(){return;}
        void main1(){return;}
        void main2(){return;}
        void main3(){return;}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Return()])),FuncDecl(Id(main1),[],VoidType,Block([Return()])),FuncDecl(Id(main2),[],VoidType,Block([Return()])),FuncDecl(Id(main3),[],VoidType,Block([Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_return_voidtype_stmt3(self):
        """ Test Return Void Type Statement """
        input = r"""void main(){
            boolean a;
            a = true;
            if (a)
                return;
            else
                main();
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,BoolType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(Id(a),Return(),CallExpr(Id(main),[]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_return_voidtype_stmt4(self):
        """ Test Return Void Type Statement """
        input = r"""void main(){
            int a;
            for (a=1;a<10;a=a+1){
                if (a == 5)
                    break;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([If(BinaryOp(==,Id(a),IntLiteral(5)),Break())]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    # TODO return voidtype with dowhile
    def test_return_voidtype_stmt5(self):
        """ Test Return Void Type Statement """
        input = r"""void main(){
            do{
                string a;
                int b;
                b = a;
                if (!a)
                    return;
            }while true;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([VarDecl(a,StringType),VarDecl(b,IntType),BinaryOp(=,Id(b),Id(a)),If(UnaryOp(!,Id(a)),Return())])],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_return_primitivetype_stmt1(self):
        """ Test Return Primitive Type Statement """
        input = r"""
        int main(){
            int a;
            return a;
        }
        float main(){
            float a;
            return a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),Return(Id(a))])),FuncDecl(Id(main),[],FloatType,Block([VarDecl(a,FloatType),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_return_primitivetype_stmt2(self):
        """ Test Return Primitive Type Statement """
        input = r"""
        string main(){
            string a;
            return a;
        }
        boolean main(){
            boolean a;
            return a;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],StringType,Block([VarDecl(a,StringType),Return(Id(a))])),FuncDecl(Id(main),[],BoolType,Block([VarDecl(a,BoolType),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_return_primitivetype_stmt3(self):
        """ Test Return Primitive Type Statement """
        input = r"""void main(){
            int a[10];
            for(i=0;i<10;i=i+1){
                a[i] = 1;
            }
            return a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,ArrayType(IntType,IntLiteral(10))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(1))])),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_return_primitivetype_stmt4(self):
        """ Test Return Primitive Type Statement """
        input = r"""
        int[] main(){
            int a[10];
            for(i=0;i<10;i=i+1){
                a[i] = 1;
            }
            return a;
        }
        float[] main(){
            float b[5];
            for(i=0;i<5;i=i+1)
                b[i] = 1;
            return b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([VarDecl(a,ArrayType(IntType,IntLiteral(10))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),IntLiteral(1))])),Return(Id(a))])),FuncDecl(Id(main),[],ArrayTypePointer(FloatType),Block([VarDecl(b,ArrayType(FloatType,IntLiteral(5))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,ArrayCell(Id(b),Id(i)),IntLiteral(1))),Return(Id(b))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_return_primitivetype_stmt5(self):
        """ Test Return Primitive Type Statement """
        input = r"""
        string[] main(){
            string a[10];
            for(i=0;i<10;i=i+1){
                a[i] = str(i);
            }
            return a;
        }
        boolean[] main(){
            boolean a[10];
            for(i=0;i<10;i=i+1){
                if (i % 2 == 0)
                    a[i] = true;
                else
                    a[i] = false;
            }
            return a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(StringType),Block([VarDecl(a,ArrayType(StringType,IntLiteral(10))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),CallExpr(Id(str),[Id(i)]))])),Return(Id(a))])),FuncDecl(Id(main),[],ArrayTypePointer(BoolType),Block([VarDecl(a,ArrayType(BoolType,IntLiteral(10))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,Id(i),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,ArrayCell(Id(a),Id(i)),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(a),Id(i)),BooleanLiteral(false)))])),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_call_func1(self):
        """ Test Call Function """
        input = r"""
        int main(){
            return sum(a,b);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Return(CallExpr(Id(sum),[Id(a),Id(b)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_call_func2(self):
        """ Test Call Function """
        input = r"""
        float main(){
            a = div(a,b);
            return a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],FloatType,Block([BinaryOp(=,Id(a),CallExpr(Id(div),[Id(a),Id(b)])),Return(Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_call_func3(self):
        """ Test Call Function """
        input = r"""
        string main(string args[]){
            string rlt;
            for(i=0;i<len(args);i=i+1){
                rlt = rlt + str(i);
            }
            return rlt;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],StringType,Block([VarDecl(rlt,StringType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),CallExpr(Id(len),[Id(args)]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(rlt),BinaryOp(+,Id(rlt),CallExpr(Id(str),[Id(i)])))])),Return(Id(rlt))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_call_func4(self):
        """ Test Call Function """
        input = r"""
        void main(string a){
            print(a);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,StringType)],VoidType,Block([CallExpr(Id(print),[Id(a)])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_call_func5(self):
        """ Test Call Function """
        input = r"""
        int main(int c[]){
            int rlt;
            rlt = div(sub(mul(c[0], 10),10),10);
            return rlt;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([VarDecl(rlt,IntType),BinaryOp(=,Id(rlt),CallExpr(Id(div),[CallExpr(Id(sub),[CallExpr(Id(mul),[ArrayCell(Id(c),IntLiteral(0)),IntLiteral(10)]),IntLiteral(10)]),IntLiteral(10)])),Return(Id(rlt))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_expression1(self):
        """ Test Expression Function """
        input = r"""
        int main(int c){
            rlt = 1 + 1 + 1 + c;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(c,IntType)],IntType,Block([BinaryOp(=,Id(rlt),BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(1)),IntLiteral(1)),Id(c)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_expression2(self):
        """ Test Expression Function """
        input = r"""
        void main(){
            rlt = 1 + 1 / 2 * 3 % 4 - 5;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(rlt),BinaryOp(-,BinaryOp(+,IntLiteral(1),BinaryOp(%,BinaryOp(*,BinaryOp(/,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4))),IntLiteral(5)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_expression3(self):
        """ Test Expression Function """
        input = r"""
        void main(){
            rlt = 1 + 1 / 2 * 3 % 4 - 5;
            a = true;
            b = rlt + a;
            if (a)
                return;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(rlt),BinaryOp(-,BinaryOp(+,IntLiteral(1),BinaryOp(%,BinaryOp(*,BinaryOp(/,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4))),IntLiteral(5))),BinaryOp(=,Id(a),BooleanLiteral(true)),BinaryOp(=,Id(b),BinaryOp(+,Id(rlt),Id(a))),If(Id(a),Return())]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_expression4(self):
        """ Test Expression Function """
        input = r"""
        void main(){
            s = a +b + c * d;
            d = a && b;
            e = !a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(s),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),BinaryOp(*,Id(c),Id(d)))),BinaryOp(=,Id(d),BinaryOp(&&,Id(a),Id(b))),BinaryOp(=,Id(e),UnaryOp(!,Id(a)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_expression5(self):
        """ Test Expression Function """
        input = r"""
        int[] main(){
            int a[1];
            if (true) return a;
            else return b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([VarDecl(a,ArrayType(IntType,IntLiteral(1))),If(BooleanLiteral(true),Return(Id(a)),Return(Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_expression6(self):
        """ Test Expression Function """
        input = r"""
        void main(){
            3[3+x] = true[b[2]] +3;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,ArrayCell(IntLiteral(3),BinaryOp(+,IntLiteral(3),Id(x))),BinaryOp(+,ArrayCell(BooleanLiteral(true),ArrayCell(Id(b),IntLiteral(2))),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_expression7(self):
        """ Test Expression Function """
        input = r"""
        void main(){
            float a, b, c, x, y, z;
            a = 9;
            b = 12;
            c = 3;
            x = a - b / 3 + c * 2 - 1;
            y = a - b / (3 + c) * (2 - 1);
            z = a - ( b / (3 + c) * 2) - 1;
            printf (x);
            printf (y);
            printf (z);
            return 0;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType),VarDecl(x,FloatType),VarDecl(y,FloatType),VarDecl(z,FloatType),BinaryOp(=,Id(a),IntLiteral(9)),BinaryOp(=,Id(b),IntLiteral(12)),BinaryOp(=,Id(c),IntLiteral(3)),BinaryOp(=,Id(x),BinaryOp(-,BinaryOp(+,BinaryOp(-,Id(a),BinaryOp(/,Id(b),IntLiteral(3))),BinaryOp(*,Id(c),IntLiteral(2))),IntLiteral(1))),BinaryOp(=,Id(y),BinaryOp(-,Id(a),BinaryOp(*,BinaryOp(/,Id(b),BinaryOp(+,IntLiteral(3),Id(c))),BinaryOp(-,IntLiteral(2),IntLiteral(1))))),BinaryOp(=,Id(z),BinaryOp(-,BinaryOp(-,Id(a),BinaryOp(*,BinaryOp(/,Id(b),BinaryOp(+,IntLiteral(3),Id(c))),IntLiteral(2))),IntLiteral(1))),CallExpr(Id(printf),[Id(x)]),CallExpr(Id(printf),[Id(y)]),CallExpr(Id(printf),[Id(z)]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_expression8(self):
        """ Test Expression Function """
        input = r"""
        void main(){
            int a;
            a = a + 1;
            print(a);
            a = a* 1;
            a = a / 1 && 1 || 1 % 1;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),CallExpr(Id(print),[Id(a)]),BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(1))),BinaryOp(=,Id(a),BinaryOp(||,BinaryOp(&&,BinaryOp(/,Id(a),IntLiteral(1)),IntLiteral(1)),BinaryOp(%,IntLiteral(1),IntLiteral(1))))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_expression9(self):
        """ Test Expression Function """
        input = r"""
        void main(){
            a = !(a && b || c);
            e = a / b *c / (10 * c % d);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),UnaryOp(!,BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)))),BinaryOp(=,Id(e),BinaryOp(/,BinaryOp(*,BinaryOp(/,Id(a),Id(b)),Id(c)),BinaryOp(%,BinaryOp(*,IntLiteral(10),Id(c)),Id(d))))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_expression10(self):
        """ Test Expression Function """
        input = r"""
           void main(){
               a = !(a && b || c);
               e = a / b *c / (10 * c % d) && !(1) || (1) / 2;
           }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),UnaryOp(!,BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),Id(c)))),BinaryOp(=,Id(e),BinaryOp(||,BinaryOp(&&,BinaryOp(/,BinaryOp(*,BinaryOp(/,Id(a),Id(b)),Id(c)),BinaryOp(%,BinaryOp(*,IntLiteral(10),Id(c)),Id(d))),UnaryOp(!,IntLiteral(1))),BinaryOp(/,IntLiteral(1),IntLiteral(2))))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_dowhile_stmt1(self):
        """ Test Do While Statement """
        input = r"""
           void main(){
               do a=a+1; while true;
           }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_dowhile_stmt2(self):
        """ Test Do While Statement """
        input = r"""
          void main(){
              do a=a+1; a=b; if (true) break; while true;
          }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(a),Id(b)),If(BooleanLiteral(true),Break())],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_dowhile_stmt3(self):
        """ Test Do While Statement"""
        input = r"""
          void main(){
              do{

              }while(a == b);
          }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([])],BinaryOp(==,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_dowhile_stmt4(self):
        """ Test Do While Statement """
        input = r"""
          void main(){
              do{
                  int a;
                  a = a + 1;
              }while(a <= 10);
          }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(<=,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_dowhile_stmt5(self):
        """ Test Do While Statement """
        input = r"""
          void main(){
              do{
                  int a;
                  a = a + 1;
                  if (a != 1)
                      break;
                  else
                      continue;
              }while(a <= 10);
          }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(!=,Id(a),IntLiteral(1)),Break(),Continue())])],BinaryOp(<=,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_dowhile_stmt6(self):
        """ Test Do While Statement """
        input = r"""
          void main(){
              do{
                  do{
                      a = a+1;
                      if (a == 5)
                          break; 
                  }while(true);
              }while(a <= 10);
          }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(==,Id(a),IntLiteral(5)),Break())])],BooleanLiteral(true))])],BinaryOp(<=,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_dowhile_stmt7(self):
        """ Test Do While Statement """
        input = r"""
        void main(){
            do{
                do{
                    a = a+1;
                    if (a == 5)
                        break; 
                    do 
                        a = a / 2;
                    while(a<1);
                }while(true || a !=5);
            }while(a <= 10);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(==,Id(a),IntLiteral(5)),Break()),Dowhile([BinaryOp(=,Id(a),BinaryOp(/,Id(a),IntLiteral(2)))],BinaryOp(<,Id(a),IntLiteral(1)))])],BinaryOp(||,BooleanLiteral(true),BinaryOp(!=,Id(a),IntLiteral(5))))])],BinaryOp(<=,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_dowhile_stmt8(self):
        """ Test Do While Statement """
        input = r"""
        void main(){
            do{
                do{
                    do 
                        a = a / 2;
                        do a = a * 2; while(a%2 == 0);
                    while(a<1);
                }while(true || a !=5);
            }while(a <= 10);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([Dowhile([Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(/,Id(a),IntLiteral(2))),Dowhile([BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)))],BinaryOp(==,BinaryOp(%,Id(a),IntLiteral(2)),IntLiteral(0)))],BinaryOp(<,Id(a),IntLiteral(1)))])],BinaryOp(||,BooleanLiteral(true),BinaryOp(!=,Id(a),IntLiteral(5))))])],BinaryOp(<=,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_dowhile_stmt9(self):
        """ Test Do While Statement """
        input = r"""
        void main(){
            do{
                do{
                    if (a)
                        return;
                }while(true || a !=5);
            }while(a <= 10);
            do continue; while 1;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([Dowhile([Block([If(Id(a),Return())])],BinaryOp(||,BooleanLiteral(true),BinaryOp(!=,Id(a),IntLiteral(5))))])],BinaryOp(<=,Id(a),IntLiteral(10))),Dowhile([Continue()],IntLiteral(1))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_dowhile_stmt10(self):
        """ Test Do While Statement """
        input = r"""
        void main(){
            do{

            }while(a <= 10);
            do{

            }while(a > 10);
            do a=a+1;a=a*2;b=c+1; while(c>0);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([])],BinaryOp(<=,Id(a),IntLiteral(10))),Dowhile([Block([])],BinaryOp(>,Id(a),IntLiteral(10))),Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2))),BinaryOp(=,Id(b),BinaryOp(+,Id(c),IntLiteral(1)))],BinaryOp(>,Id(c),IntLiteral(0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_simple_program1(self):
        """ Test Simple Program """
        input = r"""
        void print(){
            print(a);
        }
        int sum(int a, int b){
            return a + b;
        }
        """
        expect = "Program([FuncDecl(Id(print),[],VoidType,Block([CallExpr(Id(print),[Id(a)])])),FuncDecl(Id(sum),[VarDecl(a,IntType),VarDecl(b,IntType)],IntType,Block([Return(BinaryOp(+,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_simple_program2(self):
        """ Test Simple Program """
        input = r"""
        void print(int a){
            print(a);
        }
        int main(string args[]){
            int i;
            for (i=1;i<len(a);i=i+1)
                a[i] = i;
            for (i=1;i<len(a);i=i+1)
                print(a[i]);
        }
        """
        expect = "Program([FuncDecl(Id(print),[VarDecl(a,IntType)],VoidType,Block([CallExpr(Id(print),[Id(a)])])),FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],IntType,Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),CallExpr(Id(len),[Id(a)]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,ArrayCell(Id(a),Id(i)),Id(i))),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),CallExpr(Id(len),[Id(a)]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(print),[ArrayCell(Id(a),Id(i))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_simple_program3(self):
        """ Test Simple Program """
        input = r"""
        void print(int a){
            a = foo()[5];
            b = foo2(a[100])[10];
            if (a && b)
                print(a);
            else
                continue;
        }
        """
        expect = "Program([FuncDecl(Id(print),[VarDecl(a,IntType)],VoidType,Block([BinaryOp(=,Id(a),ArrayCell(CallExpr(Id(foo),[]),IntLiteral(5))),BinaryOp(=,Id(b),ArrayCell(CallExpr(Id(foo2),[ArrayCell(Id(a),IntLiteral(100))]),IntLiteral(10))),If(BinaryOp(&&,Id(a),Id(b)),CallExpr(Id(print),[Id(a)]),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_complex_program1(self):
        """ Test Complex Program """
        input = r"""
        int  main()
        {
            int i;
            i = 8;
            return 0;
        }
        int factorial( int i)
        {
            if(i < 2) 
            {
            return 1;
            }
            return i * factorial(i - 1);
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(8)),Return(IntLiteral(0))])),FuncDecl(Id(factorial),[VarDecl(i,IntType)],IntType,Block([If(BinaryOp(<,Id(i),IntLiteral(2)),Block([Return(IntLiteral(1))])),Return(BinaryOp(*,Id(i),CallExpr(Id(factorial),[BinaryOp(-,Id(i),IntLiteral(1))])))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_if_stmt8(self):
        """ Test If Statement """
        input = r"""void main(){
            int a;
            a = true;
            if (true){
                if (a == true){
                    if (!a){
                        a = false;
                        string b;
                        b = a;
                    }
                    else{
                        string b;
                        b = a;
                    }
                }
                else{
                    a = false;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a))]),Block([VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a))]))]),Block([BinaryOp(=,Id(a),BooleanLiteral(false))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_complex_program3(self):
        """ Test Complex Program """
        input = r"""
        void main(){
        int A, B, temp;

        printf("Please enter the 1st number : ");
        scanf("%d",A);
        printf("\nPlease enter the 2nd number : ");
        scanf("%d",B);

        printf("\nBefore swapping:\n");
        printf("A - %d \nB - %d", A, B);

        temp = A;
        A = B;
        B = temp;

        printf("\nAfter swapping:\n");
        printf("A - %d \nB - %d", A, B);

        return 0;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(A,IntType),VarDecl(B,IntType),VarDecl(temp,IntType),CallExpr(Id(printf),[StringLiteral(Please enter the 1st number : )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(A)]),CallExpr(Id(printf),[StringLiteral(\\nPlease enter the 2nd number : )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(B)]),CallExpr(Id(printf),[StringLiteral(\\nBefore swapping:\\n)]),CallExpr(Id(printf),[StringLiteral(A - %d \\nB - %d),Id(A),Id(B)]),BinaryOp(=,Id(temp),Id(A)),BinaryOp(=,Id(A),Id(B)),BinaryOp(=,Id(B),Id(temp)),CallExpr(Id(printf),[StringLiteral(\\nAfter swapping:\\n)]),CallExpr(Id(printf),[StringLiteral(A - %d \\nB - %d),Id(A),Id(B)]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_complex_program4(self):
        """ Test Complex Program """
        input = r"""
        int evaluatePostfix(string exp)  
{  
    // Create a stack of capacity equal to expression size  
    int stack;
    stack = createStack(strlen(exp));  
    int i;  

    // See if stack was created successfully  
    if (!stack) return -1;  

    // Scan all characters one by one  
    for (i = 0; exp[i]; i = i + 1)  
    {  
        //if the character is blank space then continue  
        if(exp[i] == " ")continue;  

        // If the scanned character is an  
        // operand (number here),extract the full number  
        // Push it to the stack.  
        if (isdigit(exp[i]))  
        {  
            int num;
            num=0;  

            //extract full number
            do{
                {  
                num = num * 10 + (exp[i] - 0);  
                i = i + 1;  
            } 
            } 
            while(isdigit(exp[i]));  
            i=i+1;  

            //push the element in the stack  
            push(stack,num);  
        }  

        // If the scanned character is an operator, pop two  
        // elements from stack apply the operator  
        else
        {  
            int val1;
            val1 = pop(stack);  
            int val2;
            val2 = pop(stack);  

            if (exp[i] == "+") {push(stack, val2 + val1); break;}
            if (exp[i] == "-") {push(stack, val2 - val1); break;  }
            if (exp[i] == "*") {push(stack, val2 * val1); break;  }
            if (exp[i] == "/") {push(stack, val2/val1); break;  }

        }  
    }  
    return pop(stack);  
}  
        """
        expect =  "Program([FuncDecl(Id(evaluatePostfix),[VarDecl(exp,StringType)],IntType,Block([VarDecl(stack,IntType),BinaryOp(=,Id(stack),CallExpr(Id(createStack),[CallExpr(Id(strlen),[Id(exp)])])),VarDecl(i,IntType),If(UnaryOp(!,Id(stack)),Return(UnaryOp(-,IntLiteral(1)))),For(BinaryOp(=,Id(i),IntLiteral(0));ArrayCell(Id(exp),Id(i));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,ArrayCell(Id(exp),Id(i)),StringLiteral( )),Continue()),If(CallExpr(Id(isdigit),[ArrayCell(Id(exp),Id(i))]),Block([VarDecl(num,IntType),BinaryOp(=,Id(num),IntLiteral(0)),Dowhile([Block([Block([BinaryOp(=,Id(num),BinaryOp(+,BinaryOp(*,Id(num),IntLiteral(10)),BinaryOp(-,ArrayCell(Id(exp),Id(i)),IntLiteral(0)))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])])],CallExpr(Id(isdigit),[ArrayCell(Id(exp),Id(i))])),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1))),CallExpr(Id(push),[Id(stack),Id(num)])]),Block([VarDecl(val1,IntType),BinaryOp(=,Id(val1),CallExpr(Id(pop),[Id(stack)])),VarDecl(val2,IntType),BinaryOp(=,Id(val2),CallExpr(Id(pop),[Id(stack)])),If(BinaryOp(==,ArrayCell(Id(exp),Id(i)),StringLiteral(+)),Block([CallExpr(Id(push),[Id(stack),BinaryOp(+,Id(val2),Id(val1))]),Break()])),If(BinaryOp(==,ArrayCell(Id(exp),Id(i)),StringLiteral(-)),Block([CallExpr(Id(push),[Id(stack),BinaryOp(-,Id(val2),Id(val1))]),Break()])),If(BinaryOp(==,ArrayCell(Id(exp),Id(i)),StringLiteral(*)),Block([CallExpr(Id(push),[Id(stack),BinaryOp(*,Id(val2),Id(val1))]),Break()])),If(BinaryOp(==,ArrayCell(Id(exp),Id(i)),StringLiteral(/)),Block([CallExpr(Id(push),[Id(stack),BinaryOp(/,Id(val2),Id(val1))]),Break()]))]))])),Return(CallExpr(Id(pop),[Id(stack)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))


    def test_complex_program5(self):
        """ Test Complex Program """
        input = r"""
                    int main()
            
            {
            
                float a, b, c;
            
                printf("\nPlease enter 3 numbers: ");
            
                scanf("%f %f %f", a, b, c);
            
                if(c<=a && c<=b)
            
                    printf("The smallest number is %.3f", c);
            
                return 0;
            
            }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(c,FloatType),CallExpr(Id(printf),[StringLiteral(\\nPlease enter 3 numbers: )]),CallExpr(Id(scanf),[StringLiteral(%f %f %f),Id(a),Id(b),Id(c)]),If(BinaryOp(&&,BinaryOp(<=,Id(c),Id(a)),BinaryOp(<=,Id(c),Id(b))),CallExpr(Id(printf),[StringLiteral(The smallest number is %.3f),Id(c)])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_complex_program6(self):
        """ Test Complex Program """
        input = r"""
        int  main()
        {
            int A, B, temp;

            temp = A;
            A = B;
            B = temp;
            
            printf("\nAfter swapping:\n");
            printf("A - %d \nB - %d", A, B);
 
            return 0;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(A,IntType),VarDecl(B,IntType),VarDecl(temp,IntType),BinaryOp(=,Id(temp),Id(A)),BinaryOp(=,Id(A),Id(B)),BinaryOp(=,Id(B),Id(temp)),CallExpr(Id(printf),[StringLiteral(\\nAfter swapping:\\n)]),CallExpr(Id(printf),[StringLiteral(A - %d \\nB - %d),Id(A),Id(B)]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_complex_program7(self):
        """ Test Complex Program """
        input = r"""
        int  main()
        {
            int n, sum , d;
            scanf("%d",n);
            do
            {
                rem = n % 10;
                sum = sum + rem;
                n = n / 100;
            }while(n != 0);

            return 0;
        }
        """
        expect =  "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(n,IntType),VarDecl(sum,IntType),VarDecl(d,IntType),CallExpr(Id(scanf),[StringLiteral(%d),Id(n)]),Dowhile([Block([BinaryOp(=,Id(rem),BinaryOp(%,Id(n),IntLiteral(10))),BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),Id(rem))),BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(100)))])],BinaryOp(!=,Id(n),IntLiteral(0))),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_complex_program8(self):
        """ Test Complex Program """
        input = r"""
        int  main()
        {
            int base, exponent;
            int result;
            result = 1;
            printf("Enter a base number: ");
            scanf("%d", base);
            printf("Enter an exponent: ");
            scanf("%d", exponent);
            do
            {
                result = result * base;
                exponent = exponent - 1;
            }while (exponent != 0);
            printf("Answer = %lld", result);
            return 0;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(base,IntType),VarDecl(exponent,IntType),VarDecl(result,IntType),BinaryOp(=,Id(result),IntLiteral(1)),CallExpr(Id(printf),[StringLiteral(Enter a base number: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(base)]),CallExpr(Id(printf),[StringLiteral(Enter an exponent: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(exponent)]),Dowhile([Block([BinaryOp(=,Id(result),BinaryOp(*,Id(result),Id(base))),BinaryOp(=,Id(exponent),BinaryOp(-,Id(exponent),IntLiteral(1)))])],BinaryOp(!=,Id(exponent),IntLiteral(0))),CallExpr(Id(printf),[StringLiteral(Answer = %lld),Id(result)]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_collection1(self):
        input = """int main() { a; }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([Id("a")]))]))
        #expect =    "Program([FuncDecl(Id(main),[],IntType,Block([Id(a)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_collection2(self):
        input = """int main(){
            n = ((((((n))/2))));
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_non_body_func_decl8(self):
        input = r"""int main(int a, float b[], string c[], boolean d){}
        float main(){}
        boolean[] main(int a[]){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(c,ArrayTypePointer(StringType)),VarDecl(d,BoolType)],IntType,Block([])),FuncDecl(Id(main),[],FloatType,Block([])),FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType))],ArrayTypePointer(BoolType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,393))
    
    def test_non_body_func_decl9(self):
        input = r"""int foo(int a, int b){}
        int[] main(){}
        float[] main(string args[]){}
        string[] int2str(int a){}
        boolean isTrue(boolean a){}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,IntType)],IntType,Block([])),FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],ArrayTypePointer(FloatType),Block([])),FuncDecl(Id(int2str),[VarDecl(a,IntType)],ArrayTypePointer(StringType),Block([])),FuncDecl(Id(isTrue),[VarDecl(a,BoolType)],BoolType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,394))


    def test_non_body_func_decl10(self):
        """ Test Non Body Function Declare """
        input = r"""int main(string args[]){}
        int[] __str__(string a, string exception, boolean b[], float a){}
        boolean[] __abc(boolean isTrue){}
        float pi(float pi){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],IntType,Block([])),FuncDecl(Id(__str__),[VarDecl(a,StringType),VarDecl(exception,StringType),VarDecl(b,ArrayTypePointer(BoolType)),VarDecl(a,FloatType)],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(__abc),[VarDecl(isTrue,BoolType)],ArrayTypePointer(BoolType),Block([])),FuncDecl(Id(pi),[VarDecl(pi,FloatType)],FloatType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_func_decl_body_vardecl1(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int main(){
        int a;
        float c;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(c,FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_func_decl_body_vardecl2(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int[] main(float b[], string a){
        int a[10];
        string c;
        boolean a[1000];
        float a;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(a,StringType)],ArrayTypePointer(IntType),Block([VarDecl(a,ArrayType(IntType,IntLiteral(10))),VarDecl(c,StringType),VarDecl(a,ArrayType(BoolType,IntLiteral(1000))),VarDecl(a,FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,397))


    def test_func_decl_body_vardecl3(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int main(){
            float a;
            string a;
            boolean b;
            int b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),VarDecl(a,StringType),VarDecl(b,BoolType),VarDecl(b,IntType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_func_decl_body_vardecl4(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int[] main(float b[], string a){
            int a[5];
            float b[10];
            string c[15];
            boolean d[20];
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(a,StringType)],ArrayTypePointer(IntType),Block([VarDecl(a,ArrayType(IntType,IntLiteral(5))),VarDecl(b,ArrayType(FloatType,IntLiteral(10))),VarDecl(c,ArrayType(StringType,IntLiteral(15))),VarDecl(d,ArrayType(BoolType,IntLiteral(20)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_func_decl_body_vardecl5(self):
        """ Test Function Declare With Body Contains Variable Declare"""
        input = r"""int[] main(float b[], string a){
            int a, a[5];
            float c, d, e[10], f[15]; int a,b,c;
            string a,b,c; string a[20];
            boolean a; float b; boolean a;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,ArrayTypePointer(FloatType)),VarDecl(a,StringType)],ArrayTypePointer(IntType),Block([VarDecl(a,IntType),VarDecl(a,ArrayType(IntType,IntLiteral(5))),VarDecl(c,FloatType),VarDecl(d,FloatType),VarDecl(e,ArrayType(FloatType,IntLiteral(10))),VarDecl(f,ArrayType(FloatType,IntLiteral(15))),VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,IntType),VarDecl(a,StringType),VarDecl(b,StringType),VarDecl(c,StringType),VarDecl(a,ArrayType(StringType,IntLiteral(20))),VarDecl(a,BoolType),VarDecl(b,FloatType),VarDecl(a,BoolType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,400))

    def test_if_stmt1(self):
        """ Test If Statement """
        input = r"""void main(){
            if (true)
                a = a + 1;
            else
                a = b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([If(BooleanLiteral(true),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,401))