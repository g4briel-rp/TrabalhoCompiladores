import argparse

def main():
    parser = argparse.ArgumentParser(description='Compiler')
    parser.add_argument('filename', help='Path to the file to be compiled')
    args = parser.parse_args()
    return args.filename

if __name__ == '__main__':
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

    tokens = []
    aux = []

    arquivo = open(main(), 'r')

    for linha in arquivo:
        print(f"tamanho da linha: {len(linha)}")
        for i in range(0, len(linha)):
            print(f"letra: {linha[i]}")
            if linha[i] != ' ' and linha[i] != '\n' and linha[i] != '\t' and linha[i] != '\r':
                aux.append(linha[i])
            else:
                if aux != []:
                    aux_str = ''.join(aux)
                    tokens.append(aux_str)
                    aux = []
    
    print(tokens)

    # tratar o token de acordo com o primeiro caractere identificado
    # testando commit