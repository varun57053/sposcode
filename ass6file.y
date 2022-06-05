%{
   #include <stdio.h>
    int yylex();
    int yyerror();
%}

%token TYPE ID SC COMMA NL
%%

start: TYPE varlist SC NL; {printf("statement valid\n"); exit(0);}
varlist : varlist COMMA ID|ID;
%%

void main()
{
	yyparse();
}

int yyerror()
{
	printf("Invalid statement\n");
}

int yywrap()
{
	return 1;
}
