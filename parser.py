import argparse

def main():
    parser = argparse.ArgumentParser(description='Compiler')
    parser.add_argument('filename', help='Path to the file to be compiled')
    args = parser.parse_args()
    return args.filename

def printLexemas(lexemas):
    for t in lexemas:
        print(t)

def encontraKey(simbolos, value):
    for chave, val in simbolos.items():
        if val == value:
            return chave
    return None

def isVariavel(aux):
    return aux.isalnum()

def isInt(aux):
    return aux.isdigit()

def isFloat(aux):
    return aux.replace('.', '', 1).isdigit()

def isValid(aux):
    if aux[0].isdigit():
        for i in range(1, len(aux)):
            if aux[i].isalpha():
                return False
    return True

if __name__ == '__main__':

    caracteres = ['+', '-', '*', '/', '(', ')', ';', ',', '.']
    caracteresEspeciais = ['=', '<', '>', ':']
    duplas = ['<=', '>=', ':=', '<>']

    simbolos = {
        1: '+',
        2: '-',
        3: '*',
        4: '/',
        5: 'mod',
        6: 'div',
        7: 'or',
        8: 'and',
        9: 'not',
        10: '=',
        11: '<>',
        12: '>',
        13: '>=',
        14: '<',
        15: '<=',
        16: ':=',
        17: 'program',
        18: 'var',
        19: 'integer',
        20: 'real',
        21: 'string',
        22: 'begin',
        23: 'end',
        24: 'for',
        25: 'to',
        26: 'while',
        27: 'do',
        28: 'break',
        29: 'continue',
        30: 'if',
        31: 'else',
        32: 'then',
        33: 'read',
        34: 'write',
        35: ';',
        36: ',',
        37: '.',
        38: ':',
        39: '(',
        40: ')',
    }

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

    numeroLinha = 1
    lexemas = []
    aux = []

    arquivo = open(main(), 'r')

    for linha in arquivo:
        # print(f"tamanho da linha: {len(linha)}")
        # print(f"linha: {linha}")

        if len(linha) == 1:
            numeroLinha += 1
            continue

        i = 0
        while i < len(linha):
            if linha[i].isalnum():
                aux.append(linha[i])
            elif linha[i].isspace():
                if len(aux) > 0:
                    var = ''.join(aux)

                    if isValid(var):
                        value = ''
                        for s in simbolos.keys():
                            if simbolos[s] == var:
                                value = encontraKey(tipos_tokens, s)

                        if value == '' and isInt(var):
                            value = 'tkn_numero_inteiro'
                        elif value == '' and isFloat(var):
                            value = 'tkn_numero_real'
                        elif value == '' and isVariavel(var):
                            value = 'tkn_variavel'

                        lexemas.append((value, var, numeroLinha, i - len(aux)))
                        aux = []
                    else:
                        print(
                            f"Erro na linha: {numeroLinha}, coluna: {i - len(aux)}\nLexema inválido: {var}")
                        exit()
            elif linha[i] in caracteres:
                if linha[i:i+2] == '//':
                    linha = arquivo.readline()
                    numeroLinha += 1
                elif linha[i] == '.' and ''.join(aux).isnumeric():
                    aux.append(linha[i])
                else:
                    if len(aux) > 0:
                        var = ''.join(aux)

                        if isValid(var):
                            value = ''
                            for s in simbolos.keys():
                                if simbolos[s] == var:
                                    value = encontraKey(tipos_tokens, s)

                            if value == '' and isInt(var):
                                value = 'tkn_numero_inteiro'
                            elif value == '' and isFloat(var):
                                value = 'tkn_numero_real'
                            elif value == '' and isVariavel(var):
                                value = 'tkn_variavel'

                            lexemas.append((value, var, numeroLinha, i - len(aux)))
                            aux = []
                        else:
                            print(
                                f"Erro na linha: {numeroLinha}, coluna: {i - len(aux)}\nLexema inválido: {var}")
                            exit()
                    aux.append(linha[i])
                    var = ''.join(aux)
                    value = ''
                    for s in simbolos.keys():
                        if simbolos[s] == var:
                            value = encontraKey(tipos_tokens, s)

                    if value == '' and isInt(var):
                        value = 'tkn_numero_inteiro'
                    elif value == '' and isFloat(var):
                        value = 'tkn_numero_real'
                    elif value == '' and isVariavel(var):
                        value = 'tkn_variavel'

                    lexemas.append((value, var, numeroLinha, i))
                    aux = []
            elif linha[i] in caracteresEspeciais:
                if len(aux) > 0:
                    var = ''.join(aux)

                    if isValid(var):
                        value = ''
                        for s in simbolos.keys():
                            if simbolos[s] == var:
                                value = encontraKey(tipos_tokens, s)

                        if value == '' and isInt(var):
                            value = 'tkn_numero_inteiro'
                        elif value == '' and isFloat(var):
                            value = 'tkn_numero_real'
                        elif value == '' and isVariavel(var):
                            value = 'tkn_variavel'

                        lexemas.append((value, var, numeroLinha, i - len(aux)))
                        aux = []
                    else:
                        print(
                            f"Erro na linha: {numeroLinha}, coluna: {i - len(aux)}\nLexema inválido: {var}")
                        exit()

                d = (''.join(linha[i:i+2]))
                if d in duplas:
                    aux.append(linha[i:i+2])
                    var = ''.join(aux)
                    value = ''
                    for s in simbolos.keys():
                        if simbolos[s] == var:
                            value = encontraKey(tipos_tokens, s)

                    if value == '' and isInt(var):
                        value = 'tkn_numero_inteiro'
                    elif value == '' and isFloat(var):
                        value = 'tkn_numero_real'
                    elif value == '' and isVariavel(var):
                            value = 'tkn_variavel'

                    lexemas.append((value, var, numeroLinha, i))
                    i += 1
                else:
                    aux.append(linha[i])
                    var = ''.join(aux)
                    value = ''
                    for s in simbolos.keys():
                        if simbolos[s] == var:
                            value = encontraKey(tipos_tokens, s)

                    if value == '' and isInt(var):
                        value = 'tkn_numero_inteiro'
                    elif value == '' and isFloat(var):
                        value = 'tkn_numero_real'
                    elif value == '' and isVariavel(var):
                            value = 'tkn_variavel'

                    lexemas.append((value, var, numeroLinha, i))
                aux = []
            elif linha[i] == '"':
                k = i + 1
                while (linha[k] != '"'):
                    aux.append(linha[k])
                    k += 1

                    if k == (len(linha) - 1):
                        linha = arquivo.readline()
                        numeroLinha += 1
                        k = 0
                        if not linha:
                            print(
                                f"Chegou ao final do arquivo sem fechar as aspas, na linha: {numeroLinha}, coluna: {k}")
                            exit()
                i = k
                var = ''.join(aux)
                value = 'tkn_string'
                lexemas.append((value, var, numeroLinha, i - len(aux)))
                aux = []
            elif linha[i] == '{':

                k = i + 1
                while (linha[k] != '}'):
                    k += 1
                    if k == (len(linha)):
                        linha = arquivo.readline()
                        numeroLinha += 1
                        k = 0
                        if not linha:
                            print(
                                f"Chegou ao final do arquivo sem fechar as chaves, na linha: {numeroLinha}, coluna: {k}")
                            exit()
                i = k
            else:
                print(
                    f"Erro na linha: {numeroLinha}, coluna: {i}\nCaractere inválido: {linha[i]}")
                exit()
            i += 1
        numeroLinha += 1

    printLexemas(lexemas)
    # print(lexemas)

    # numero com letras - ok
    # string que nao fecha - ok
    # comentario que nao fecha -> comentario com chaves - ok
