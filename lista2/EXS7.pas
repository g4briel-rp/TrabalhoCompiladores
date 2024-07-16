program exs7;

var n1: real;

begin;

 //depois de se declarar as variaveis se apresenta o resumo do programa ao usuario.

 write ("caro usuario este programa calculara seu aumento e caso voce nao for o receber te mostrara uma mensagem.");
 write ("para come�ar precione enter.");

 //se coleta a variavel do salario para se fazer a condicional.

 write ("por favor informe o seu salario.");
 read (n1);

   {ent�o se faz uma condi��o para que se o salario for maior que 500 entao se recebe 30% de aumento caso contrario
   se mostra a mensagem ao usuario que ele nao tem direito a aumento}

   result:= n1*1.30;

 if (n1 < 500) then
    begin
    write ("seu novo salario e de ", result , " .");
    end;

    else if (n1 >= 500 ) then
            begin
            write ("caro usuario voce tem direito a aumento.");
            end;

 write (" ");
 write ("para encerrar o programa precione qualquer tecla.");

end.