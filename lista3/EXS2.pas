program EXS2;

var n1, i , j, fat: integer;
    e: real;

begin;
 write ("caro usuario este programa recebera um numero inteiro a sua escolha e adicionara a 1 uma fracao ate chegar,");
 write ("no numero escolhido.");
 write ("para prosseguir tecle enter.");
 write ("por favor digite um numero inteiro e positivo.");
 read (n1);

 e:=1;

 for i:=1 to n1 do

    begin
    fat:=1;

     for j:=1 to i do
         begin
         fat:= fat*j;
         end;

       e:= e+1/fat;
     end;

 write ("E igual a ", e , " .");
 write (" ");
 write ("para encerrar o programa precione qualquer tecla.");

end.
