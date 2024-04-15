%{
int count = 0;
%}
%%
[A-Z] {printf("%s capital letter\n", yytext);count++;}
.* {printf("%s not a capital letter\n", yytext);}
%%
void main()
{
yylex();
printf("\nNumber of Capital letters in the given input - %d\n", count);
}
int yywrap(){}