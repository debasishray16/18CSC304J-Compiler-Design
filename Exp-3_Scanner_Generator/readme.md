FAQ: 
0. On which system should the assignments be done?
Ideally on a linux box. If you only have a Windows machine, try installing
cygwin.

1. How to identify the lexical tokens?
Look at the minijava.html and also see the sample programs.

2. How to compile? 

The code will be compiled and run on the command line only. Open a
terminal, change-directory to the folder in which the files are there and
execute the following commands:

$ flex P1.l
$ gcc lex.yy.c -lfl -o P1
or
$ gcc lex.yy.c -ll -o P1

3. How to run?

$ ./P1 

4. How can I test against testcases:

Example:
./P1 < programs/Fibonacci.java
