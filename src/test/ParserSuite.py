import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "Error on line 1 col 7: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test203(self):
        """tesst 203"""
        input = """Var: x,y,z; Function: haha
        Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test204(self):
        """test 204"""
        input = """Var: x;

 Function: fact
    Parameter: n
    Body: 
       If n==0 Then 
       Return 1;
         Else
        Return n*fact(n-1);
         EndIf.
         EndBody.
 Function: main
     Body:
         x=10;
       fact(x);
                EndBody. """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test205(self):
        """test 205"""
        input = """Function: main
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test206(self):
        """test 206"""
        input = """Function: main
        Body:
        Parameter: n
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test206(self):
        """test 206"""
        input = """Function: main
        Body:
        Parameter: n;
        printf("Hello");
        EndBody.
        """
        expect = "Error on line 3 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test207(self):
        """test 207"""
        input = """
        Var: x;
        Function: main
        Parameter: n
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test208(self):
        """test 208"""
        input = """
        Var: x,y=5;
        Function: main
        Parameter: n
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test209(self):
        """test 209"""
        input = """
        Var: x,y=5, a[12];
        Function: main
        Parameter: n
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test210(self):
        """test 210"""
        input = """
        Var: x,y=5;
        Function: main
        Parameter: n, m=5
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test211(self):
        """test 211"""
        input = """
        Var: x,y=5;
        Function: main
        Parameter: n, m=5
        Body:
        Var: i,j;
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test212(self):
        """test 212"""
        input = """
        Var: x,y=5;
        Function: main
        Parameter: n, m=5
        Var: i,j;
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "Error on line 5 col 8: Var: "
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test213(self):
        """test 213 variable first in body"""
        input = """
        Var: x,y=5;
        Function: main
        Parameter: n, m=5
        Body:
        printf("Hello");
        Var: i,j;
        EndBody.
        """
        expect = "Error on line 7 col 8: Var: "
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test214(self):
        """test 214"""
        input = """
        Var: x,y=5, s="phongle";
        Function: main
        Parameter: n, m=5
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test215(self):
        """test 21"""
        input = """
        Var: x=1.25, y= "True";
        Function: main
        Parameter: n, m=5
        Body:
        printf("Hello");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test216_expression(self):
        """test 216 expression"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
        printf("Hello");
        x=y+z;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test217(self):
        """test 217"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
        printf("Hello");
        x=3*5+4*6;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test218(self):
        """test 218"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
        printf("Hello");
        x=3*(5+4)*6;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test219(self):
        """test 219"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
        printf("Hello");
        x=3*5+4*-6;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test220(self):
        """test 220"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
        printf("Hello");
        x=3*(5+4)*-6;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test221(self):
        """test 221"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
        printf("Hello");
        3=1;
        EndBody.
        """
        expect = "Error on line 6 col 8: 3"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test222(self):
        """test 222"""
        input = """
        Var: x,y,z;
        Function: main
        Body:
        printf("Hello");
        3=x;
        EndBody.
        """
        expect = "Error on line 6 col 8: 3"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test223(self):
        """test 223"""
        input = """
        Var: x,y,z;
        Function: sub
        Parameter: x
        Body:
        printf("x");
        x=x-1;
        sub(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test224(self):
        """test 224"""
        input = """
        Var: x,y,z;
        Function: sub
        Parameter: x
        Body:
        printf("x");
        x=x-1;
        sub(x)=1;
        EndBody.
        """
        expect = "Error on line 8 col 14: ="
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test225(self):
        """test 225"""
        input = """
        Var: x,y,z;
        Function: sub
        Parameter: x
        Body:
        printf("x");
        x=x-1;
        y = sub(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test226(self):
        """test 226"""
        input = """
        Var: x,y={4,5,6},z;
        Function: sub
        Parameter: x
        Body:
        printf("x");
        x=x-1;
        y[1] = sub(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test227(self):
        """test 227"""
        input = """
        Var: x,y={4,5,6},z;
        Function: sub
        Parameter: x
        Body:
        printf("x");
        x=x-1 = y[1] = sub(x);
        EndBody.
        """
        expect = "Error on line 7 col 14: ="
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test228_if(self):
        """test 228 if"""
        input = """
        Var: x,y,z;
        Function: main
        Parameter: x
        Body:
        printf("x");
        If(x>1) Then x = y; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test229_if(self):
        """test 229 if"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        if(x>1) then x = y; EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 21: x"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test230_if_else(self):
        """test 230 if-else"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))


    def test231_if_else(self):
        """test 231 if-else"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        ElseIf x==1 Then x= x+1;
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test232_if(self):
        """test 232 if"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        if(x=1) then x = y; EndIf.
        EndBody.
        """
        expect = "Error on line 5 col 12: ="
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test233_if_else(self):
        """test 233 if-else"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        ElseIf x!=1 Then x= x+1;
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))    


    def test234_if_else(self):
        """test 234 if-else"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        ElseIf x>=1 Then x= x+1;
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test235_if_else(self):
        """test 235 if-else"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        ElseIf x>=. 1.25 Then x= x+1;
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test236_if_else(self):
        """test 236 if-else"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        ElseIf x>=. 1.25 Then x= x+1;
        Else sub(x); EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test237_if_in_if(self):
        """test 234 if-in if"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        If (y>2) Then y=6;
        EndIf.
        
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    # white
    def test238_white(self):
        """test 238"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
        While(a>1) Do EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test239_white(self):
        """test 239"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
        While(a>1) Do 123; EndWhile.
        EndBody.
        """
        expect = "Error on line 5 col 22: 123"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test240_white(self):
        """test 240"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
        While(a>1) Do abc EndWhile.
        EndBody.
        """
        expect = "Error on line 5 col 26: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test241_white(self):
        """test 241"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
        While(a>1) Do x= y+1; EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test242_white(self):
        """test 242"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
        While(a>1) Do x= y+1;
            While(x>1) Do x= y+2;
        
            EndWhile.
         EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test243_white(self):
        """test 243"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
        While(a>1) Do x= y+1;
            While(x>1) Do x= y+2;
                While(y>1) Do x= y+3;
        
                EndWhile.
            EndWhile.
         EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))




















