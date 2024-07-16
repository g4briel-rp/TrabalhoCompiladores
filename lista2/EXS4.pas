program exs4;

var n1,n2,n3: real;

begin;

 //depois de se declarar as variaveis, se l� os numeros do usuario.

 write ("caro usuario este programa recebera 3 numeros e lhe dira qual o maior deles.");
 write ("para continuar precione qualquer tecla.");

 write ("por favor digite o primeiro numero.");
 read (n1);

 write ("digite o segundo numero diferente do primeiro.");
 read (n2);

 write ("agora digite o terceiro numero diferente dos outros 2.");
 read (n3);

 {se faz uma cadeia de ifs como condi��o um numero maior que os outros dois.
  E se apresenta ao usuario os resultados.}

 if (n1 < n2) and (n1 < n3) then
    begin
    write ("O maior numero e ,", n1 , " .");
    end;

    else if (n2 < n1) and (n2 < n3) then
            begin
            write ("O maior numero e ", n2 , " .");
            end;

            else if (n3 < n1) and (n3 < n2) then
                    begin
                    write ("O maior numero e ,", n3 , " .");
                    end;

                    else begin
                         write ("Os numeros nao atenderam as condicoes exigidas.");
                         end;

 write (" ");
 write ("Para encerrar o programa precione qualquer tecla.");

end.