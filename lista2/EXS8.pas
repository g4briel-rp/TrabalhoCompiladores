program exs8;

var sal:real;

begin;

 //depois de se coletar as variaveis se apresenta o programa ao usuario.

 write ("caro usuario este programa calculara seu novo salario de acordo com seu salario atual.");
 write ("para comecar tecle enter");

 //entao se le o salario dele para poder calcular de quanto sera o aumento.

 write ("por favor informe seu salario.");
 read (sal);

 {ent�o se caso o salario do usuario for menor ou igual a 300 se da um aumento de 35% a ele caso contrario
  ele recebe somente 15% de aumento.}

  novoSalario:= sal*1.35;
  novoSalario2:= sal*1.15

 if (sal <= 300) then
    begin
    write ("seu novo salario e de ", novoSalario , " .");
    end;

    else if (sal > 300) then
            begin
            write ("seu novo salario e de ", novoSalario2 , " .");
            end;


 write (" ");
 write ("para encerrar o programa precione qualquer tecla.");

end.