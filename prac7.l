%{  
#include<stdio.h>
int words=1;
int characters=0;
int lines=1 ;   
%}  
                             /*number {digit}+(\.{digit}+)?; */     
%%

["\t" " "] words++;  
\n {lines++;words++;}
. characters++; 
                  
%%
   
int main()
{
	yyin= fopen("sample.txt","r"); 
    yylex();
    printf("\nNo. of words : %d",words);
    printf("\nNo. of characters : %d",characters);
    printf("\nNo. of lines : %d",lines);
     //printf("\nNo. of numbers : %d",number);
      
    printf("\n");
}

int yywrap()
{
	return 1;
}
