program exs8;

var n1,n2,n3,i,qtd,cont: integer;

begin;

 {Depois de se declarar as variaveis se le a quantidade de numeros que o usuario
 deseja e se le os 3 numeros.}

 write ("Digite a quantidade de numeros voc� deseja ter na sequencia.");
 read (qtd);
 write ("Digite o primeiro numero.");
 read (n1);
 write ("Digite o segundo numero.");
 read (n2);
 write ("Digite o terceiro numero.");
 read (n3);


 {Se coloca em um la�o de repeti��o para ir escrevendo os valores de acordo
 com regras ja estabelicidas e vai se multiplicando esses valores. Se coloca
 comandos break no meio do la�o por que se por acaso o contador ficar igual a
 quantidade de termos que o usuario deseja no meio do la�o ele n�o ira parar
 ate a checagem inicial.}

 while cont<>qtd do
      begin
      write (n1," ");
      n1:=n1*2;
      cont:=cont+1;

      if cont=qtd then
         break;

      write (n2," ");
      n2:=n2*3;
      cont:=cont+1;

      if cont=qtd then
         break;

      write (n3," ");
      n3:=n3*4;
      cont:=cont+1;
      end;

write ("");
write ("");
write ("Para encerrar o programa pressione qualquer tecla.");

end.
