/* A Bison parser, made by GNU Bison 2.5.  */

/* Bison interface for Yacc-like parsers in C
   
      Copyright (C) 1984, 1989-1990, 2000-2011 Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     HASHDEFINE = 258,
     NOT = 259,
     CURLY_OPEN = 260,
     CURLY_CLOSE = 261,
     PAR_OPEN = 262,
     PAR_CLOSE = 263,
     SQR_CLOSE = 264,
     IF = 265,
     WHILE = 266,
     CLASS = 267,
     PUBLIC = 268,
     STATIC = 269,
     VOID = 270,
     MAIN = 271,
     STR = 272,
     PRINTLN = 273,
     EXTENDS = 274,
     THIS = 275,
     NEW = 276,
     SEMI_COLON = 277,
     COMMA = 278,
     LENGTH = 279,
     TRUE = 280,
     FALSE = 281,
     NUMBER = 282,
     RET = 283,
     BOOL = 285,
     INT = 286,
     IDENTIFIER = 287,
     ADD = 288,
     SUB = 289,
     MUL = 290,
     DIV = 291,
     MOD = 292,
     BIT_AND = 293,
     LESSTHAN = 294,
     SQR_OPEN = 295,
     DOT = 296,
     ASSIGNMENT = 297,
     ELSE = 298,
     lab1 = 299,
     newlabel = 300,
     label = 301
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 2068 of yacc.c  */
#line 25 "P1.y"

char* str;    



/* Line 2068 of yacc.c  */
#line 102 "P1.tab.h"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


