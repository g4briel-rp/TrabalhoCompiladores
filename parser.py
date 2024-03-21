import argparse

def main():
    parser = argparse.ArgumentParser(description='Compiler')
    parser.add_argument('filename', help='Path to the file to be compiled')
    args = parser.parse_args()
    return args.filename

def printLexemas(lexemas):
    for t in lexemas:
        print(t)

if __name__ == '__main__':

    caracteres = ['+', '-', '*', '/', '(', ')', ';', ',', '.']
    caracteresEspeciais = ['=', '<', '>', ':']
    duplas = ['<=', '>=', ':=', '==', '<>']    

    tipos = {
        'tkn_add': 1,
        'tkn_sub': 2,
        'tkn_mult': 3,
        'tkn_div': 4,
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
                    lexemas.append((''.join(aux), numeroLinha, i - len(aux)))
                    aux = []
                    # subir o while para encontrar a primeiro caractere
            elif linha[i] in caracteres:
                if len(aux) > 0:
                    lexemas.append((''.join(aux), numeroLinha, i - len(aux)))           
                    aux = []
                aux.append(linha[i])
                lexemas.append((''.join(aux), numeroLinha, i))
                aux = []
            elif linha[i] in caracteresEspeciais:
                if len(aux) > 0:
                    lexemas.append((''.join(aux), numeroLinha, i - len(aux)))         
                    aux = []
                
                d = (''.join(linha[i:i+2]))
                if d in duplas:
                    aux.append(linha[i:i+2])
                    lexemas.append((''.join(aux), numeroLinha, i))
                    i += 1
                else:
                    aux.append(linha[i])
                    lexemas.append((''.join(aux), numeroLinha, i))
                aux = []
            elif linha[i] == '"':
                k = i + 1
                while(linha[k] != '"'):
                    aux.append(linha[k])
                    k += 1

                    if k == (len(linha) - 1):
                        linha = arquivo.readline()
                        numeroLinha += 1
                        k = 0 
                        if not linha:
                            print(f"Chegou ao final do arquivo sem fechar as aspas na linha: {numeroLinha}, coluna: {k}")
                            break    
                i = k
                lexemas.append((''.join(aux), numeroLinha, i - len(aux)))
                aux = []
            else:
                print(f"Erro na linha: {numeroLinha}, coluna: {i}")
                exit()
            i += 1
        numeroLinha += 1
    
    printLexemas(lexemas)
    # print(lexemas)