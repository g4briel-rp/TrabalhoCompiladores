program exs8;

var n1,n2,n3,n4: real;

begin;

 //primeiramente se da o resumo do que o programa far� para o usuario.
 //e depois j� se manda ele digitar as variaveis que ser�o utilizadas.

 write ("caro usuario este programa recebera dois numeros e te dara opcoes sobre o que   fazer com eles.");
 write ("para continuar precione enter.");

 write ("por favor digite o primeiro numero");
 read (n1);

 write ("por favor digite o segundo numero");
 read (n2);

 //se da as op��es para o usuario escolher o que deseja ser feito a principio.

 write ("tecle 1 para somar os dois numeros.");
 write ("tecle 2 para calcular a raiz quadrada de um numero.");
 read (n3);

 //agora come�a uma pequena cadeia de ifs para determinar o que fazer caso o usuario digite 2.
 //se l� o valor que ele quer e apresenta-se o resultado a ele.

 if n3=2 then begin
              write ("precione 1 para a raiz quadrada do primeiro numero.");
              write ("precione 2 para a raiz quadrada do segundo numero.");   
              read (n4);
              end;

 //aqui � a outra parte da cadeia de if caso ele digite 1 para a variavel n4 se calcula a raiz quadrada de n1.
 //poderia ser utilizado somente um else, porem se fosse feito desse jeito qualquer valor que o usuario digitasse cairia no else.
 //por isso se abre outra condi��o para caso do usuario digitar um valor que n�o seja 2 o programa se encerra e assim ele tem que recome�ar.

 if n4=1 then begin
              write ("a raiz quadrada do primeiro numero e ", raiz1, " .");
              end;

              else if n4=2 then begin
                                write ("a raiz quadrada do segundo numero e ", raiz2, " .");
                                end;



 //aqui est� a condi��o para o n3 ser 1.
 //so basta apresentar pro usuario a soma dos dois numeros.

 soma:= n1+n2;

 if  n3=1 then begin
               write ("o resultados da soma dos numeros e ",soma," .");
               end;


 write (" ");
 write ("para encerrar o programa precione qualquer tecla");

end.




