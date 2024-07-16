program exs7;

var i,j,soma,aux: integer;

begin;

 {Se declara as variaveis para realizar os calculos.}

 write ("Fibbonaci.");

 {Atribui-se os valores para a soma=0 e para o aux=1}

 soma:=0;
 aux:=1;

 {� nescessario apresentar os resultados antes de se realizar os calculos}

 for i:=1 to 6 do
     begin

          write (soma);
          write (aux);
          soma:=soma+aux;

               {Quando se faz um outro la�o dentro do primeiro com condi��o
               de parada a soma do ultimo numero se define a soma dos dois
               e eles sempre v�o se acrescentando e assim se faz o fibonacci.}

               for j:=1 to soma do
               begin
               aux:=aux+1;
               end;


     end;

end.
