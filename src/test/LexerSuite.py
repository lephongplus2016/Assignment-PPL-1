import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

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

    def test301(self):
        """test301"""
        self.assertTrue(TestLexer.checkLexeme("""#""","""Error Token #""",301))

    def test302(self):
        """test302"""
        self.assertTrue(TestLexer.checkLexeme("""" abc ""","""Unclosed String: " abc """,302))

    def test303(self):
        """test303- add"""
        self.assertTrue(TestLexer.checkLexeme(""" 1+2==3 ""","""1,+,2,==,3,<EOF>""",303))

    def test304(self):
        """test304- UNTERMINATED_COMMENT ---"""
        self.assertTrue(TestLexer.checkLexeme(""" ** lelel lkfkl 123 ""","""Unterminated Comment""",304))   

    def test305(self):
        """test305- UNTERMINATED_COMMENT 2 ---"""
        self.assertTrue(TestLexer.checkLexeme(""" **lelel lkfkl 123 * ""","""Unterminated Comment""",305))       

    def test306(self):
        """test306- COMMENT 2 ---"""
        self.assertTrue(TestLexer.checkLexeme(""" **lelel lkfkl 123
        * dfsdf
        dsfsdfdsf 
         ** ""","""<EOF>""",306))     

    def test307(self):
        """test307"""
        self.assertTrue(TestLexer.checkLexeme(""" {[(12.55; 12.5e-12)]} true ""","""{,[,(,12.55,;,12.5e-12,),],},true,<EOF>""",307))  

    
    def test308(self):
        """test308 """
        self.assertTrue(TestLexer.checkLexeme(""" {1,2,3} {{1,2},{2,3}} """,""" """,308))   

    def test309(self):
        """test309 """
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" """,""" """,309))    