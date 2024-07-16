program exs4;

var n1,n2,n3: real;

begin;

 write ("caro usuario este programa recebera tres numeros e os apresentara em ordem crescente");
 write ("para iniciarmos tecle enter.");

 write ("por favor digite o primeiro numero ");
 read (n1);

 write ("agora digite o segundo numero diferente do primeiro ");
 read (n2);

 write ("agora digite o terceiro numero diferente do primeiro e do segundo ");
 read (n3);

 //primeiro se le os 3 numeros que o usuario deseja.
 //então o que deve ser feito é calcular todas as combinações possiveis entre n1,n2,n3 serem diferentes e,
 //escreve-las, e depois disso só e preciso mostrar os resultados.

 if (n1>n2) and (n1>n3) and (n2>n3)
   then  begin write("a ordem crescente desses numeros e ",n1,", ",n2,", ",n3 ,".");
         end;

        else if (n1>n2) and (n1>n3) and (n3>n2)
               then  begin
                     write ("a ordem crescente desses numeros e ", n1,", ",n3 ,", ", n2, ".");
                     end;

                     else if (n2>n1) and (n2>n3) and (n1>n3)
                            then  begin
                                  write ("a ordem crescente desses numeros e ", n2,", ",n1 ,", ", n3, ".");
                                  end;

                                  else if (n2>n1) and (n2>n3) and (n3>n1)
                                         then  begin
                                               write ("a ordem crescente desses numeros e ", n2,", ",n3 ,", ", n1, ".");
                                               end;

                                               else if (n3>n1) and (n3>n2) and (n1>n2)
                                                      then  begin
                                                            write ("a ordem crescente desses numeros e ", n3,", ",n1 ,", ", n2, ".");
                                                            end;

                                                            else if (n3>n1) and (n3>n2) and (n2>n1)
                                                                   then  begin
                                                                         write ("a ordem crescente desses numeros e ", n3,", ",n2 ,", ", n1, ".");
                                                                         end;


 write (" ");
 write ("para encerrar o programa precione qualquer tecla");

end.
