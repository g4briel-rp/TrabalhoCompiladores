program exs10;

var preco, imp, dis : real;

begin;

 //depois de se declarar as variaveis se apresenta ao usuario o resumo do programa.

 write ("caro usuario este programa recebera o valor de custo de um carro e te retornara os valores do,");
 write ("imposto, da porcentagem do distribuidor e o valor final.");
 write ("para prosseguir tecle enter.");

 //entao se coleta o preco do carro para definir o valor do imposto e lucro do distribuidor.

 write ("primeiramente digite o valor de preco de custo do carro.");
 read (preco);


 {se faz uma cadeia de ifs para atribuir o valor do imposto e do lucro do distribuidor a variaveis declaradas acima.}

 if (preco <= 12000) then
    begin
    imp:= preco*0;
    dis:= preco*0.05;
    end;

    else if (preco > 12000) and (preco <= 25000) then
            begin
            imp:= preco*0.15;
            dis:= preco*0.10;
            end;

            else if (preco > 25000) then
                    begin
                    imp:= preco*0.20;
                    dis:= preco*0.15;
                    end;


   //ent�o so resta mostrar ao usuario os resultados.

   precoFinal:= preco+imp+dis;

  write ("caro usuario o valor do imposto e de ", imp , " .");
  write ("o valor do lucro do distribuidor e de ", dis , " .");
  write ("o preco final do carro e de ", precoFinal , " .");
  write (" ");
  write ("para encerrar o programa precione qualquer tecla");


end.
