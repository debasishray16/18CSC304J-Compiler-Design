%{
#include <stdio.h>
#include <stdlib.h>
#include "P1.tab.h" // Include the token definitions from P1.tab.h
%}

%%
"if"                        { printf("Keyword: %s\n", yytext); return IF; }
"else"                      { printf("Keyword: %s\n", yytext); return ELSE; }
"while"                     { printf("Keyword: %s\n", yytext); return WHILE; }
"class"                     { printf("Keyword: %s\n", yytext); return CLASS; }
"public"                    { printf("Keyword: %s\n", yytext); return PUBLIC; }
"static"                    { printf("Keyword: %s\n", yytext); return STATIC; }
"void"                      { printf("Keyword: %s\n", yytext); return VOID; }
"main"                      { printf("Keyword: %s\n", yytext); return MAIN; }
"String"                    { printf("Keyword: %s\n", yytext); return STR; }
"System.out.println"       { printf("Keyword: %s\n", yytext); return PRINTLN; }
"extends"                   { printf("Keyword: %s\n", yytext); return EXTENDS; }
"this"                      { printf("Keyword: %s\n", yytext); return THIS; }
"new"                       { printf("Keyword: %s\n", yytext); return NEW; }
"length"                    { printf("Keyword: %s\n", yytext); return LENGTH; }
"true"                      { printf("Keyword: %s\n", yytext); return TRUE; }
"false"                     { printf("Keyword: %s\n", yytext); return FALSE; }
"return"                    { printf("Keyword: %s\n", yytext); return RET; }
"boolean"                   { printf("Keyword: %s\n", yytext); return BOOL; }
"int"                       { printf("Keyword: %s\n", yytext); return INT; }
[a-zA-Z][a-zA-Z0-9_]*       { printf("Identifier: %s\n", yytext); return IDENTIFIER; }
[0-9]+                      { printf("Number: %s\n", yytext); return NUMBER; }
"="                         { printf("Operator: %s\n", yytext); return ASSIGNMENT; }
"+"                         { printf("Operator: %s\n", yytext); return ADD; }
"-"                         { printf("Operator: %s\n", yytext); return SUB; }
"*"                         { printf("Operator: %s\n", yytext); return MUL; }
"/"                         { printf("Operator: %s\n", yytext); return DIV; }
"%"                         { printf("Operator: %s\n", yytext); return MOD; }
"!"                         { printf("Operator: %s\n", yytext); return NOT; }
";"                         { printf("Semicolon\n"); return SEMI_COLON; }
","                         { printf("Comma\n"); return COMMA; }
"."                         { printf("Dot\n"); return DOT; }
"("                         { printf("Left Parenthesis\n"); return PAR_OPEN; }
")"                         { printf("Right Parenthesis\n"); return PAR_CLOSE; }
"{"                         { printf("Left Curly Brace\n"); return CURLY_OPEN; }
"}"                         { printf("Right Curly Brace\n"); return CURLY_CLOSE; }
"["                         { printf("Left Square Bracket\n"); return SQR_OPEN; }
"]"                         { printf("Right Square Bracket\n"); return SQR_CLOSE; }
"/*"                        { /* Handle comments */ }
"//"                        { /* Handle comments */ }
[ \t\n]                     ; /* skip whitespace */
.                           { printf("Invalid Character: %s\n", yytext); }
%%

int main() {
    while (yylex() != 0);
    return 0;
}

int yywrap(){
return 1;
}