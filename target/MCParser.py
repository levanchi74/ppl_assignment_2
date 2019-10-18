# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u0130\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\6\2F\n\2\r\2\16\2G")
        buf.write("\3\2\3\2\3\3\3\3\5\3N\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\7\5W\n\5\f\5\16\5Z\13\5\3\6\3\6\3\6\3\6\5\6`\n\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\5\bh\n\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\5\tp\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13y\n\13\f")
        buf.write("\13\16\13|\13\13\3\f\3\f\3\f\3\f\5\f\u0082\n\f\3\r\3\r")
        buf.write("\7\r\u0086\n\r\f\r\16\r\u0089\13\r\3\r\3\r\3\16\3\16\5")
        buf.write("\16\u008f\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u0099\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5")
        buf.write("\20\u00a2\n\20\3\21\3\21\6\21\u00a6\n\21\r\21\16\21\u00a7")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25")
        buf.write("\5\25\u00c0\n\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u00cc\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u00d4\n\30\f\30\16\30\u00d7\13\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\7\31\u00df\n\31\f\31\16\31\u00e2")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\32\5\32\u00e9\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u00f0\n\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\7\34\u00f8\n\34\f\34\16\34\u00fb\13\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\7\35\u0103\n\35\f\35\16\35\u0106")
        buf.write("\13\35\3\36\3\36\3\36\5\36\u010b\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\5\37\u0115\n\37\3 \3 \3 \5 \u011a")
        buf.write("\n \3 \3 \3 \3 \3!\3!\3!\3!\3!\7!\u0125\n!\f!\16!\u0128")
        buf.write("\13!\5!\u012a\n!\3!\3!\3\"\3\"\3\"\2\6.\60\668#\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@B\2\7\4\2\23\23\25\27\3\2\36\37\3\2 \"\4\2\37\37")
        buf.write("##\3\2\3\6\2\u0133\2E\3\2\2\2\4M\3\2\2\2\6O\3\2\2\2\b")
        buf.write("S\3\2\2\2\n[\3\2\2\2\fa\3\2\2\2\16c\3\2\2\2\20o\3\2\2")
        buf.write("\2\22q\3\2\2\2\24u\3\2\2\2\26}\3\2\2\2\30\u0083\3\2\2")
        buf.write("\2\32\u008e\3\2\2\2\34\u0098\3\2\2\2\36\u009a\3\2\2\2")
        buf.write(" \u00a3\3\2\2\2\"\u00ad\3\2\2\2$\u00b7\3\2\2\2&\u00ba")
        buf.write("\3\2\2\2(\u00bd\3\2\2\2*\u00c3\3\2\2\2,\u00cb\3\2\2\2")
        buf.write(".\u00cd\3\2\2\2\60\u00d8\3\2\2\2\62\u00e8\3\2\2\2\64\u00ef")
        buf.write("\3\2\2\2\66\u00f1\3\2\2\28\u00fc\3\2\2\2:\u010a\3\2\2")
        buf.write("\2<\u0114\3\2\2\2>\u0119\3\2\2\2@\u011f\3\2\2\2B\u012d")
        buf.write("\3\2\2\2DF\5\4\3\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2")
        buf.write("\2\2HI\3\2\2\2IJ\7\2\2\3J\3\3\2\2\2KN\5\6\4\2LN\5\16\b")
        buf.write("\2MK\3\2\2\2ML\3\2\2\2N\5\3\2\2\2OP\5\f\7\2PQ\5\b\5\2")
        buf.write("QR\7*\2\2R\7\3\2\2\2SX\5\n\6\2TU\7,\2\2UW\5\n\6\2VT\3")
        buf.write("\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y\t\3\2\2\2ZX\3\2")
        buf.write("\2\2[_\7\30\2\2\\]\7(\2\2]^\7\3\2\2^`\7)\2\2_\\\3\2\2")
        buf.write("\2_`\3\2\2\2`\13\3\2\2\2ab\t\2\2\2b\r\3\2\2\2cd\5\20\t")
        buf.write("\2de\7\30\2\2eg\7$\2\2fh\5\24\13\2gf\3\2\2\2gh\3\2\2\2")
        buf.write("hi\3\2\2\2ij\7%\2\2jk\5\30\r\2k\17\3\2\2\2lp\5\f\7\2m")
        buf.write("p\7\24\2\2np\5\22\n\2ol\3\2\2\2om\3\2\2\2on\3\2\2\2p\21")
        buf.write("\3\2\2\2qr\5\f\7\2rs\7(\2\2st\7)\2\2t\23\3\2\2\2uz\5\26")
        buf.write("\f\2vw\7,\2\2wy\5\26\f\2xv\3\2\2\2y|\3\2\2\2zx\3\2\2\2")
        buf.write("z{\3\2\2\2{\25\3\2\2\2|z\3\2\2\2}~\5\f\7\2~\u0081\7\30")
        buf.write("\2\2\177\u0080\7(\2\2\u0080\u0082\7)\2\2\u0081\177\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0082\27\3\2\2\2\u0083\u0087")
        buf.write("\7&\2\2\u0084\u0086\5\32\16\2\u0085\u0084\3\2\2\2\u0086")
        buf.write("\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u008a\3\2\2\2\u0089\u0087\3\2\2\2\u008a\u008b\7")
        buf.write("\'\2\2\u008b\31\3\2\2\2\u008c\u008f\5\6\4\2\u008d\u008f")
        buf.write("\5\34\17\2\u008e\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f")
        buf.write("\33\3\2\2\2\u0090\u0099\5\36\20\2\u0091\u0099\5 \21\2")
        buf.write("\u0092\u0099\5\"\22\2\u0093\u0099\5$\23\2\u0094\u0099")
        buf.write("\5&\24\2\u0095\u0099\5(\25\2\u0096\u0099\5*\26\2\u0097")
        buf.write("\u0099\5\30\r\2\u0098\u0090\3\2\2\2\u0098\u0091\3\2\2")
        buf.write("\2\u0098\u0092\3\2\2\2\u0098\u0093\3\2\2\2\u0098\u0094")
        buf.write("\3\2\2\2\u0098\u0095\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\35\3\2\2\2\u009a\u009b\7\r\2\2\u009b")
        buf.write("\u009c\7$\2\2\u009c\u009d\5,\27\2\u009d\u009e\7%\2\2\u009e")
        buf.write("\u00a1\5\34\17\2\u009f\u00a0\7\13\2\2\u00a0\u00a2\5\34")
        buf.write("\17\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\37")
        buf.write("\3\2\2\2\u00a3\u00a5\7\17\2\2\u00a4\u00a6\5\34\17\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\7")
        buf.write("\20\2\2\u00aa\u00ab\5,\27\2\u00ab\u00ac\7*\2\2\u00ac!")
        buf.write("\3\2\2\2\u00ad\u00ae\7\f\2\2\u00ae\u00af\7$\2\2\u00af")
        buf.write("\u00b0\5,\27\2\u00b0\u00b1\7*\2\2\u00b1\u00b2\5,\27\2")
        buf.write("\u00b2\u00b3\7*\2\2\u00b3\u00b4\5,\27\2\u00b4\u00b5\7")
        buf.write("%\2\2\u00b5\u00b6\5\34\17\2\u00b6#\3\2\2\2\u00b7\u00b8")
        buf.write("\7\t\2\2\u00b8\u00b9\7*\2\2\u00b9%\3\2\2\2\u00ba\u00bb")
        buf.write("\7\n\2\2\u00bb\u00bc\7*\2\2\u00bc\'\3\2\2\2\u00bd\u00bf")
        buf.write("\7\16\2\2\u00be\u00c0\5,\27\2\u00bf\u00be\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\7*\2\2")
        buf.write("\u00c2)\3\2\2\2\u00c3\u00c4\5,\27\2\u00c4\u00c5\7*\2\2")
        buf.write("\u00c5+\3\2\2\2\u00c6\u00c7\5.\30\2\u00c7\u00c8\7\31\2")
        buf.write("\2\u00c8\u00c9\5,\27\2\u00c9\u00cc\3\2\2\2\u00ca\u00cc")
        buf.write("\5.\30\2\u00cb\u00c6\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("-\3\2\2\2\u00cd\u00ce\b\30\1\2\u00ce\u00cf\5\60\31\2\u00cf")
        buf.write("\u00d5\3\2\2\2\u00d0\u00d1\f\4\2\2\u00d1\u00d2\7\32\2")
        buf.write("\2\u00d2\u00d4\5\60\31\2\u00d3\u00d0\3\2\2\2\u00d4\u00d7")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("/\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\b\31\1\2\u00d9")
        buf.write("\u00da\5\62\32\2\u00da\u00e0\3\2\2\2\u00db\u00dc\f\4\2")
        buf.write("\2\u00dc\u00dd\7\33\2\2\u00dd\u00df\5\62\32\2\u00de\u00db")
        buf.write("\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\61\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3")
        buf.write("\u00e4\5\64\33\2\u00e4\u00e5\7\34\2\2\u00e5\u00e6\5\64")
        buf.write("\33\2\u00e6\u00e9\3\2\2\2\u00e7\u00e9\5\64\33\2\u00e8")
        buf.write("\u00e3\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\63\3\2\2\2\u00ea")
        buf.write("\u00eb\5\66\34\2\u00eb\u00ec\7\35\2\2\u00ec\u00ed\5\66")
        buf.write("\34\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\5\66\34\2\u00ef")
        buf.write("\u00ea\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0\65\3\2\2\2\u00f1")
        buf.write("\u00f2\b\34\1\2\u00f2\u00f3\58\35\2\u00f3\u00f9\3\2\2")
        buf.write("\2\u00f4\u00f5\f\4\2\2\u00f5\u00f6\t\3\2\2\u00f6\u00f8")
        buf.write("\58\35\2\u00f7\u00f4\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\67\3\2\2\2\u00fb")
        buf.write("\u00f9\3\2\2\2\u00fc\u00fd\b\35\1\2\u00fd\u00fe\5:\36")
        buf.write("\2\u00fe\u0104\3\2\2\2\u00ff\u0100\f\4\2\2\u0100\u0101")
        buf.write("\t\4\2\2\u0101\u0103\5:\36\2\u0102\u00ff\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u01059\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\t\5\2")
        buf.write("\2\u0108\u010b\5:\36\2\u0109\u010b\5<\37\2\u010a\u0107")
        buf.write("\3\2\2\2\u010a\u0109\3\2\2\2\u010b;\3\2\2\2\u010c\u010d")
        buf.write("\7$\2\2\u010d\u010e\5,\27\2\u010e\u010f\7%\2\2\u010f\u0115")
        buf.write("\3\2\2\2\u0110\u0115\5B\"\2\u0111\u0115\7\30\2\2\u0112")
        buf.write("\u0115\5@!\2\u0113\u0115\5> \2\u0114\u010c\3\2\2\2\u0114")
        buf.write("\u0110\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3\2\2\2")
        buf.write("\u0114\u0113\3\2\2\2\u0115=\3\2\2\2\u0116\u011a\7\30\2")
        buf.write("\2\u0117\u011a\5@!\2\u0118\u011a\5B\"\2\u0119\u0116\3")
        buf.write("\2\2\2\u0119\u0117\3\2\2\2\u0119\u0118\3\2\2\2\u011a\u011b")
        buf.write("\3\2\2\2\u011b\u011c\7(\2\2\u011c\u011d\5,\27\2\u011d")
        buf.write("\u011e\7)\2\2\u011e?\3\2\2\2\u011f\u0120\7\30\2\2\u0120")
        buf.write("\u0129\7$\2\2\u0121\u0126\5,\27\2\u0122\u0123\7,\2\2\u0123")
        buf.write("\u0125\5,\27\2\u0124\u0122\3\2\2\2\u0125\u0128\3\2\2\2")
        buf.write("\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u012a\3")
        buf.write("\2\2\2\u0128\u0126\3\2\2\2\u0129\u0121\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7%\2\2\u012c")
        buf.write("A\3\2\2\2\u012d\u012e\t\6\2\2\u012eC\3\2\2\2\34GMX_go")
        buf.write("z\u0081\u0087\u008e\u0098\u00a1\u00a7\u00bf\u00cb\u00d5")
        buf.write("\u00e0\u00e8\u00ef\u00f9\u0104\u010a\u0114\u0119\u0126")
        buf.write("\u0129")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'break'", "'continue'", 
                     "'else'", "'for'", "'if'", "'return'", "'do'", "'while'", 
                     "'true'", "'false'", "'boolean'", "'void'", "'int'", 
                     "'float'", "'string'", "<INVALID>", "'='", "'||'", 
                     "'&&'", "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", 
                      "ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", "TRUE", 
                      "FALSE", "BOOLEANTYPE", "VOIDTYPE", "INTTYPE", "FLOATTYPE", 
                      "STRINGTYPE", "ID", "ASSIGN", "OROP", "ANDOP", "EQUALOP", 
                      "COMPOP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                      "NEGOP", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", 
                      "COLON", "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_varlist = 3
    RULE_var = 4
    RULE_primtype = 5
    RULE_funcdecl = 6
    RULE_returntype = 7
    RULE_arrptrtype = 8
    RULE_paralist = 9
    RULE_para = 10
    RULE_blockstmt = 11
    RULE_vardecl_stmt = 12
    RULE_stmt = 13
    RULE_ifstmt = 14
    RULE_dowhilestmt = 15
    RULE_forstmt = 16
    RULE_breakstmt = 17
    RULE_contistmt = 18
    RULE_returnstmt = 19
    RULE_expstmt = 20
    RULE_exp = 21
    RULE_exp1 = 22
    RULE_exp2 = 23
    RULE_exp3 = 24
    RULE_exp4 = 25
    RULE_exp5 = 26
    RULE_exp6 = 27
    RULE_exp7 = 28
    RULE_exp8 = 29
    RULE_elearray = 30
    RULE_funcall = 31
    RULE_literal = 32

    ruleNames =  [ "program", "decl", "vardecl", "varlist", "var", "primtype", 
                   "funcdecl", "returntype", "arrptrtype", "paralist", "para", 
                   "blockstmt", "vardecl_stmt", "stmt", "ifstmt", "dowhilestmt", 
                   "forstmt", "breakstmt", "contistmt", "returnstmt", "expstmt", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "elearray", "funcall", "literal" ]

    EOF = Token.EOF
    INTLIT=1
    FLOATLIT=2
    BOOLEANLIT=3
    STRINGLIT=4
    BLOCK_COMMENT=5
    LINE_COMMENT=6
    BREAK=7
    CONTINUE=8
    ELSE=9
    FOR=10
    IF=11
    RETURN=12
    DO=13
    WHILE=14
    TRUE=15
    FALSE=16
    BOOLEANTYPE=17
    VOIDTYPE=18
    INTTYPE=19
    FLOATTYPE=20
    STRINGTYPE=21
    ID=22
    ASSIGN=23
    OROP=24
    ANDOP=25
    EQUALOP=26
    COMPOP=27
    ADDOP=28
    SUBOP=29
    MULOP=30
    DIVOP=31
    MODOP=32
    NEGOP=33
    LB=34
    RB=35
    LP=36
    RP=37
    LS=38
    RS=39
    SEMI=40
    COLON=41
    COMMA=42
    WS=43
    ERROR_CHAR=44
    UNCLOSE_STRING=45
    ILLEGAL_ESCAPE=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.decl()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLEANTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
                    break

            self.state = 71
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MCParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MCParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def varlist(self):
            return self.getTypedRuleContext(MCParser.VarlistContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.primtype()
            self.state = 78
            self.varlist()
            self.state = 79
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_varlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = MCParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.var()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 82
                self.match(MCParser.COMMA)
                self.state = 83
                self.var()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(MCParser.ID)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 90
                self.match(MCParser.LS)
                self.state = 91
                self.match(MCParser.INTLIT)
                self.state = 92
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEANTYPE(self):
            return self.getToken(MCParser.BOOLEANTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimtype" ):
                return visitor.visitPrimtype(self)
            else:
                return visitor.visitChildren(self)




    def primtype(self):

        localctx = MCParser.PrimtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLEANTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0)):
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


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returntype(self):
            return self.getTypedRuleContext(MCParser.ReturntypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MCParser.BlockstmtContext,0)


        def paralist(self):
            return self.getTypedRuleContext(MCParser.ParalistContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.returntype()
            self.state = 98
            self.match(MCParser.ID)
            self.state = 99
            self.match(MCParser.LB)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLEANTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE))) != 0):
                self.state = 100
                self.paralist()


            self.state = 103
            self.match(MCParser.RB)
            self.state = 104
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturntypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def arrptrtype(self):
            return self.getTypedRuleContext(MCParser.ArrptrtypeContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_returntype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturntype" ):
                return visitor.visitReturntype(self)
            else:
                return visitor.visitChildren(self)




    def returntype(self):

        localctx = MCParser.ReturntypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returntype)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.arrptrtype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrptrtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arrptrtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrptrtype" ):
                return visitor.visitArrptrtype(self)
            else:
                return visitor.visitChildren(self)




    def arrptrtype(self):

        localctx = MCParser.ArrptrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrptrtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.primtype()
            self.state = 112
            self.match(MCParser.LS)
            self.state = 113
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ParaContext)
            else:
                return self.getTypedRuleContext(MCParser.ParaContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = MCParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.para()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 116
                self.match(MCParser.COMMA)
                self.state = 117
                self.para()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MCParser.PrimtypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def getRuleIndex(self):
            return MCParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MCParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.primtype()
            self.state = 124
            self.match(MCParser.ID)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LS:
                self.state = 125
                self.match(MCParser.LS)
                self.state = 126
                self.match(MCParser.RS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def vardecl_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Vardecl_stmtContext)
            else:
                return self.getTypedRuleContext(MCParser.Vardecl_stmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MCParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MCParser.LP)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.BOOLEANTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.ID) | (1 << MCParser.SUBOP) | (1 << MCParser.NEGOP) | (1 << MCParser.LB) | (1 << MCParser.LP))) != 0):
                self.state = 130
                self.vardecl_stmt()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_vardecl_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl_stmt" ):
                return visitor.visitVardecl_stmt(self)
            else:
                return visitor.visitChildren(self)




    def vardecl_stmt(self):

        localctx = MCParser.Vardecl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vardecl_stmt)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.BOOLEANTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRINGTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.vardecl()
                pass
            elif token in [MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLEANLIT, MCParser.STRINGLIT, MCParser.BREAK, MCParser.CONTINUE, MCParser.FOR, MCParser.IF, MCParser.RETURN, MCParser.DO, MCParser.ID, MCParser.SUBOP, MCParser.NEGOP, MCParser.LB, MCParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.stmt()
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


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstmt(self):
            return self.getTypedRuleContext(MCParser.IfstmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MCParser.DowhilestmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MCParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MCParser.BreakstmtContext,0)


        def contistmt(self):
            return self.getTypedRuleContext(MCParser.ContistmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MCParser.ReturnstmtContext,0)


        def expstmt(self):
            return self.getTypedRuleContext(MCParser.ExpstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MCParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.ifstmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.dowhilestmt()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.forstmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 145
                self.breakstmt()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 146
                self.contistmt()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 147
                self.returnstmt()
                pass
            elif token in [MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLEANLIT, MCParser.STRINGLIT, MCParser.ID, MCParser.SUBOP, MCParser.NEGOP, MCParser.LB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 148
                self.expstmt()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 149
                self.blockstmt()
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


    class IfstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MCParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MCParser.IF)
            self.state = 153
            self.match(MCParser.LB)
            self.state = 154
            self.exp()
            self.state = 155
            self.match(MCParser.RB)
            self.state = 156
            self.stmt()
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 157
                self.match(MCParser.ELSE)
                self.state = 158
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_dowhilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MCParser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dowhilestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MCParser.DO)
            self.state = 163 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 162
                self.stmt()
                self.state = 165 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.ID) | (1 << MCParser.SUBOP) | (1 << MCParser.NEGOP) | (1 << MCParser.LB) | (1 << MCParser.LP))) != 0)):
                    break

            self.state = 167
            self.match(MCParser.WHILE)
            self.state = 168
            self.exp()
            self.state = 169
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MCParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(MCParser.FOR)
            self.state = 172
            self.match(MCParser.LB)
            self.state = 173
            self.exp()
            self.state = 174
            self.match(MCParser.SEMI)
            self.state = 175
            self.exp()
            self.state = 176
            self.match(MCParser.SEMI)
            self.state = 177
            self.exp()
            self.state = 178
            self.match(MCParser.RB)
            self.state = 179
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MCParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MCParser.BREAK)
            self.state = 182
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContistmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_contistmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContistmt" ):
                return visitor.visitContistmt(self)
            else:
                return visitor.visitChildren(self)




    def contistmt(self):

        localctx = MCParser.ContistmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_contistmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MCParser.CONTINUE)
            self.state = 185
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MCParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MCParser.RETURN)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID) | (1 << MCParser.SUBOP) | (1 << MCParser.NEGOP) | (1 << MCParser.LB))) != 0):
                self.state = 188
                self.exp()


            self.state = 191
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpstmt" ):
                return visitor.visitExpstmt(self)
            else:
                return visitor.visitChildren(self)




    def expstmt(self):

        localctx = MCParser.ExpstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.exp()
            self.state = 194
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp)
        try:
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.exp1(0)
                self.state = 197
                self.match(MCParser.ASSIGN)
                self.state = 198
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def OROP(self):
            return self.getToken(MCParser.OROP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 206
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 207
                    self.match(MCParser.OROP)
                    self.state = 208
                    self.exp2(0) 
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(MCParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def ANDOP(self):
            return self.getToken(MCParser.ANDOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 217
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 218
                    self.match(MCParser.ANDOP)
                    self.state = 219
                    self.exp3() 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp4Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp4Context,i)


        def EQUALOP(self):
            return self.getToken(MCParser.EQUALOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = MCParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp3)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.exp4()
                self.state = 226
                self.match(MCParser.EQUALOP)
                self.state = 227
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp5Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp5Context,i)


        def COMPOP(self):
            return self.getToken(MCParser.COMPOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = MCParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp4)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.exp5(0)
                self.state = 233
                self.match(MCParser.COMPOP)
                self.state = 234
                self.exp5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.exp5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(MCParser.Exp5Context,0)


        def ADDOP(self):
            return self.getToken(MCParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MCParser.SUBOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADDOP or _la==MCParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.exp6(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def MULOP(self):
            return self.getToken(MCParser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(MCParser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(MCParser.MODOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MULOP) | (1 << MCParser.DIVOP) | (1 << MCParser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.exp7() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def SUBOP(self):
            return self.getToken(MCParser.SUBOP, 0)

        def NEGOP(self):
            return self.getToken(MCParser.NEGOP, 0)

        def exp8(self):
            return self.getTypedRuleContext(MCParser.Exp8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = MCParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUBOP, MCParser.NEGOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                _la = self._input.LA(1)
                if not(_la==MCParser.SUBOP or _la==MCParser.NEGOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                self.exp7()
                pass
            elif token in [MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLEANLIT, MCParser.STRINGLIT, MCParser.ID, MCParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.exp8()
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


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def literal(self):
            return self.getTypedRuleContext(MCParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def elearray(self):
            return self.getTypedRuleContext(MCParser.ElearrayContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = MCParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp8)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(MCParser.LB)
                self.state = 267
                self.exp()
                self.state = 268
                self.match(MCParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.match(MCParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.funcall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
                self.elearray()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElearrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(MCParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RS(self):
            return self.getToken(MCParser.RS, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def literal(self):
            return self.getTypedRuleContext(MCParser.LiteralContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_elearray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElearray" ):
                return visitor.visitElearray(self)
            else:
                return visitor.visitChildren(self)




    def elearray(self):

        localctx = MCParser.ElearrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elearray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 276
                self.match(MCParser.ID)
                pass

            elif la_ == 2:
                self.state = 277
                self.funcall()
                pass

            elif la_ == 3:
                self.state = 278
                self.literal()
                pass


            self.state = 281
            self.match(MCParser.LS)
            self.state = 282
            self.exp()
            self.state = 283
            self.match(MCParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MCParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(MCParser.ID)
            self.state = 286
            self.match(MCParser.LB)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ID) | (1 << MCParser.SUBOP) | (1 << MCParser.NEGOP) | (1 << MCParser.LB))) != 0):
                self.state = 287
                self.exp()
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 288
                    self.match(MCParser.COMMA)
                    self.state = 289
                    self.exp()
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 297
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def BOOLEANLIT(self):
            return self.getToken(MCParser.BOOLEANLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLEANLIT) | (1 << MCParser.STRINGLIT))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.exp1_sempred
        self._predicates[23] = self.exp2_sempred
        self._predicates[26] = self.exp5_sempred
        self._predicates[27] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




