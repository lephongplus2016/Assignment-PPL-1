# Assignment-PPL-main
## Introduce
After completing this assignment, you will be able to
* define formally lexicon of a programming language.
* use ANTLR to implement a lexer for a programming language.
* define formally grammar of a programming language.
* use ANTLR to implement a recognizer for a programming language.
## Specification
Need to install antlr for this ass:
* Download antlr-4.8-complete.jar from [this](https://www.antlr.org/download.html), set the environment variable ANTLR_JAR to this file; 

* Install antlr4-python3-runtime (see instructions in section Python Targets of the above webpage).


* Install Python 3 if you have not installed it yet.

* Download initial.zip and unzip it.
To run:
```
python run.py gen
python run.py test LexerSuite
python run.py test ParserSuite
```
## Hint 
To complete this assignment, you need to:
* read carefully the specification of language
* Modify BKIT.g4. in the initial code to describe formally BKIT language.Please fill
in your id in the header of this file.
* Add more test in LexerSuite and ParserSuite in the initial code.
This assignment is divided two phases: lexer phase and recognizer phase. These phases
are assessed independently.
