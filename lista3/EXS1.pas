program exs1;

var   novo: real;
      anoAtual, i: integer;

begin;

 //depois de se declarar as constantes e variaveis se da o resumo do programa ao usuario.

 write ("caro usuario este programa calculara o salario de uma pessoa contratada em 2005 com o salario de 1000$, ");
 write ("e recebendo aumento do dobro do percentual do ano anterior sendo que o primeiro e de 1.5%.");
 write ("para prosseguir tecle enter.");

 //se l� o ano atual para poder ser feita a contagem.

 write ("digite o ano atual.");
 read (anoAtual);

 //se atribui o valor do novo salario.

 novo:= sal*percentual+sal;

 //e na estrutura de repeti��o a cada ano aumentado se aumentar� a porcentagem e consequentemente o salario final.


  for i:=ano to anoAtual do

  begin
  novo:= novo*(percentual*2)+novo;
  end;

  //E ent�o se apresenta o resultado ao usuario.

 write ("novo salario � de , ", novo , " .");
 write (" ");
 write ("para encerrar precione qualquer tecla.");

end.
