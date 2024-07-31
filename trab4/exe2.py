def programa():
    l = [
        ("call", "print", "Digite a primeira nota: ", None),
        ("call", "scan", "nota1", "float"),
        ("call", "print", "Digite a segunda nota: ", None),
        ("call", "scan", "nota2", "float"),
        ("call", "print", "Digite a terceira nota: ", None),
        ("call", "scan", "nota3", "float"),
        ("+", "soma", "nota1", "nota2"),
        ("+", "soma", "soma", "nota3"),
        ("/", "media", "soma", 3),
        (">=", "aprovado", "media", 6),
        ("if", "aprovado", "aprovado", "reprovado"),
        ("label", "aprovado", None, None),
        ("call", "print", "Aluno aprovado.", None),
        ("jump", "fim", None, None),
        ("label", "reprovado", None, None),
        ("call", "print", "Aluno reprovado.", None),
        ("label", "fim", None, None)
    ]
    return l