program EXS2;

var n1,n2,media :real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 write ("caro usuario este programa recebera duas notas suas calculara a media aritimetica delas,");
 write ("entao lhe mostrara se voce foi aprovado ou reprovado.");
 write ("para comecar tecle enter.");

 //entao se le as variaveis para fazer a media de nota.

 write ("por favor digite a primeira nota.");
 read (n1);

 write ("agora digite a segunda nota.");
 read (n2);


 media:= (n1+ n2)/2;

   {ent�o antes de se come�ar a cadeia de ifs para apresentar a mensagem ao usuario
   se mostra a media aritimetica dele}

 write ("Sua media aritimetica e ", media, " .");

 //ent�o se faz uma pequena cadeia de ifs para definir a mensagem apresentada ao usuario.

 if (media >= 7) and (media <= 10) then
    begin
    write ("Voce foi aprovado!!!");
    end;

    else if (media < 7) and (media >= 4) then
            begin
            write ("Voce tera que fazer o exame.");
            end;

            else if (media < 4) and (media >= 0) then
                    begin
                    write ("Voce foi reprovado.");
                    end;

 write (" ");
 write ("para encerrar o programa precione qualquer tecla.");

end.