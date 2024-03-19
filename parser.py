import argparse

def main():
    parser = argparse.ArgumentParser(description='Compiler')
    parser.add_argument('filename', help='Path to the file to be compiled')
    args = parser.parse_args()
    return args.filename

def printTokens(tokens):
    for t in tokens:
        print(t)

if __name__ == '__main__':

    caracteres = ['+', '-', '*', '/', '(', ')', ';', ',', '.']
    caracteresEspeciais = ['=', '<', '>', ':']
    duplas = ['<=', '>=', ':=', '==', '<>']    

    operadores_A = ['+', '-', '*', '/', 'mod', 'div']
    operadores_LRA = ['or', 'and', 'not', '==', '<>', '>', '>=', '<', '<=', ':=']
    palavras_reservadas = ['program', 'var', 'integer', 'real', 'string', 'begin', 'end', 'for', 'to', 'while', 'do', 'break', 'continue', 'if', 'else', 'then', 'read', 'write']
    simbolos = [';', ',', '.', ':', '(', ')']

    tipos = {
        'operadores_A': operadores_A,
        'operadores_LRA': operadores_LRA,
        'palavras_reservadas': palavras_reservadas,
        'simbolos': simbolos
    }

    numeroLinha = 1
    tokens = []
    aux = []

    arquivo = open(main(), 'r')

    for linha in arquivo:
        print(f"tamanho da linha: {len(linha)}")
        print(f"linha: {linha}")

        if len(linha) == 1:
            numeroLinha += 1
            continue

        # verifica se o primeiro caractere é uma letra ou espaço (REGRA)
        if linha[0].isalpha():
            aux.append(linha[0])
            i = 1
            while i < len(linha):
                if linha[i].isalnum():
                    aux.append(linha[i])
                elif linha[i] == '"':
                    k = i + 1
                    while(linha[k] != '"'):
                        aux.append(linha[k])
                        k += 1
                    i = k
                    tokens.append(''.join(aux))
                    aux = []
                elif linha[i] in caracteres:
                    if len(aux) > 0:
                        tokens.append(''.join(aux))               
                        aux = []
                    aux.append(linha[i])
                    tokens.append(''.join(aux))
                    aux = []
                elif linha[i] in caracteresEspeciais:
                    tokens.append(''.join(aux))
                    aux = []
                    if linha[i:i+1] in duplas:
                        aux.append(linha[i:i+1])
                        tokens.append(''.join(aux))
                    else:
                        aux.append(linha[i])
                        tokens.append(''.join(aux))
                    aux = []
                elif linha[i].isspace():
                    if len(aux) > 0:
                        tokens.append(''.join(aux))
                        aux = []
                else:
                    print(f"Erro na linha: {numeroLinha}, coluna: {i}")
                    exit()
                i += 1
        elif linha[0].isspace():
            # encontrar a primeira letra
            j = 1
            while linha[j].isspace() and j < len(linha) - 1:
                j += 1
            
            if linha[j].isalpha():
                aux.append(linha[j])
                i = j + 1
                while i != len(linha):
                    if linha[i].isalnum():
                        aux.append(linha[i])
                    elif linha[i] == '"':
                        k = i + 1
                        while(linha[k] != '"'):
                            aux.append(linha[k])
                            k += 1
                        i = k
                        tokens.append(''.join(aux))
                        aux = []
                    elif linha[i] in caracteres:
                        if len(aux) > 0:
                            tokens.append(''.join(aux))               
                            aux = []
                        aux.append(linha[i])
                        tokens.append(''.join(aux))
                        aux = []
                    elif linha[i] in caracteresEspeciais:
                        tokens.append(''.join(aux))
                        aux = []
                        if linha[i:i+1] in duplas:
                            aux.append(linha[i:i+1])
                            tokens.append(''.join(aux))
                        else:
                            aux.append(linha[i])
                            tokens.append(''.join(aux))
                        aux = []
                    elif linha[i].isspace():
                        if len(aux) > 0:
                            tokens.append(''.join(aux))
                            aux = []
                    else:
                        print(f"Erro na linha: {numeroLinha}, coluna: {i}")
                        exit()
                    i += 1
        elif linha[0:1] == '//':
            # comentário vai até o final da linha
            continue
        elif linha[0] == '{':
            # encontrar o fechamento do comentário
            continue
        elif linha[0].isdigit() or linha[0] in tipos['operadores_A'] or linha[0] in tipos['operadores_LRA'] or linha[0] in tipos['simbolos']:
            # retornar erro
            print(f"Erro na linha: {numeroLinha}, coluna: 0")
            break
        
        numeroLinha += 1
    
    # printTokens(tokens)
    print(tokens)

    # tratar o token de acordo com o primeiro caractere identificado
    # testando commit