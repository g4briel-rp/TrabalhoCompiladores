program exs6;

var n1: integer;

begin;

 //aqui se da o resumo do programa para o usuario

 write ("caro usuario este programa lhe informara se o numero inteiro que voce digitou e par ou impar");
 write ("para comecar tecle enter");

 write ("por favor digite um numero inteiro");
 read (n1);

 //depois se le o numero que ele quer testar e limpa a tela para mostrar o resultado


 // o modo de descobrir se um n�mero � par ou impar � o dividindo por 2.
 // se o resultado for 0 entao o numero � par,caso contrario o numero � impar.
 // a linha acima � o que � nescessario colocar na condi��o para descobrir, depois disto so resta mostrar os resultados ao usuario.

 if (n1)mod(2)=0  then  begin
                      write(n1," e par.");
                      end;

                      else  begin
                            write (n1," e impar.");
                            end;

 write (" ");
 write ("para encerrar o programa aperte qualquer tecla.");

end.
