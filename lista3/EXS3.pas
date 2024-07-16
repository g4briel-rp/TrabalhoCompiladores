program exs3;

var numero,i,j: integer;
    fat,n:real;

begin;

 {Depois de se declarar as variaveis se da o resumo do programa ao usuario.}

 write ("Caro usuario este programa recebera um numero e lhe mostrara quantos numeros,");
 write ("uma tabela com a fatorial deste valor.");
 write ("para continuar pressione enter.");

 {Ent�o se le o numero para definir ate que numero a fatorial sera calculada.}

 write ("Digite o numero inteiro.");
 read (numero);


  {Ent�o se cria dois la�os para definir a fatorial e a soma desta fatorial.}

   for i:=1 to numero do
       begin


           for j:=1 to i do
                begin
                fat:=1;
                fat:= fat/i;
                end;
       n:= n+fat;
       write (fat);
       end;

 {A unica coisa restante � apresentar os resultados ao usuario.}


  write ("A fatorial do numero,",numero," �, ", n , " .");
  write ("Para encerrar o programa pressione qualquer tecla.");


end.
