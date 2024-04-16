program exs1;

var n1,n2,n3,n4,media :real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 write ("Caro usuario este programa recebera quatro notas suas e lhe mostrara sua media aritimetica.");
 write ("para prosseguir tecle enter.");

 //se le os 4 valores para calcular a media.

 write("por favor digite a primeira nota.");
 read (n1);

 write ("por favor digite a segunda nota.");
 read (n2);

 write ("por favor digite a terceira nota.");
 read (n3);

 write ("por favor digite a quarta nota.");
 read (n4);


 media:= (n1+n2+n3+n4)/3;

 //se calcula a media e manda o resultado ao usuario.

 write ("Sua media aritimetica e ", media, " .");

 //e se finaliza com uma cadeia de ifs para exibir a mensagem de aprova��o ou reprova��o.

 if (media < 7) then
    begin
    write ("Caro usuario voce foi reprovado.");
    end;

    else if (media >= 7) then
            begin
            write ("Caro usuario voce foi aprovado.");
            end;

 write ("  ");
 write ("para encerrar precione qualquer tecla.");

end.