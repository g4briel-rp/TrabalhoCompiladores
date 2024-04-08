import parserTP01_att as parser

tipos_tokens = {
    'tkn_add': 1,
    'tkn_sub': 2,
    'tkn_mult': 3,
    'tkn_divisao': 4,
    'tkn_mod': 5,
    'tkn_div': 6,
    'tkn_or': 7,
    'tkn_and': 8,
    'tkn_not': 9,
    'tkn_igual': 10,
    'tkn_dif': 11,
    'tkn_maior': 12,
    'tkn_maior_igual': 13,
    'tkn_menor': 14,
    'tkn_menor_igual': 15,
    'tkn_atrib': 16,
    'tkn_program': 17,
    'tkn_var': 18,
    'tkn_integer': 19,
    'tkn_real': 20,
    'tkn_string': 21,
    'tkn_begin': 22,
    'tkn_end': 23,
    'tkn_for': 24,
    'tkn_to': 25,
    'tkn_while': 26,
    'tkn_do': 27,
    'tkn_break': 28,
    'tkn_continue': 29,
    'tkn_if': 30,
    'tkn_else': 31,
    'tkn_then': 32,
    'tkn_read': 33,
    'tkn_write': 34,
    'tkn_ponto_virgula': 35,
    'tkn_virgula': 36,
    'tkn_ponto': 37,
    'tkn_dois_pontos': 38,
    'tkn_abre_parenteses': 39,
    'tkn_fecha_parenteses': 40,
    'tkn_variavel': 41,
    'tkn_numero_inteiro': 42,
    'tkn_numero_real': 43,
    'tkn_string': 44,
}

def function():
    consome('tkn_program')
    pass

def declarations():
    pass

def consome(arg1, lista):
    pass

if __name__ == '__main__':
    lista = parser.executar()

    parser.imprime(lista)