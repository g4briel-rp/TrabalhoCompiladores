program exs3;

var n1,n2: real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 write ("caro usuario este programa recebera dois numeros e lhe dira qual o menor.");
 write ("para comecar tecle enter.");

 //entao se le as notas que ele vai digitar.

 write ("por favor digite o primeiro numero.");
 read (n1);

 write ("agora digite o segundo numero.");
 read (n2);


 //ent�o na cadeia de ifs se apresenta qual o numero � o maior.

 if (n1 > n2) then
    begin
    write ("o numero menor e ", n2 , " .");
    end;

    else if (n2 > n1) then
            begin
            write ("o numero menor e ", n1 , " .");
            end;

            else if (n1 = n2) then
                    begin
                    write ("os dois numeros sao iguais.");
                    end;

 write (" ");
 write ("para encerrar o programa precione qualquer tecla.");

end.
