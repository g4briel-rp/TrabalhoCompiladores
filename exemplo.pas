// ignorar esta linha

9. program exemplo;

var op1, op2, op3:integer;
var num:=6789.1234, num2:=2307
begin
    write("Digite o n1.\n");
    read(op1);
    write("Digite o n2.\n");
    read(op2);
    
    write("Digite 1 para soma, 2 para subtracao.\n");
    read(op3);
    
    if op3<>1 then
    begin
        write("a soma eh",op1/op2);
    end;
    if op3=2 then
    begin
        write("a sub eh",op1/op2);
    end;
end.
