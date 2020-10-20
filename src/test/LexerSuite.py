import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(""" switch (tr) {case 1:cout<<"C";break; case 2:cout<<"CC";break;} ""","""switch,(,tr,),{,case,1,:,cout,<,<,C,;,break,;,case,2,:,cout,<,<,CC,;,break,;,},<EOF>""",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_error_token(self):
        """test error token"""
        self.assertTrue(TestLexer.checkLexeme("""#""","""Error Token #""",108))
        self.assertTrue(TestLexer.checkLexeme(""" "khoa hoc may tinh" #""","""khoa hoc may tinh,Error Token #""",109))
        self.assertTrue(TestLexer.checkLexeme(""" khoa hoc may tinh_# ""","""khoa,hoc,may,tinh_,Error Token #""",110))
        self.assertTrue(TestLexer.checkLexeme(""" khoahoc@maytinh ""","""khoahoc,Error Token @""",111))
        self.assertTrue(TestLexer.checkLexeme(""" ^aaaaa ""","""Error Token ^""",112))

    def test113(self):
        """test113"""
        self.assertTrue(TestLexer.checkLexeme("""" abc ""","""Unclosed String:  abc """,113))

    def test_id(self):
        """test id"""
        self.assertTrue(TestLexer.checkLexeme("""hongphong""","""hongphong,<EOF>""",114))
        self.assertTrue(TestLexer.checkLexeme(""" hong phong ""","""hong,phong,<EOF>""",115))
        self.assertTrue(TestLexer.checkLexeme(""" 1phong ""","""1,phong,<EOF>""",116))
        self.assertTrue(TestLexer.checkLexeme(""" _phongle ""","""Error Token _""",117))
        self.assertTrue(TestLexer.checkLexeme(""" 0P ""","""0,Error Token P""",118))
        self.assertTrue(TestLexer.checkLexeme(""" phong_le ""","""phong_le,<EOF>""",119))
        self.assertTrue(TestLexer.checkLexeme(""" phong-le ""","""phong,-,le,<EOF>""",120))
        self.assertTrue(TestLexer.checkLexeme(""" p_ ""","""p_,<EOF>""",121))
        self.assertTrue(TestLexer.checkLexeme(""" p123 ""","""p123,<EOF>""",122))

    def test_boolean(self):
        """test boolean"""
        self.assertTrue(TestLexer.checkLexeme(""" "TRUE" ""","""TRUE,<EOF>""",123))
        self.assertTrue(TestLexer.checkLexeme(""" "FALSE" ""","""FALSE,<EOF>""",124))
        self.assertTrue(TestLexer.checkLexeme(""" "True" ""","""True,<EOF>""",125))
        self.assertTrue(TestLexer.checkLexeme(""" "tRUE" ""","""tRUE,<EOF>""",126))
        self.assertTrue(TestLexer.checkLexeme(""" "TRUE FALSE" ""","""TRUE FALSE,<EOF>""",127))
        self.assertTrue(TestLexer.checkLexeme(""" "TRue" "FaLSE" ""","""TRue,FaLSE,<EOF>""",128))
        self.assertTrue(TestLexer.checkLexeme(""" "TRUE" "FALSE" ""","""TRUE,FALSE,<EOF>""",129))

    def test_integer(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("""123 456""","""123,456,<EOF>""",130))
        self.assertTrue(TestLexer.checkLexeme(""" 123_456 ""","""123,Error Token _""",131))
        self.assertTrue(TestLexer.checkLexeme(""" 0xFF ""","""0xFF,<EOF>""",132))
        self.assertTrue(TestLexer.checkLexeme(""" 0XABC ""","""0XABC,<EOF>""",133))
        self.assertTrue(TestLexer.checkLexeme(""" 0o123 ""","""0o123,<EOF>""",134))
        self.assertTrue(TestLexer.checkLexeme(""" 0999 ""","""0,999,<EOF>""",135))
        self.assertTrue(TestLexer.checkLexeme(""" 0O11 ""","""0O11,<EOF>""",136))
        self.assertTrue(TestLexer.checkLexeme(""" 00000001 ""","""0,0,0,0,0,0,0,1,<EOF>""",137))
        self.assertTrue(TestLexer.checkLexeme(""" 123456789 ""","""123456789,<EOF>""",138))   

    def test_float(self):
        """test float"""
        self.assertTrue(TestLexer.checkLexeme("""9.25""","""9.25,<EOF>""",139))
        self.assertTrue(TestLexer.checkLexeme(""" 0.25 ""","""0.25,<EOF>""",140))
        self.assertTrue(TestLexer.checkLexeme(""" 9.0e3 ""","""9.0e3,<EOF>""",141))
        self.assertTrue(TestLexer.checkLexeme(""" 9.00000e6 ""","""9.00000e6,<EOF>""",142))
        self.assertTrue(TestLexer.checkLexeme(""" .123 """,""".,123,<EOF>""",143))
        self.assertTrue(TestLexer.checkLexeme(""" 0.1e2 ""","""0.1e2,<EOF>""",144))
        self.assertTrue(TestLexer.checkLexeme(""" 9.025e-2 ""","""9.025e-2,<EOF>""",145))
        self.assertTrue(TestLexer.checkLexeme(""" 9.e-10 ""","""9.e-10,<EOF>""",146))
        self.assertTrue(TestLexer.checkLexeme(""" 9000. ""","""9000.,<EOF>""",147))   

    def test_keywords(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme(""" "BreAK" """, """BreAK,<EOF>""",148))
        self.assertTrue(TestLexer.checkLexeme(""" "ConTinue" """, """ConTinue,<EOF>""",149))
        self.assertTrue(TestLexer.checkLexeme(""" "FoR" """, """FoR,<EOF>""", 150))
        self.assertTrue(TestLexer.checkLexeme(""" "TO" """, """TO,<EOF>""", 151))
        self.assertTrue(TestLexer.checkLexeme(""" "DowTO" """, """DowTO,<EOF>""", 152))
        self.assertTrue(TestLexer.checkLexeme(""" "Do" """, """Do,<EOF>""", 153))
        self.assertTrue(TestLexer.checkLexeme(""" "If" """, """If,<EOF>""", 154))
        self.assertTrue(TestLexer.checkLexeme(""" "Then" """, """Then,<EOF>""", 155))
        self.assertTrue(TestLexer.checkLexeme(""" "White" """, """White,<EOF>""", 156))
        self.assertTrue(TestLexer.checkLexeme(""" "Begin" "Function" "End" """, """Begin,Function,End,<EOF>""", 157))
        self.assertTrue(TestLexer.checkLexeme(""" "BEGIN FUNCTION END" """, """BEGIN FUNCTION END,<EOF>""", 158))
        self.assertTrue(TestLexer.checkLexeme(""" "Continue" """, """Continue,<EOF>""", 159))
        self.assertTrue(TestLexer.checkLexeme(""" "Var" """, """Var,<EOF>""", 160))
        self.assertTrue(TestLexer.checkLexeme(""" "EndDo" """, """EndDo,<EOF>""", 161))

    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""**123**""","""<EOF>""",162))
        self.assertTrue(TestLexer.checkLexeme(""" ** abc \n ** abc ""","""abc,<EOF>""",163))
        self.assertTrue(TestLexer.checkLexeme(""" ***abc ** ""","""<EOF>""",164))
        self.assertTrue(TestLexer.checkLexeme(""" *** *** ** ** ""","""*,<EOF>""",165))
        self.assertTrue(TestLexer.checkLexeme(""" **** ""","""<EOF>""",166))
        self.assertTrue(TestLexer.checkLexeme(""" phong **le** ""","""phong,<EOF>""",167))
        self.assertTrue(TestLexer.checkLexeme("""* * 123 * * ""","""*,*,123,*,*,<EOF>""",168))
        self.assertTrue(TestLexer.checkLexeme(""" **123* -*""","""Unterminated Comment""",169))
        self.assertTrue(TestLexer.checkLexeme(""" 12**12**12 ""","""12,12,<EOF>""",170)) 

    def test_whitespace(self):
        """test whitespace"""
        self.assertTrue(TestLexer.checkLexeme("""  \n\t ""","""<EOF>""",171))
        self.assertTrue(TestLexer.checkLexeme(""" \n ""","""<EOF>""",172))
        self.assertTrue(TestLexer.checkLexeme(""" \t ""","""<EOF>""",173))
        self.assertTrue(TestLexer.checkLexeme(""" \r""","""<EOF>""",174))
        self.assertTrue(TestLexer.checkLexeme(""" phong \n le ""","""phong,le,<EOF>""",175))


    def test_string_and_array(self):
        """test string and array"""
        self.assertTrue(TestLexer.checkLexeme(""" "Le Hong Phong" ""","""Le Hong Phong,<EOF>""",176))
        self.assertTrue(TestLexer.checkLexeme(""" "phong \\b le" ""","""phong \\b le,<EOF>""",177))
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\ncd" ""","""Unclosed String: abcd\n""",178))
        self.assertTrue(TestLexer.checkLexeme(""" "phong \\f le" ""","""phong \\f le,<EOF>""",179))
        self.assertTrue(TestLexer.checkLexeme(""" "abcd\tcd" ""","""abcd\tcd,<EOF>""",180))
        self.assertTrue(TestLexer.checkLexeme(""" "phong '"le'" " ""","""phong '"le'" ,<EOF>""",181))
        self.assertTrue(TestLexer.checkLexeme(""" "phong "m" le" ""","""phong ,m, le,<EOF>""",182))
        self.assertTrue(TestLexer.checkLexeme(""" "khoa hoc '" '" " ""","""khoa hoc '" '" ,<EOF>""",183))
        self.assertTrue(TestLexer.checkLexeme(""" {1,2,3} ""","""{1,2,3},<EOF>""",184)) 
        self.assertTrue(TestLexer.checkLexeme(""" {{1,1},{2,2},{3,3}} ""","""{{1,1},{2,2},{3,3}},<EOF>""",185)) 
        self.assertTrue(TestLexer.checkLexeme(""" {1,  2,3   } ""","""{1,2,3},<EOF>""",186)) 
        self.assertTrue(TestLexer.checkLexeme(""" {"a","b","c"} ""","""{a,b,c},<EOF>""",187)) 

    def test_Illegal_Escape_In_String(self):
        """test Illegal Escape In String"""
        self.assertTrue(TestLexer.checkLexeme(""" "phong \\m le" ""","""Illegal Escape In String: phong \\m""",188))
        self.assertTrue(TestLexer.checkLexeme(""" "phong \\a le" ""","""Illegal Escape In String: phong \\a""",189))
        self.assertTrue(TestLexer.checkLexeme(""" "phong \\# le" ""","""Illegal Escape In String: phong \\#""",190))

    def test_unclose_string(self):
        """test unclose_string"""
        self.assertTrue(TestLexer.checkLexeme("""  "le phong ""","""Unclosed String: le phong """,191))
        self.assertTrue(TestLexer.checkLexeme(""" "le phong' ""","""Unclosed String: le phong' """,192))
        self.assertTrue(TestLexer.checkLexeme(""" "le"phong ""","""le,phong,<EOF>""",193))
        self.assertTrue(TestLexer.checkLexeme(""" "le""phong""","""le,Unclosed String: phong""",194))
        self.assertTrue(TestLexer.checkLexeme(""" \"\" \"\"\"  """,""",,Unclosed String:   """,195))

    def test_UNTERMINATED_COMMENT(self):
        """test UNTERMINATED_COMMENT"""
        self.assertTrue(TestLexer.checkLexeme(""" ** khoa hoc * ""","""Unterminated Comment""",196))
        self.assertTrue(TestLexer.checkLexeme(""" ** khoa hoc  ""","""Unterminated Comment""",197))
        self.assertTrue(TestLexer.checkLexeme(""" **khoa* hoc* * ""","""Unterminated Comment""",198))

    def test_free(self):
        """test free"""
        self.assertTrue(TestLexer.checkLexeme(""" int n,m;\n    print >> n >> m;\n ""","""int,n,,,m,;,print,>,>,n,>,>,m,;,<EOF>""",199))

        self.assertTrue(TestLexer.checkLexeme(""" for (double double i = 0; i < n; i ++)\n  ""","""for,(,double,double,i,=,0,;,i,<,n,;,i,+,+,),<EOF>""",200))

        

  

    