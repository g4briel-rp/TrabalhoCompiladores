def programa():
    l = [
        ("call", "print", "Digite a medida do lado A: ", None),
        ("call", "scan", "a", "float"),
        ("call", "print", "Digite a medida do lado B: ", None),
        ("call", "scan", "b", "float"),
        ("call", "print", "Digite a medida do lado C: ", None),
        ("call", "scan", "c", "float"),
        ("+", "sum1", "a", "b"),
        (">", "gt1", "sum1", "c"),
        ("+", "sum2", "a", "c"),
        (">", "gt2", "sum2", "b"),
        ("+", "sum3", "b", "c"),
        (">", "gt3", "sum3", "a"),
        ("&&", "temp4", "gt1", "gt2"),
        ("&&", "temp5", "temp4", "gt3"),
        ("if", "temp5", "triangulo", "nao_tri"),
        ("label", "triangulo", None, None),
        ("call", "print", "É possível formar um triângulo.", None),
        ("jump", "fim", None, None),
        ("label", "nao_tri", None, None),
        ("call", "print", "Não é possível formar um triângulo.", None),
        ("label", "fim", None, None)
    ]
    return l