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
        Parameter: n, m
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
        Parameter: n, m
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
        Parameter: n, m
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
        Parameter: n, m
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
        Parameter: n, m
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
        Parameter: n, m
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

    def test244_white(self):
        """test 244"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
         Do x= y+1;While(a>1) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test245_white(self):
        """test 245"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
         Do x= y+1;
                Do z= y+1;
                While(a>6) EndDo.
         While(a>1) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test246_white(self):
        """test 246"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
         Do x= y+1;
                Do z= y+1;
                    Do z= y+3;
                    While(a>9) EndDo.
                While(a>6) EndDo.
         While(a>1) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

# for
    def test247_for(self):
        """test 247"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test248_for(self):
        """test 248"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))


    def test249_for(self):
        """test 249"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))


    def test250_for(self):
        """test 250"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            for(i=1,i>6,1) Do x =x +1;
            EndFor.
        EndBody.
        """
        expect = "Error on line 5 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,250))


    def test251_for(self):
        """test 251"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
            EndFor
        EndBody.
        """
        expect = "Error on line 7 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    
    def test252_for(self):
        """test 252"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
                If(a==1) Then a=a+1;
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test253_for(self):
        """test 253"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i!=6,1) Do x =x +1;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test254_for(self):
        """test 254"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
                If(a==1) Then a=a+1;
                EndIf
            EndFor.
        EndBody.
        """
        expect = "Error on line 8 col 12: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test255_for(self):
        """test 255"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
                If(a==1) Then a=a+1
                EndIf.
            EndFor.
        EndBody.
        """
        expect = "Error on line 7 col 16: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test256_for(self):
        """test 256"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
                For(j=1,j>6,1) Do y =y +1;
                
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test257(self):
        """test 257"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
                For(j=1,j>6,1) Do y =y +1;
                Continue;
                EndFor.
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test258(self):
        """test 258"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i>6,1) Do x =x +1;
                For(j=1,j>6,1) Do y =y +1;
                
                EndFor. Continue;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test259(self):
        """test 259"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            Continue;
            For(i=1,i>6,1) Do x =x +1;
                For(j=1,j>6,1) Do y =y +1;
                
                EndFor. 
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test260(self):
        """test 260"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        If (y>2) Then y=6;
        EndIf.
        Continue;
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test261(self):
        """test 261"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; Continue;
        If (y>2) Then y=6;
        EndIf.
        
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test262(self):
        """test 262"""
        input = """
        Var: x,y,z;
        Function: main Parameter: x
        Body:
        If(x>1) Then x = y; 
        If (y>2) Then y=6;
        EndIf.
        Break;
        Else x = z; EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))


    def test263(self):
        """test 249"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1; Break;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test264_for(self):
        """test 264"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1; Return x;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test265_for(self):
        """test 265"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1; Return x =x+1;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test266(self):
        """test 266"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1; Return 99;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test267(self):
        """test 267"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1; Return x=True;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test268(self):
        """test 268"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1; Return x=False;
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test269(self):
        """test 269"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
            For(i=1,i==6,1) Do x =x +1; Return sub(x);
            EndFor.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test270(self):
        """test 270"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
           write("Tinh dien tich hinh chu nhat");
           a=x*y;
           printf(a);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test271(self):
        """test 271"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
           write("Tinh dien tich hinh chu nhat");
           a=x*y;
           printf(a);
           Var: b;
        EndBody.
        """
        expect = "Error on line 8 col 11: Var: "
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test272(self):
        """test 272"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Body:
           write("Tinh dien tich hinh chu nhat");
           a=x*y;
           printf(a);
        EndBody.
        Var: b;
        """
        expect = "Error on line 9 col 8: Var: "
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test273(self):
        """test 273"""
        input = """
        Var: x,y,z;
        Function: main Parameter: a
        Var: b;
        Body:
           write("Tinh dien tich hinh chu nhat");
           a=x*y;
           printf(a);
        EndBody.
        """
        expect = "Error on line 4 col 8: Var: "
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test274(self):
        """test 274"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
          read(a,b,c);
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        Else write("khong la boi so");
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test275(self):
        """test 275"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
          read(a,b,c);
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        Else write("khong la boi so");
        EndIf
        EndBody.
        """
        expect = "Error on line 10 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test276(self):
        """test 276"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
          read(a,b,c);
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        else write("khong la boi so");
        EndIf.
        EndBody.
        """
        expect = "Error on line 8 col 13: write"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test277(self):
        """test 277"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
          read(a,b,c);
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        Elsewrite("khong la boi so");
        EndIf.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test278(self):
        """test 278"""
        input = """
        Var: a,b,c;
        Function: mainParameter: d
        Body:
          read(a,b,c);
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        Else write("khong la boi so");
        EndIf.
        EndBody.
        """
        expect = "Error on line 3 col 31: :"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test279(self):
        """test 279"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
          read(a,b,c);
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        Else write("khong la boi so");
        EndIf.EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test280(self):
        """test 280"""
        input = """
        Var: a,b,c;
        Function main Parameter: d
        Body:
          read(a,b,c);
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        Else write("khong la boi so");
        EndIf.
        EndBody.
        """
        expect = "Error on line 3 col 17: main"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test281(self):
        """test 281"""
        input = """
        Var: a,b,c;
        Function: main 
        Body:
          read(a,b,c);
       
        
        EndBody.

        Function: main2 
        Body:
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        EndIf.
        EndBody.

        Function: main3 
        Body:
        write("khong la boi so");
      
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test282(self):
        """test 282"""
        input = """
        Var: a,b,c;
        Function: main 
        Body:
          read(a,b,c);
        EndBody.

        Function: main2 
        Body:
        If((a*a==1) || (c*c==1)) Then
            write("a=b=c=1");
        EndIf.
        EndBody.

        Function: main3 
        Body:
        write("khong la boi so");
      
        EndBody.
        Function: main3 
        Body: write("khong la boi so");EndBody.
        Function: main4 
        Body: write("khong la boi so");EndBody.
        Function: main5 
        Body: write("khong la boi so");EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test283(self):
        """test 283"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
        s = "hello";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test284(self):
        """test 284"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
        s = "hello" + "world";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test285(self):
        """test 285"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
        s = "True";
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test286(self):
        """test 286"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
        s = foo(x);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test287(self):
        """test 287"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
        s = foo();
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test288(self):
        """test 288"""
        input = """
        Var: a,b,c;
        Function: main Parameter: d
        Body:
        s = foo()+5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test289(self):
        """test 289"""
        input = """
        Var: a,b,c;
        Var: f[2][2];
        Function: main Parameter: d
        Body:
        s = foo()+5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test290(self):
        """test 290"""
        input = """
        Var: a,b,c;
        Var: f[2][2], s="string";
        Function: main Parameter: d
        Body:
        s = foo()+5;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test291(self):
        """test 291"""
        input = """
        Var: a,b,c;
        Var: f[2][2], s="string" ;
        Function: main Parameter: d
        Body:
        s = foo()+5;
        t =True
        EndBody.
        """
        expect = "Error on line 8 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test292(self):
        """test 292"""
        input = """
       Function: test Parameter: k
			Body:
            Var: j;
			
				 j="Integer"+"Integer";
			EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test293(self):
        """test 293"""
        input = """
       Function: test Parameter: k
			Body:
            Var: j;
			For (j=1,n<k,6) Do
				 If (True) Then
				   ElseIf k==n Then 
				   Else test(k+1); 
				  EndIf.
            EndFor.
			EndBody.
        """
        expect = "Error on line 6 col 9: True"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test294(self):
        """test 294"""
        input = """
       Function: test Parameter: k
			Body:
            Var: j;
			For (j=1,n<k,6) Do
				 If (x=True) Then
				   ElseIf k==n Then 
				   Else test(k+1); 
				  EndIf.
            EndFor.
			EndBody.
        """
        expect = "Error on line 6 col 10: ="
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test295(self):
        """test 295"""
        input = """
       Function: test Parameter: k
			Body:
            Var: j;
			For (j=1,n<k,6) Do
				 If (x==True) Then
				   ElseIf k==n Then 
				   Else test(k+1); 
				  EndIf.
            EndFor.
			EndBody.
        """
        expect = "Error on line 6 col 12: True"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test296(self):
        """test 296"""
        input = """
       Function: test Parameter: k
			Body:
            Var: j;
			For (j=1,n<k,6) Do
				 If (x=="test") Then
				   ElseIf k==n Then 
				   Else test(k+1); 
				  EndIf.
            EndFor.
			EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test297(self):
        """test 297"""
        input = """
       Function: test Parameter: k
			Body:Var: j;
			For (j=1,n<k,6) DoIf (x=="test") Then
				   ElseIf k==n Then Else test(k+1); 
				  EndIf.EndFor.EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test298(self):
        """test 298"""
        input = """
       Function: test Parameter: k
			Body:
                exit();
					inc(x);
			EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test299(self):
        """test 299"""
        input = """
       Function: test Parameter: k
			Body:
            write("Press any key when ready ...");
			  read();
			EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    
    def test300(self):
        """test300"""
        input = """
       Function: mysqr Parameter: x
			Body:
				result = sqr(x) - 1;
			EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))