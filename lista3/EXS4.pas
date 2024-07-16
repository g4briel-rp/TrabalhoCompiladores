program exs4;

var cod,codMenor,codMaior  ,i,  m1,maior,menor, aci, cont: integer;
    mediaVei, mediaAci: real;

begin;

 {Depois de se declarar as variaveis se atribui valores as variaveis que serao
 utilizados posteriormente.}

 maior:=0;
 menor:=10000;
 mediaVei:=0;
 mediaAci:=0;

 {Se cria um la�o de repeti��o para receber os valores e ir se definindo os
 valores finais que ser�o apresentados ao usuario.}

 for i:=1 to 5 do
     begin
     write ("Digite o codigo da cidade.");
     read (cod);
     write ("Digite o numero de veiculos de passeio.");
     read (m1);
     write ("Digite o numero de acidentes de transito.");
     read (aci);

     mediaVei:=mediaVei+m1;

     if ( aci>maior) then
        begin
        maior:=aci;
        codMaior:= cod;
        end;

     if ( aci < menor) then
        begin
        menor:=aci;
        codMenor:= cod;
        end;

     if (m1 < 2000) then
        begin
        mediaAci:= mediaAci+aci;
        cont:=cont+1;
        end;

     end;

  {Se calcula as duas medias e se apresenta os resultados ao usuario.}

  mediaVei:= mediaVei/5;
  mediaAci:= mediaAci/cont;
  write ("A cidade que mais tem acidentes e, ",codMaior ," com ,",maior," acidentes.");
  write ("A cidade que mais tem acidentes e, ",codMenor ," com ,",menor," acidentes.");
  write ("A media da quantidade de veiculos das 5 cidades e de, ",mediaVei ," veiculos.");
  write ("A media de acidentes das cidade que possuem menos que 2000 veiculos de passeio,");
  write ("� de, ", mediaAci ," acidentes.");
  write ("");
  write ("Para encerrar o programa pressione qualquer tecla.");

end.

