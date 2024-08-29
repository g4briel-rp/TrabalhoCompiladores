program exs1;

var n1, n2, n3, n4: real;

{n1, n2, n3, n4: integer;
n1, n2, n3, n4: string;}

begin;
    n3 := n1 / (n2 * n4);
    
    {read(n1);
    write("Soma: ", n1);
    for j:=1 to 10 do
    begin
        for i:=10 to 20 do
        begin 
            k:= j + i;
            fat:= fat*k;
            break;
        end;
    end;
    while cont<>qtd do
    begin
        write (n1," ");
        cont:=cont+1;
    end;}
    
    {if (n1 < n2) and (n1 < n3) then
    begin
        write ("O maior numero e ,", n1 , " .");
    end;
    else
    begin
        write ("O maior numero e ", n2 , " .");
    end;}

    while cont<>qtd do
    begin
        write (n1);
        cont:=cont+1;
        if cont=qtd then
            continue;
    end;
end.