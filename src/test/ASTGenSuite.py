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