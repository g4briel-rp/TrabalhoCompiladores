import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Compiler')
    parser.add_argument('filename', help='Path to the file to be compiled')
    args = parser.parse_args()
    return args.filename

def classifica(simbolos, var, value):

    if var in simbolos.values():
        for s in simbolos.keys():
            if simbolos[s] == var:
                value = s
    elif value == None and isInt(var):
        value = 42
    elif value == None and isFloat(var):
        value = 43
    elif value == None and isVariavel(var):
        value = 41

    return value

def imprime(lexemas):
    for t in lexemas:
        print(t)

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

def erroLexema(numeroLinha, i, aux, var):
    print(
        f"Erro na linha: {numeroLinha}, coluna: {(i - len(aux) + 1)}\nLexema inválido: {var}")
    exit()

def executar():

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

    numeroLinha = 1
    lexemas = []
    aux = []

    arquivo = open(main(), 'r')

    for linha in arquivo:
        if len(linha) == 1:
            numeroLinha += 1
            continue
        i = 0
        while i < len(linha):
            # vai armazenando em aux todo caractere alphanumérico até achar um separador
            if linha[i].isalnum(): 
                aux.append(linha[i])
            # se o separador for um espaço
            elif linha[i].isspace(): 
                if len(aux) > 0:
                    var = ''.join(aux)
                    if isValid(var):
                        value = None
                        value = classifica(simbolos, var, value)
                        # se o número for float e terminar com '.', concatenar o 0
                        if value == 43 and var[len(var)-1] == '.':
                            var += '0'
                        lexemas.append((value, var, numeroLinha, (i - len(aux) + 1)))
                        aux = []
                    else:
                       erroLexema(numeroLinha, i, aux, var)
            elif linha[i] in caracteres:
                if linha[i:i+2] == '//':
                    linha = arquivo.readline()
                    numeroLinha += 1
                elif linha[i] == '.' and ''.join(aux).isnumeric():
                    aux.append(linha[i])
                    
                else:
                    if len(aux) > 0:
                        var = ''.join(aux)
                        # print('valor de var: ',var)
                        
                        # veririca se o que está se formando é válido
                        if isValid(var):
                            value = None
                            value = classifica(simbolos, var, value)
                            # print('valor da classificação: ',value)
                            if value == 43 and var[len(var)-1] == '.':
                                var += 0
                            lexemas.append((value, var, numeroLinha, (i - len(aux) + 1)))
                            aux = []
                        else:
                            erroLexema(numeroLinha, i, aux, var)
                    aux.append(linha[i])
                    var = ''.join(aux)
                    value = None
                    value = classifica(simbolos, var, value)
                    lexemas.append((value, var, numeroLinha, i + 1))
                    aux = []
            elif linha[i] in caracteresEspeciais:
                if len(aux) > 0:
                    var = ''.join(aux)
                    if isValid(var):
                        value = None
                        value = classifica(simbolos, var, value)
                        lexemas.append((value, var, numeroLinha, (i - len(aux) + 1)))
                        aux = []
                    else:
                       erroLexema(numeroLinha, i, aux, var)
                d = (''.join(linha[i:i+2]))
                if d in duplas:
                    aux.append(linha[i:i+2])
                    var = ''.join(aux)
                    value = None
                    value = classifica(simbolos, var, value)
                    lexemas.append((value, var, numeroLinha, i + 1))
                    i += 1
                else:
                    aux.append(linha[i])
                    var = ''.join(aux)
                    value = None
                    value = classifica(simbolos, var, value)
                    lexemas.append((value, var, numeroLinha, i + 1))
                aux = []
            elif linha[i] == '"':
                linhaErro = numeroLinha
                k = i + 1
                colunaErro = k
                while (linha[k] != '"'):
                    aux.append(linha[k])
                    k += 1
                    if k == (len(linha) - 1):
                        linha = arquivo.readline()
                        numeroLinha += 1
                        k = 0
                        if not linha:
                            print(
                                f"Chegou ao final do arquivo sem fechar as aspas, na linha: {linhaErro}, coluna: {colunaErro}")
                            exit()
                i = k
                var = ''.join(aux)
                value = 44

                if '\\n' in var:
                    var = re.sub(r'\\n', '\n', var)
                elif '\\t' in var:
                    var = re.sub(r'\\t', '    ', var)
                
                lexemas.append((value, var, numeroLinha, (i - len(aux) + 1)))
                aux = []
            elif linha[i] == '{':
                linhaErro = numeroLinha
                k = i + 1
                colunaErro = k
                while (linha[k] != '}'):
                    k += 1
                    if k == (len(linha)):
                        linha = arquivo.readline()
                        numeroLinha += 1
                        k = 0
                        if not linha:
                            print(
                                f"Chegou ao final do arquivo sem fechar as chaves, na linha: {linhaErro}, coluna: {colunaErro}")
                            exit()
                i = k
            else:
                print(
                    f"Erro na linha: {numeroLinha}, coluna: {i}\nCaractere inválido: {linha[i]}")
                exit()
            i += 1
        numeroLinha += 1
    # printLexemas(lexemas)
    return lexemas