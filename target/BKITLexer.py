# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2O")
        buf.write("\u0301\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\7\13\u0128\n\13\f\13\16\13\u012b\13\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01c4\n!\3\"\3\"")
        buf.write("\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\38\38\38\38\39\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3C\3C\5C\u021e\nC\3D\3")
        buf.write("D\7D\u0222\nD\fD\16D\u0225\13D\3E\3E\3E\3E\3E\7E\u022c")
        buf.write("\nE\fE\16E\u022f\13E\3E\3E\3E\3E\3E\7E\u0236\nE\fE\16")
        buf.write("E\u0239\13E\5E\u023b\nE\3F\3F\3F\3F\3F\7F\u0242\nF\fF")
        buf.write("\16F\u0245\13F\3F\3F\3F\3F\3F\7F\u024c\nF\fF\16F\u024f")
        buf.write("\13F\5F\u0251\nF\3G\3G\5G\u0255\nG\3G\6G\u0258\nG\rG\16")
        buf.write("G\u0259\3H\6H\u025d\nH\rH\16H\u025e\3H\3H\6H\u0263\nH")
        buf.write("\rH\16H\u0264\3H\3H\7H\u0269\nH\fH\16H\u026c\13H\3H\5")
        buf.write("H\u026f\nH\3H\7H\u0272\nH\fH\16H\u0275\13H\3H\3H\6H\u0279")
        buf.write("\nH\rH\16H\u027a\3H\5H\u027e\nH\5H\u0280\nH\3I\3I\5I\u0284")
        buf.write("\nI\3J\3J\3J\3J\3J\3J\5J\u028c\nJ\3K\3K\5K\u0290\nK\3")
        buf.write("L\3L\3L\7L\u0295\nL\fL\16L\u0298\13L\3L\3L\3L\3M\3M\3")
        buf.write("M\3M\3M\3M\5M\u02a3\nM\3N\3N\7N\u02a7\nN\fN\16N\u02aa")
        buf.write("\13N\3N\3N\7N\u02ae\nN\fN\16N\u02b1\13N\3N\3N\7N\u02b5")
        buf.write("\nN\fN\16N\u02b8\13N\3N\7N\u02bb\nN\fN\16N\u02be\13N\3")
        buf.write("N\7N\u02c1\nN\fN\16N\u02c4\13N\3N\3N\3N\3O\3O\7O\u02cb")
        buf.write("\nO\fO\16O\u02ce\13O\3O\3O\3P\3P\7P\u02d4\nP\fP\16P\u02d7")
        buf.write("\13P\3P\3P\3P\3P\3P\3Q\3Q\3R\6R\u02e1\nR\rR\16R\u02e2")
        buf.write("\3R\3R\3S\3S\3S\3S\7S\u02eb\nS\fS\16S\u02ee\13S\3S\3S")
        buf.write("\3S\3S\3S\3T\3T\3T\3T\3T\3T\7T\u02fb\nT\fT\16T\u02fe\13")
        buf.write("T\3U\3U\3\u02ec\2V\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085")
        buf.write("D\u0087\2\u0089\2\u008b\2\u008d\2\u008fE\u0091F\u0093")
        buf.write("\2\u0095\2\u0097G\u0099\2\u009bH\u009dI\u009fJ\u00a1K")
        buf.write("\u00a3L\u00a5M\u00a7N\u00a9O\3\2\21\3\2c|\6\2\62;C\\a")
        buf.write("ac|\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\62")
        buf.write("9\4\2GGgg\n\2$$))^^ddhhppttvv\5\2\f\f$$^^\7\2\f\f\17\17")
        buf.write("$$))^^\t\2))^^ddhhppttvv\5\2\13\f\17\17\"\"\3\2,,\2\u0339")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\3\u00ab\3\2\2\2\5\u00b1")
        buf.write("\3\2\2\2\7\u00be\3\2\2\2\t\u00cb\3\2\2\2\13\u00d9\3\2")
        buf.write("\2\2\r\u00e7\3\2\2\2\17\u00f7\3\2\2\2\21\u0107\3\2\2\2")
        buf.write("\23\u0116\3\2\2\2\25\u0125\3\2\2\2\27\u012c\3\2\2\2\31")
        buf.write("\u0131\3\2\2\2\33\u0136\3\2\2\2\35\u013d\3\2\2\2\37\u0140")
        buf.write("\3\2\2\2!\u0144\3\2\2\2#\u014a\3\2\2\2%\u0150\3\2\2\2")
        buf.write("\'\u0157\3\2\2\2)\u0160\3\2\2\2+\u016a\3\2\2\2-\u0170")
        buf.write("\3\2\2\2/\u0179\3\2\2\2\61\u0181\3\2\2\2\63\u0185\3\2")
        buf.write("\2\2\65\u018c\3\2\2\2\67\u0191\3\2\2\29\u0194\3\2\2\2")
        buf.write(";\u019a\3\2\2\2=\u01a3\3\2\2\2?\u01a8\3\2\2\2A\u01c3\3")
        buf.write("\2\2\2C\u01c5\3\2\2\2E\u01c7\3\2\2\2G\u01c9\3\2\2\2I\u01cc")
        buf.write("\3\2\2\2K\u01ce\3\2\2\2M\u01d1\3\2\2\2O\u01d3\3\2\2\2")
        buf.write("Q\u01d6\3\2\2\2S\u01d8\3\2\2\2U\u01db\3\2\2\2W\u01dd\3")
        buf.write("\2\2\2Y\u01df\3\2\2\2[\u01e2\3\2\2\2]\u01e5\3\2\2\2_\u01e8")
        buf.write("\3\2\2\2a\u01eb\3\2\2\2c\u01ed\3\2\2\2e\u01ef\3\2\2\2")
        buf.write("g\u01f2\3\2\2\2i\u01f5\3\2\2\2k\u01f9\3\2\2\2m\u01fc\3")
        buf.write("\2\2\2o\u01ff\3\2\2\2q\u0203\3\2\2\2s\u0207\3\2\2\2u\u0209")
        buf.write("\3\2\2\2w\u020b\3\2\2\2y\u020d\3\2\2\2{\u020f\3\2\2\2")
        buf.write("}\u0211\3\2\2\2\177\u0213\3\2\2\2\u0081\u0215\3\2\2\2")
        buf.write("\u0083\u0217\3\2\2\2\u0085\u021d\3\2\2\2\u0087\u021f\3")
        buf.write("\2\2\2\u0089\u023a\3\2\2\2\u008b\u0250\3\2\2\2\u008d\u0252")
        buf.write("\3\2\2\2\u008f\u027f\3\2\2\2\u0091\u0283\3\2\2\2\u0093")
        buf.write("\u028b\3\2\2\2\u0095\u028f\3\2\2\2\u0097\u0291\3\2\2\2")
        buf.write("\u0099\u02a2\3\2\2\2\u009b\u02a4\3\2\2\2\u009d\u02c8\3")
        buf.write("\2\2\2\u009f\u02d1\3\2\2\2\u00a1\u02dd\3\2\2\2\u00a3\u02e0")
        buf.write("\3\2\2\2\u00a5\u02e6\3\2\2\2\u00a7\u02f4\3\2\2\2\u00a9")
        buf.write("\u02ff\3\2\2\2\u00ab\u00ac\7X\2\2\u00ac\u00ad\7c\2\2\u00ad")
        buf.write("\u00ae\7t\2\2\u00ae\u00af\7<\2\2\u00af\u00b0\7\"\2\2\u00b0")
        buf.write("\4\3\2\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3")
        buf.write("\u00b4\7v\2\2\u00b4\u00b5\7a\2\2\u00b5\u00b6\7q\2\2\u00b6")
        buf.write("\u00b7\7h\2\2\u00b7\u00b8\7a\2\2\u00b8\u00b9\7h\2\2\u00b9")
        buf.write("\u00ba\7n\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7c\2\2\u00bc")
        buf.write("\u00bd\7v\2\2\u00bd\6\3\2\2\2\u00be\u00bf\7h\2\2\u00bf")
        buf.write("\u00c0\7n\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2\7c\2\2\u00c2")
        buf.write("\u00c3\7v\2\2\u00c3\u00c4\7a\2\2\u00c4\u00c5\7v\2\2\u00c5")
        buf.write("\u00c6\7q\2\2\u00c6\u00c7\7a\2\2\u00c7\u00c8\7k\2\2\u00c8")
        buf.write("\u00c9\7p\2\2\u00c9\u00ca\7v\2\2\u00ca\b\3\2\2\2\u00cb")
        buf.write("\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce")
        buf.write("\u00cf\7a\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1\7h\2\2\u00d1")
        buf.write("\u00d2\7a\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7v\2\2\u00d4")
        buf.write("\u00d5\7t\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7")
        buf.write("\u00d8\7i\2\2\u00d8\n\3\2\2\2\u00d9\u00da\7u\2\2\u00da")
        buf.write("\u00db\7v\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7k\2\2\u00dd")
        buf.write("\u00de\7p\2\2\u00de\u00df\7i\2\2\u00df\u00e0\7a\2\2\u00e0")
        buf.write("\u00e1\7q\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3\7a\2\2\u00e3")
        buf.write("\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7v\2\2\u00e6")
        buf.write("\f\3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9\7n\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7v\2\2\u00ec")
        buf.write("\u00ed\7a\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7q\2\2\u00ef")
        buf.write("\u00f0\7a\2\2\u00f0\u00f1\7u\2\2\u00f1\u00f2\7v\2\2\u00f2")
        buf.write("\u00f3\7t\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7p\2\2\u00f5")
        buf.write("\u00f6\7i\2\2\u00f6\16\3\2\2\2\u00f7\u00f8\7u\2\2\u00f8")
        buf.write("\u00f9\7v\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7k\2\2\u00fb")
        buf.write("\u00fc\7p\2\2\u00fc\u00fd\7i\2\2\u00fd\u00fe\7a\2\2\u00fe")
        buf.write("\u00ff\7q\2\2\u00ff\u0100\7h\2\2\u0100\u0101\7a\2\2\u0101")
        buf.write("\u0102\7h\2\2\u0102\u0103\7n\2\2\u0103\u0104\7q\2\2\u0104")
        buf.write("\u0105\7c\2\2\u0105\u0106\7v\2\2\u0106\20\3\2\2\2\u0107")
        buf.write("\u0108\7d\2\2\u0108\u0109\7q\2\2\u0109\u010a\7q\2\2\u010a")
        buf.write("\u010b\7n\2\2\u010b\u010c\7a\2\2\u010c\u010d\7q\2\2\u010d")
        buf.write("\u010e\7h\2\2\u010e\u010f\7a\2\2\u010f\u0110\7u\2\2\u0110")
        buf.write("\u0111\7v\2\2\u0111\u0112\7t\2\2\u0112\u0113\7k\2\2\u0113")
        buf.write("\u0114\7p\2\2\u0114\u0115\7i\2\2\u0115\22\3\2\2\2\u0116")
        buf.write("\u0117\7u\2\2\u0117\u0118\7v\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write("\u011a\7k\2\2\u011a\u011b\7p\2\2\u011b\u011c\7i\2\2\u011c")
        buf.write("\u011d\7a\2\2\u011d\u011e\7q\2\2\u011e\u011f\7h\2\2\u011f")
        buf.write("\u0120\7a\2\2\u0120\u0121\7d\2\2\u0121\u0122\7q\2\2\u0122")
        buf.write("\u0123\7q\2\2\u0123\u0124\7n\2\2\u0124\24\3\2\2\2\u0125")
        buf.write("\u0129\t\2\2\2\u0126\u0128\t\3\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\26\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d")
        buf.write("\7D\2\2\u012d\u012e\7q\2\2\u012e\u012f\7f\2\2\u012f\u0130")
        buf.write("\7{\2\2\u0130\30\3\2\2\2\u0131\u0132\7G\2\2\u0132\u0133")
        buf.write("\7n\2\2\u0133\u0134\7u\2\2\u0134\u0135\7g\2\2\u0135\32")
        buf.write("\3\2\2\2\u0136\u0137\7G\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7f\2\2\u0139\u013a\7h\2\2\u013a\u013b\7q\2\2\u013b\u013c")
        buf.write("\7t\2\2\u013c\34\3\2\2\2\u013d\u013e\7K\2\2\u013e\u013f")
        buf.write("\7h\2\2\u013f\36\3\2\2\2\u0140\u0141\7X\2\2\u0141\u0142")
        buf.write("\7c\2\2\u0142\u0143\7t\2\2\u0143 \3\2\2\2\u0144\u0145")
        buf.write("\7G\2\2\u0145\u0146\7p\2\2\u0146\u0147\7f\2\2\u0147\u0148")
        buf.write("\7F\2\2\u0148\u0149\7q\2\2\u0149\"\3\2\2\2\u014a\u014b")
        buf.write("\7D\2\2\u014b\u014c\7t\2\2\u014c\u014d\7g\2\2\u014d\u014e")
        buf.write("\7c\2\2\u014e\u014f\7m\2\2\u014f$\3\2\2\2\u0150\u0151")
        buf.write("\7G\2\2\u0151\u0152\7n\2\2\u0152\u0153\7u\2\2\u0153\u0154")
        buf.write("\7g\2\2\u0154\u0155\7K\2\2\u0155\u0156\7h\2\2\u0156&\3")
        buf.write("\2\2\2\u0157\u0158\7G\2\2\u0158\u0159\7p\2\2\u0159\u015a")
        buf.write("\7f\2\2\u015a\u015b\7Y\2\2\u015b\u015c\7j\2\2\u015c\u015d")
        buf.write("\7k\2\2\u015d\u015e\7n\2\2\u015e\u015f\7g\2\2\u015f(\3")
        buf.write("\2\2\2\u0160\u0161\7R\2\2\u0161\u0162\7c\2\2\u0162\u0163")
        buf.write("\7t\2\2\u0163\u0164\7c\2\2\u0164\u0165\7o\2\2\u0165\u0166")
        buf.write("\7g\2\2\u0166\u0167\7v\2\2\u0167\u0168\7g\2\2\u0168\u0169")
        buf.write("\7t\2\2\u0169*\3\2\2\2\u016a\u016b\7Y\2\2\u016b\u016c")
        buf.write("\7j\2\2\u016c\u016d\7k\2\2\u016d\u016e\7n\2\2\u016e\u016f")
        buf.write("\7g\2\2\u016f,\3\2\2\2\u0170\u0171\7E\2\2\u0171\u0172")
        buf.write("\7q\2\2\u0172\u0173\7p\2\2\u0173\u0174\7v\2\2\u0174\u0175")
        buf.write("\7k\2\2\u0175\u0176\7p\2\2\u0176\u0177\7w\2\2\u0177\u0178")
        buf.write("\7g\2\2\u0178.\3\2\2\2\u0179\u017a\7G\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017b\u017c\7f\2\2\u017c\u017d\7D\2\2\u017d\u017e")
        buf.write("\7q\2\2\u017e\u017f\7f\2\2\u017f\u0180\7{\2\2\u0180\60")
        buf.write("\3\2\2\2\u0181\u0182\7H\2\2\u0182\u0183\7q\2\2\u0183\u0184")
        buf.write("\7t\2\2\u0184\62\3\2\2\2\u0185\u0186\7T\2\2\u0186\u0187")
        buf.write("\7g\2\2\u0187\u0188\7v\2\2\u0188\u0189\7w\2\2\u0189\u018a")
        buf.write("\7t\2\2\u018a\u018b\7p\2\2\u018b\64\3\2\2\2\u018c\u018d")
        buf.write("\7V\2\2\u018d\u018e\7t\2\2\u018e\u018f\7w\2\2\u018f\u0190")
        buf.write("\7g\2\2\u0190\66\3\2\2\2\u0191\u0192\7F\2\2\u0192\u0193")
        buf.write("\7q\2\2\u01938\3\2\2\2\u0194\u0195\7G\2\2\u0195\u0196")
        buf.write("\7p\2\2\u0196\u0197\7f\2\2\u0197\u0198\7K\2\2\u0198\u0199")
        buf.write("\7h\2\2\u0199:\3\2\2\2\u019a\u019b\7H\2\2\u019b\u019c")
        buf.write("\7w\2\2\u019c\u019d\7p\2\2\u019d\u019e\7e\2\2\u019e\u019f")
        buf.write("\7v\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2")
        buf.write("\7p\2\2\u01a2<\3\2\2\2\u01a3\u01a4\7V\2\2\u01a4\u01a5")
        buf.write("\7j\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7\7p\2\2\u01a7>\3")
        buf.write("\2\2\2\u01a8\u01a9\7H\2\2\u01a9\u01aa\7c\2\2\u01aa\u01ab")
        buf.write("\7n\2\2\u01ab\u01ac\7u\2\2\u01ac\u01ad\7g\2\2\u01ad@\3")
        buf.write("\2\2\2\u01ae\u01c4\5\27\f\2\u01af\u01c4\5\31\r\2\u01b0")
        buf.write("\u01c4\5\33\16\2\u01b1\u01c4\5\35\17\2\u01b2\u01c4\5\37")
        buf.write("\20\2\u01b3\u01c4\5!\21\2\u01b4\u01c4\5#\22\2\u01b5\u01c4")
        buf.write("\5%\23\2\u01b6\u01c4\5\'\24\2\u01b7\u01c4\5)\25\2\u01b8")
        buf.write("\u01c4\5+\26\2\u01b9\u01c4\5-\27\2\u01ba\u01c4\5/\30\2")
        buf.write("\u01bb\u01c4\5\61\31\2\u01bc\u01c4\5\63\32\2\u01bd\u01c4")
        buf.write("\5\65\33\2\u01be\u01c4\5\67\34\2\u01bf\u01c4\59\35\2\u01c0")
        buf.write("\u01c4\5;\36\2\u01c1\u01c4\5=\37\2\u01c2\u01c4\5? \2\u01c3")
        buf.write("\u01ae\3\2\2\2\u01c3\u01af\3\2\2\2\u01c3\u01b0\3\2\2\2")
        buf.write("\u01c3\u01b1\3\2\2\2\u01c3\u01b2\3\2\2\2\u01c3\u01b3\3")
        buf.write("\2\2\2\u01c3\u01b4\3\2\2\2\u01c3\u01b5\3\2\2\2\u01c3\u01b6")
        buf.write("\3\2\2\2\u01c3\u01b7\3\2\2\2\u01c3\u01b8\3\2\2\2\u01c3")
        buf.write("\u01b9\3\2\2\2\u01c3\u01ba\3\2\2\2\u01c3\u01bb\3\2\2\2")
        buf.write("\u01c3\u01bc\3\2\2\2\u01c3\u01bd\3\2\2\2\u01c3\u01be\3")
        buf.write("\2\2\2\u01c3\u01bf\3\2\2\2\u01c3\u01c0\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4B\3\2\2\2\u01c5\u01c6")
        buf.write("\7?\2\2\u01c6D\3\2\2\2\u01c7\u01c8\7-\2\2\u01c8F\3\2\2")
        buf.write("\2\u01c9\u01ca\7-\2\2\u01ca\u01cb\7\60\2\2\u01cbH\3\2")
        buf.write("\2\2\u01cc\u01cd\7/\2\2\u01cdJ\3\2\2\2\u01ce\u01cf\7/")
        buf.write("\2\2\u01cf\u01d0\7\60\2\2\u01d0L\3\2\2\2\u01d1\u01d2\7")
        buf.write(",\2\2\u01d2N\3\2\2\2\u01d3\u01d4\7,\2\2\u01d4\u01d5\7")
        buf.write("\60\2\2\u01d5P\3\2\2\2\u01d6\u01d7\7^\2\2\u01d7R\3\2\2")
        buf.write("\2\u01d8\u01d9\7^\2\2\u01d9\u01da\7\60\2\2\u01daT\3\2")
        buf.write("\2\2\u01db\u01dc\7\'\2\2\u01dcV\3\2\2\2\u01dd\u01de\7")
        buf.write("#\2\2\u01deX\3\2\2\2\u01df\u01e0\7(\2\2\u01e0\u01e1\7")
        buf.write("(\2\2\u01e1Z\3\2\2\2\u01e2\u01e3\7~\2\2\u01e3\u01e4\7")
        buf.write("~\2\2\u01e4\\\3\2\2\2\u01e5\u01e6\7?\2\2\u01e6\u01e7\7")
        buf.write("?\2\2\u01e7^\3\2\2\2\u01e8\u01e9\7#\2\2\u01e9\u01ea\7")
        buf.write("?\2\2\u01ea`\3\2\2\2\u01eb\u01ec\7>\2\2\u01ecb\3\2\2\2")
        buf.write("\u01ed\u01ee\7@\2\2\u01eed\3\2\2\2\u01ef\u01f0\7>\2\2")
        buf.write("\u01f0\u01f1\7?\2\2\u01f1f\3\2\2\2\u01f2\u01f3\7@\2\2")
        buf.write("\u01f3\u01f4\7?\2\2\u01f4h\3\2\2\2\u01f5\u01f6\7?\2\2")
        buf.write("\u01f6\u01f7\7\61\2\2\u01f7\u01f8\7?\2\2\u01f8j\3\2\2")
        buf.write("\2\u01f9\u01fa\7>\2\2\u01fa\u01fb\7\60\2\2\u01fbl\3\2")
        buf.write("\2\2\u01fc\u01fd\7@\2\2\u01fd\u01fe\7\60\2\2\u01fen\3")
        buf.write("\2\2\2\u01ff\u0200\7>\2\2\u0200\u0201\7?\2\2\u0201\u0202")
        buf.write("\7\60\2\2\u0202p\3\2\2\2\u0203\u0204\7@\2\2\u0204\u0205")
        buf.write("\7?\2\2\u0205\u0206\7\60\2\2\u0206r\3\2\2\2\u0207\u0208")
        buf.write("\7*\2\2\u0208t\3\2\2\2\u0209\u020a\7+\2\2\u020av\3\2\2")
        buf.write("\2\u020b\u020c\7]\2\2\u020cx\3\2\2\2\u020d\u020e\7_\2")
        buf.write("\2\u020ez\3\2\2\2\u020f\u0210\7}\2\2\u0210|\3\2\2\2\u0211")
        buf.write("\u0212\7\177\2\2\u0212~\3\2\2\2\u0213\u0214\7<\2\2\u0214")
        buf.write("\u0080\3\2\2\2\u0215\u0216\7\60\2\2\u0216\u0082\3\2\2")
        buf.write("\2\u0217\u0218\7.\2\2\u0218\u0084\3\2\2\2\u0219\u021e")
        buf.write("\5\u0087D\2\u021a\u021e\5\u0089E\2\u021b\u021e\5\u008b")
        buf.write("F\2\u021c\u021e\7\62\2\2\u021d\u0219\3\2\2\2\u021d\u021a")
        buf.write("\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021c\3\2\2\2\u021e")
        buf.write("\u0086\3\2\2\2\u021f\u0223\t\4\2\2\u0220\u0222\t\5\2\2")
        buf.write("\u0221\u0220\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221\3")
        buf.write("\2\2\2\u0223\u0224\3\2\2\2\u0224\u0088\3\2\2\2\u0225\u0223")
        buf.write("\3\2\2\2\u0226\u0227\7\62\2\2\u0227\u0228\7z\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u022d\t\6\2\2\u022a\u022c\t\7\2\2")
        buf.write("\u022b\u022a\3\2\2\2\u022c\u022f\3\2\2\2\u022d\u022b\3")
        buf.write("\2\2\2\u022d\u022e\3\2\2\2\u022e\u023b\3\2\2\2\u022f\u022d")
        buf.write("\3\2\2\2\u0230\u0231\7\62\2\2\u0231\u0232\7Z\2\2\u0232")
        buf.write("\u0233\3\2\2\2\u0233\u0237\t\6\2\2\u0234\u0236\t\7\2\2")
        buf.write("\u0235\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0237\u0238\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u023a\u0226\3\2\2\2\u023a\u0230\3\2\2\2\u023b")
        buf.write("\u008a\3\2\2\2\u023c\u023d\7\62\2\2\u023d\u023e\7q\2\2")
        buf.write("\u023e\u023f\3\2\2\2\u023f\u0243\t\b\2\2\u0240\u0242\t")
        buf.write("\t\2\2\u0241\u0240\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241")
        buf.write("\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0251\3\2\2\2\u0245")
        buf.write("\u0243\3\2\2\2\u0246\u0247\7\62\2\2\u0247\u0248\7Q\2\2")
        buf.write("\u0248\u0249\3\2\2\2\u0249\u024d\t\b\2\2\u024a\u024c\t")
        buf.write("\t\2\2\u024b\u024a\3\2\2\2\u024c\u024f\3\2\2\2\u024d\u024b")
        buf.write("\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u0251\3\2\2\2\u024f")
        buf.write("\u024d\3\2\2\2\u0250\u023c\3\2\2\2\u0250\u0246\3\2\2\2")
        buf.write("\u0251\u008c\3\2\2\2\u0252\u0254\t\n\2\2\u0253\u0255\7")
        buf.write("/\2\2\u0254\u0253\3\2\2\2\u0254\u0255\3\2\2\2\u0255\u0257")
        buf.write("\3\2\2\2\u0256\u0258\t\5\2\2\u0257\u0256\3\2\2\2\u0258")
        buf.write("\u0259\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2")
        buf.write("\u025a\u008e\3\2\2\2\u025b\u025d\t\5\2\2\u025c\u025b\3")
        buf.write("\2\2\2\u025d\u025e\3\2\2\2\u025e\u025c\3\2\2\2\u025e\u025f")
        buf.write("\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0280\5\u008dG\2\u0261")
        buf.write("\u0263\t\5\2\2\u0262\u0261\3\2\2\2\u0263\u0264\3\2\2\2")
        buf.write("\u0264\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0266\3")
        buf.write("\2\2\2\u0266\u026e\7\60\2\2\u0267\u0269\t\5\2\2\u0268")
        buf.write("\u0267\3\2\2\2\u0269\u026c\3\2\2\2\u026a\u0268\3\2\2\2")
        buf.write("\u026a\u026b\3\2\2\2\u026b\u026d\3\2\2\2\u026c\u026a\3")
        buf.write("\2\2\2\u026d\u026f\5\u008dG\2\u026e\u026a\3\2\2\2\u026e")
        buf.write("\u026f\3\2\2\2\u026f\u0280\3\2\2\2\u0270\u0272\t\5\2\2")
        buf.write("\u0271\u0270\3\2\2\2\u0272\u0275\3\2\2\2\u0273\u0271\3")
        buf.write("\2\2\2\u0273\u0274\3\2\2\2\u0274\u0276\3\2\2\2\u0275\u0273")
        buf.write("\3\2\2\2\u0276\u0278\7\60\2\2\u0277\u0279\t\5\2\2\u0278")
        buf.write("\u0277\3\2\2\2\u0279\u027a\3\2\2\2\u027a\u0278\3\2\2\2")
        buf.write("\u027a\u027b\3\2\2\2\u027b\u027d\3\2\2\2\u027c\u027e\5")
        buf.write("\u008dG\2\u027d\u027c\3\2\2\2\u027d\u027e\3\2\2\2\u027e")
        buf.write("\u0280\3\2\2\2\u027f\u025c\3\2\2\2\u027f\u0262\3\2\2\2")
        buf.write("\u027f\u0273\3\2\2\2\u0280\u0090\3\2\2\2\u0281\u0284\5")
        buf.write("\65\33\2\u0282\u0284\5? \2\u0283\u0281\3\2\2\2\u0283\u0282")
        buf.write("\3\2\2\2\u0284\u0092\3\2\2\2\u0285\u0286\7^\2\2\u0286")
        buf.write("\u028c\t\13\2\2\u0287\u0288\7)\2\2\u0288\u028c\7$\2\2")
        buf.write("\u0289\u028a\7^\2\2\u028a\u028c\7d\2\2\u028b\u0285\3\2")
        buf.write("\2\2\u028b\u0287\3\2\2\2\u028b\u0289\3\2\2\2\u028c\u0094")
        buf.write("\3\2\2\2\u028d\u0290\n\f\2\2\u028e\u0290\5\u0093J\2\u028f")
        buf.write("\u028d\3\2\2\2\u028f\u028e\3\2\2\2\u0290\u0096\3\2\2\2")
        buf.write("\u0291\u0296\7$\2\2\u0292\u0295\5\u0093J\2\u0293\u0295")
        buf.write("\n\r\2\2\u0294\u0292\3\2\2\2\u0294\u0293\3\2\2\2\u0295")
        buf.write("\u0298\3\2\2\2\u0296\u0294\3\2\2\2\u0296\u0297\3\2\2\2")
        buf.write("\u0297\u0299\3\2\2\2\u0298\u0296\3\2\2\2\u0299\u029a\7")
        buf.write("$\2\2\u029a\u029b\bL\2\2\u029b\u0098\3\2\2\2\u029c\u02a3")
        buf.write("\5\u0085C\2\u029d\u02a3\5\u008fH\2\u029e\u02a3\5\u0097")
        buf.write("L\2\u029f\u02a3\5\u0091I\2\u02a0\u02a3\5\u009bN\2\u02a1")
        buf.write("\u02a3\3\2\2\2\u02a2\u029c\3\2\2\2\u02a2\u029d\3\2\2\2")
        buf.write("\u02a2\u029e\3\2\2\2\u02a2\u029f\3\2\2\2\u02a2\u02a0\3")
        buf.write("\2\2\2\u02a2\u02a1\3\2\2\2\u02a3\u009a\3\2\2\2\u02a4\u02a8")
        buf.write("\5{>\2\u02a5\u02a7\5\u00a3R\2\u02a6\u02a5\3\2\2\2\u02a7")
        buf.write("\u02aa\3\2\2\2\u02a8\u02a6\3\2\2\2\u02a8\u02a9\3\2\2\2")
        buf.write("\u02a9\u02ab\3\2\2\2\u02aa\u02a8\3\2\2\2\u02ab\u02bc\5")
        buf.write("\u0099M\2\u02ac\u02ae\5\u00a3R\2\u02ad\u02ac\3\2\2\2\u02ae")
        buf.write("\u02b1\3\2\2\2\u02af\u02ad\3\2\2\2\u02af\u02b0\3\2\2\2")
        buf.write("\u02b0\u02b2\3\2\2\2\u02b1\u02af\3\2\2\2\u02b2\u02b6\7")
        buf.write(".\2\2\u02b3\u02b5\5\u00a3R\2\u02b4\u02b3\3\2\2\2\u02b5")
        buf.write("\u02b8\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b6\u02b7\3\2\2\2")
        buf.write("\u02b7\u02b9\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b9\u02bb\5")
        buf.write("\u0099M\2\u02ba\u02af\3\2\2\2\u02bb\u02be\3\2\2\2\u02bc")
        buf.write("\u02ba\3\2\2\2\u02bc\u02bd\3\2\2\2\u02bd\u02c2\3\2\2\2")
        buf.write("\u02be\u02bc\3\2\2\2\u02bf\u02c1\5\u00a3R\2\u02c0\u02bf")
        buf.write("\3\2\2\2\u02c1\u02c4\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c2")
        buf.write("\u02c3\3\2\2\2\u02c3\u02c5\3\2\2\2\u02c4\u02c2\3\2\2\2")
        buf.write("\u02c5\u02c6\5}?\2\u02c6\u02c7\bN\3\2\u02c7\u009c\3\2")
        buf.write("\2\2\u02c8\u02cc\7$\2\2\u02c9\u02cb\5\u0095K\2\u02ca\u02c9")
        buf.write("\3\2\2\2\u02cb\u02ce\3\2\2\2\u02cc\u02ca\3\2\2\2\u02cc")
        buf.write("\u02cd\3\2\2\2\u02cd\u02cf\3\2\2\2\u02ce\u02cc\3\2\2\2")
        buf.write("\u02cf\u02d0\bO\4\2\u02d0\u009e\3\2\2\2\u02d1\u02d5\7")
        buf.write("$\2\2\u02d2\u02d4\5\u0095K\2\u02d3\u02d2\3\2\2\2\u02d4")
        buf.write("\u02d7\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2")
        buf.write("\u02d6\u02d8\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d8\u02d9\7")
        buf.write("^\2\2\u02d9\u02da\n\16\2\2\u02da\u02db\3\2\2\2\u02db\u02dc")
        buf.write("\bP\5\2\u02dc\u00a0\3\2\2\2\u02dd\u02de\7=\2\2\u02de\u00a2")
        buf.write("\3\2\2\2\u02df\u02e1\t\17\2\2\u02e0\u02df\3\2\2\2\u02e1")
        buf.write("\u02e2\3\2\2\2\u02e2\u02e0\3\2\2\2\u02e2\u02e3\3\2\2\2")
        buf.write("\u02e3\u02e4\3\2\2\2\u02e4\u02e5\bR\6\2\u02e5\u00a4\3")
        buf.write("\2\2\2\u02e6\u02e7\7,\2\2\u02e7\u02e8\7,\2\2\u02e8\u02ec")
        buf.write("\3\2\2\2\u02e9\u02eb\13\2\2\2\u02ea\u02e9\3\2\2\2\u02eb")
        buf.write("\u02ee\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ec\u02ea\3\2\2\2")
        buf.write("\u02ed\u02ef\3\2\2\2\u02ee\u02ec\3\2\2\2\u02ef\u02f0\7")
        buf.write(",\2\2\u02f0\u02f1\7,\2\2\u02f1\u02f2\3\2\2\2\u02f2\u02f3")
        buf.write("\bS\6\2\u02f3\u00a6\3\2\2\2\u02f4\u02f5\7,\2\2\u02f5\u02f6")
        buf.write("\7,\2\2\u02f6\u02fc\3\2\2\2\u02f7\u02f8\7,\2\2\u02f8\u02fb")
        buf.write("\n\20\2\2\u02f9\u02fb\n\20\2\2\u02fa\u02f7\3\2\2\2\u02fa")
        buf.write("\u02f9\3\2\2\2\u02fb\u02fe\3\2\2\2\u02fc\u02fa\3\2\2\2")
        buf.write("\u02fc\u02fd\3\2\2\2\u02fd\u00a8\3\2\2\2\u02fe\u02fc\3")
        buf.write("\2\2\2\u02ff\u0300\13\2\2\2\u0300\u00aa\3\2\2\2(\2\u0129")
        buf.write("\u01c3\u021d\u0223\u022d\u0237\u023a\u0243\u024d\u0250")
        buf.write("\u0254\u0259\u025e\u0264\u026a\u026e\u0273\u027a\u027d")
        buf.write("\u027f\u0283\u028b\u028f\u0294\u0296\u02a2\u02a8\u02af")
        buf.write("\u02b6\u02bc\u02c2\u02cc\u02d5\u02e2\u02ec\u02fa\u02fc")
        buf.write("\7\3L\2\3N\3\3O\4\3P\5\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    ID = 10
    BODY = 11
    ELSE = 12
    ENDFOR = 13
    IF = 14
    VAR = 15
    ENDDO = 16
    BREAK = 17
    ELSEIF = 18
    ENDWHILE = 19
    PARAMETER = 20
    WHILE = 21
    CONTINUE = 22
    ENDBODY = 23
    FOR = 24
    RETURN = 25
    TRUE = 26
    DO = 27
    ENDIF = 28
    FUNCTION = 29
    THEN = 30
    FALSE = 31
    KEYWORDS = 32
    ASSIGN = 33
    ADD = 34
    ADD_FLOAT = 35
    SUB = 36
    SUB_FLOAT = 37
    MUL = 38
    MUL_FLOAT = 39
    DIVISION = 40
    DIVISION_FLOAT = 41
    MOD = 42
    NEGATIVE = 43
    AND = 44
    OR = 45
    EQUAL = 46
    IS_NOT_EQUAL = 47
    LESS = 48
    MORE_THAN = 49
    LESS_OR_EQUAL = 50
    MORE_OR_EQUAL = 51
    NOT_EQUAL_FLOAT = 52
    LESS_FLOAT = 53
    MORE_FLOAT = 54
    LESS_OR_EQUAL_FLOAT = 55
    MORE_OR_EQUAL_FLOAT = 56
    LEFT_ROUND_BRACKET = 57
    RIGHT_ROUND_BRACKET = 58
    LEFT_SQUARE_BRACKET = 59
    RIGHT_SQUARE_BRACKET = 60
    LEFT_CURLY_BRACKET = 61
    RIGHT_CURLY_BRACKET = 62
    COLON = 63
    DOT = 64
    COMMA = 65
    INTEGER = 66
    FLOAT = 67
    BOOLEAN = 68
    STRING = 69
    ARRAY = 70
    UNCLOSE_STRING = 71
    ILLEGAL_ESCAPE = 72
    SEMI = 73
    WS = 74
    BLOCK_COMMENT = 75
    UNTERMINATED_COMMENT = 76
    ERROR_CHAR = 77

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Var: '", "'int_of_float'", "'float_to_int'", "'int_of_string'", 
            "'string_of_int'", "'float_to_string'", "'string_of_float'", 
            "'bool_of_string'", "'string_of_bool'", "'Body'", "'Else'", 
            "'Endfor'", "'If'", "'Var'", "'EndDo'", "'Break'", "'ElseIf'", 
            "'EndWhile'", "'Parameter'", "'While'", "'Continue'", "'EndBody'", 
            "'For'", "'Return'", "'True'", "'Do'", "'EndIf'", "'Function'", 
            "'Then'", "'False'", "'='", "'+'", "'+.'", "'-'", "'-.'", "'*'", 
            "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", 
            "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "':'", "'.'", "','", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "BODY", "ELSE", "ENDFOR", "IF", "VAR", "ENDDO", "BREAK", 
            "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", 
            "FOR", "RETURN", "TRUE", "DO", "ENDIF", "FUNCTION", "THEN", 
            "FALSE", "KEYWORDS", "ASSIGN", "ADD", "ADD_FLOAT", "SUB", "SUB_FLOAT", 
            "MUL", "MUL_FLOAT", "DIVISION", "DIVISION_FLOAT", "MOD", "NEGATIVE", 
            "AND", "OR", "EQUAL", "IS_NOT_EQUAL", "LESS", "MORE_THAN", "LESS_OR_EQUAL", 
            "MORE_OR_EQUAL", "NOT_EQUAL_FLOAT", "LESS_FLOAT", "MORE_FLOAT", 
            "LESS_OR_EQUAL_FLOAT", "MORE_OR_EQUAL_FLOAT", "LEFT_ROUND_BRACKET", 
            "RIGHT_ROUND_BRACKET", "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", 
            "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", "COLON", "DOT", 
            "COMMA", "INTEGER", "FLOAT", "BOOLEAN", "STRING", "ARRAY", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "SEMI", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "ID", "BODY", "ELSE", "ENDFOR", "IF", 
                  "VAR", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", 
                  "WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", 
                  "DO", "ENDIF", "FUNCTION", "THEN", "FALSE", "KEYWORDS", 
                  "ASSIGN", "ADD", "ADD_FLOAT", "SUB", "SUB_FLOAT", "MUL", 
                  "MUL_FLOAT", "DIVISION", "DIVISION_FLOAT", "MOD", "NEGATIVE", 
                  "AND", "OR", "EQUAL", "IS_NOT_EQUAL", "LESS", "MORE_THAN", 
                  "LESS_OR_EQUAL", "MORE_OR_EQUAL", "NOT_EQUAL_FLOAT", "LESS_FLOAT", 
                  "MORE_FLOAT", "LESS_OR_EQUAL_FLOAT", "MORE_OR_EQUAL_FLOAT", 
                  "LEFT_ROUND_BRACKET", "RIGHT_ROUND_BRACKET", "LEFT_SQUARE_BRACKET", 
                  "RIGHT_SQUARE_BRACKET", "LEFT_CURLY_BRACKET", "RIGHT_CURLY_BRACKET", 
                  "COLON", "DOT", "COMMA", "INTEGER", "BASE10", "BASE16", 
                  "BASE8", "EXPONENT", "FLOAT", "BOOLEAN", "EscapeSequence", 
                  "Character", "STRING", "LITERALS", "ARRAY", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "SEMI", "WS", "BLOCK_COMMENT", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[74] = self.STRING_action 
            actions[76] = self.ARRAY_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = self.text[1:-1]
            	
     

    def ARRAY_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace(" ","")	
            	self.text = self.text.replace("\"","")	
            	self.text = self.text.replace("\n","")	
            	self.text = self.text.replace("\t","")	
            	self.text = self.text.replace("\r","")	

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise IllegalEscape(self.text[1:])
            	
     


