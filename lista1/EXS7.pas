program exs7;

var n1,n2,n3: real;
    I: integer;

begin;

 //aqui se da o resumo do programa pro usuario e o que ele faz

 write ("caro usuario este programa recebera tres numeros a sua escolha");
 write ("e de acordo com sua vontade eles serao apresentados em ordem,");
 write ("crescente, decrescente ou de modo que o maior fica no meio dos dois.");
 write (" ");
 write ("para iniciar tecle enter.");

 // aqui � feita a intera��o com o usuario onde ele digitar� os numeros a serem lidos

 write ("primeiro digite o primeiro numero ");
 read (n1);

 write ("agora digite o segundo numero ");
 read (n2);

 write ("agora digite o terceiro numero ");
 read (n3);

 write ("agora digite o que voce quer que seja feito");
 write (" ");
 write ("digite 1 para os numeros serem apresentados em ordem crescente");
 write ("digite 2 para os numeros serem apresentados em ordem decrescente");
 write ("digite 3 para que o numero maior seja apresentado no meio dos outros dois");
 read (i);

 //agora come�a a primeira cadeia de ifs onde o usuario digita 1 para obter seus numeros em ordem crescente
 //cada cadeia � constituida com 1 condi��o prim�ria, que � o recebimento do que o usuario deseja fazer com os
 //seus numeros digitados.
 //entao quando o programa acha a cadeia que o usuario deseja, ele abre a primeira condi��o da cadeia que pede a condi��o de um numero ser maior que o outro
 //e dentro dela foi colocado outra condi��o para determinar a ordem exata dos numeros a serem apresentados.



 if i=1
   then  begin

       if (n1<n2) and (n1<n3)
         then

              if (n2<n3)
                 then begin
                      write ("a ordem crescente dos numeros e, ", n1, " ,", n2, " ,", n3, " .");
                      end;

                 else begin
                      write ("a ordem crescente dos numeros e, ", n1, " ,", n3, " ,", n2, " .");
                      end;


       if (n2<n1) and (n2<n3)
         then

              if (n1<n3)
                 then begin
                      write ("a ordem crescente dos numeros e, ", n2, " ,", n1, " ,", n3, " .");
                      end;

                 else begin
                      write ("a ordem crescente dos numeros e, ", n2, " ,", n3, " ,", n1, " .");
                      end;


       if (n3<n2) and (n3<n1)
         then

              if (n1<n2)
                 then begin
                      write ("a ordem crescente dos numeros e, ", n3, " ,", n1, " ,", n2, " .");
                      end;

                 else begin
                      write ("a ordem crescente dos numeros e, ", n3, " ,", n2, " ,", n1, " .");
                      end;
         end;

  if i=2
   then  begin

    if (n1>n2) and (n1>n3)
       then

            if (n2>n3)
             then begin
                  write ("a ordem decrescente dos numeros e, ", n1, " ,", n2, " ,", n3, " .");
                  end;

                  else begin
                      write ("a ordem decrescente dos numeros e, ", n1, " ,", n3, " ,", n2, " .");
                      end;


    if (n2>n1) and (n2>n3)
      then

          if (n1>n3)
            then begin
                 write ("a ordem decrescente dos numeros e, ", n2, " ,", n1, " ,", n3, " .");
                 end;

                 else begin
                      write ("a ordem decrescente dos numeros e, ", n2, " ,", n3, " ,", n1, " .");
                      end;


    if (n3>n2) and (n3>n1)
      then

          if (n1>n2)
            then begin
                 write ("a ordem decrescente dos numeros e, ", n3, " ,", n1, " ,", n2, " .");
                 end;

                 else begin
                      write ("a ordem decrescente dos numeros e, ", n3, " ,", n2, " ,", n1, " .");
                      end;
         end;

 //somente para a op��o 3 do usuario que as coisas mudam um pouco aqui voc� so precisa saber qual o numero maior entao
 //basta fazer 3 condi��es, na qual o programa achar a condi��o verdadeira, so resta dar o tratamento para o usuario.

 if i=3
   then  begin

         if (n1>n2) and (n1>n3)
           then begin
                write ("a ordem desejada dos numeros e, ", n2, " ,", n1, " ,", n3, " .");
                end;

         if (n2>n1) and (n2>n3)
           then begin
                write ("a ordem desejada dos numeros e, ", n1, " ,", n2, " ,", n3, " .");
                end;

         if (n3>n2) and (n3>n1)
           then begin
                write ("a ordem desejada dos numeros e, ", n1, " ,", n3, " ,", n2, " .");
                end;

         end;


  write (" ");
  write ("para encerrar o programa aperte qualquer tecla.");


end.
