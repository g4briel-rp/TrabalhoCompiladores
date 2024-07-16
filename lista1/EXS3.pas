program exs3;

var n1,n2: real;

begin;

 write ("caro usuario este programa mostrara qual dos numeros que voce inseriu e o maior deles");
 write ("para comecar tecle enter");

 write ("por favor digite o primeiro numero e tecle enter ");
 read (n1);

 write ("agora digite o segundo numero e tecle enter ");
 read (n2);

 //primeiro se le os dois numeros que o usuario digitou, então voce faz as 3 condições possiveis, que nesse caso são.
 //o n1 maior que o n2, o contrario desta situação, e ambos os numeros iguais.
 //então so resta digitar os comandos para cada caso.

 if n1 > n2
   then   begin
          write ("o numero maior e , ", n1, ".");
          end;

         else if (n1 < n2)
                then  begin
                      write ("o numero maior e , ", n2, ".");
                      end;

                   else if (n1=n2)
                          then begin
                               write ("os dois numeros sao iguais.");
                               end;


        write (" ");
        write ("para encerrar o programa aperte qualquer tecla.");

end.
