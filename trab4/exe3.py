def programa():
    l = [
        ("=", "contador", 'int', 1),
        ("label", "loop", None, None),
        ("call", "print", "Número:", None),
        ("call", "print", None, "contador"),
        ("+", "contador", "contador", 1),
        ("<=", "condicao", "contador", 10),
        ("if", "condicao", "loop", "fim"),
        ('label', 'fim', None, None)
    ]
    return l