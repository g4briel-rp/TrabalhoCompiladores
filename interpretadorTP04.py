import codigointermediario
import trab4
import trab4.exe1
import trab4.exe2
import parserTP03

# unitario - subtração -> inverter sinal | exemplo: -(-5)
# unitario - adição -> manter sinal | exemplo: +(-5)
# not - negação -> inverter valor booleano | exemplo: !true

tipos = {
    'adicao': '+',
    'subtracao': '-',
    'multiplicacao': '*',
    'divisao_real': '/',
    'modulo': '%',
    'divisao_inteira': '//',
    'or': '||',
    'and': '&&',
    'not': '!',
    'igualdade': '==',
    'diferença': '<>',
    'maior': '>',
    'maior_igual': '>=',
    'menor': '<',
    'menor_igual': '<=',
    'atribuicao': '=',
    'if': 'if',
    'jump': 'jump',
    'call': 'call',
    'label': 'label'
}

operadores_logicos_relacionais_atibuicao = ['<', '<=', '>', '>=', '==', '<>', '=', '||', '&&', '!']

operadores_aritmeticos = ['+', '-', '*', '/', '%', '//']

def instrucaoIsValid(instrucao):
    if instrucao[0] in tipos.values():
        return True
    return False

def existeVariavel(variavel, variaveis):
    if variavel in variaveis:
        return True
    return False

def executaOperacao(instrucao, variaveis):
    operador = instrucao[0]
    variavel = instrucao[1]

    operando_1 = instrucao[2]
    tipo_operando_1 = type(operando_1)

    existe_variavel_1 = False
    if tipo_operando_1 == str:
        existe_variavel_1 = existeVariavel(operando_1, variaveis)

    operando_2 = instrucao[3]
    tipo_operando_2 = type(operando_2)

    existe_variavel_2 = False
    if tipo_operando_2 == str:
        existe_variavel_2 = existeVariavel(operando_2, variaveis)

    match operador:
        case '<':    
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] < operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 < variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 < operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] < variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '<=':
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] <= operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 <= variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 <= operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] <= variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '>':
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] > operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 > variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 > operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] > variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '>=':
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] >= operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 >= variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 >= operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] >= variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '==':
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] == operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 == variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 == operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] == variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '<>':
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] != operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 != variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 != operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] != variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '=':
            if operando_2 == None:
                if operando_1 == 'int':
                    variaveis[variavel] = 0
                elif operando_1 == 'float':
                    variaveis[variavel] = 0.0
                elif operando_1 == 'string':
                    variaveis[variavel] = ''
                else:
                    print(f'Operação inválida: {instrucao}')
                    exit()
            else:
                if operando_2 in variaveis:
                    variaveis[variavel] = variaveis[operando_2]
                else:
                    variaveis[variavel] = operando_2
        case '||':
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] or operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 or variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 or operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] or variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '&&':
            if existe_variavel_1 and not(existe_variavel_2):
                if variaveis[operando_1] and operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and existe_variavel_2:
                if operando_1 and variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            elif not(existe_variavel_1) and not(existe_variavel_2):
                if operando_1 and operando_2:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
            else:
                if variaveis[operando_1] and variaveis[operando_2]:
                    variaveis[variavel] = True
                else:
                    variaveis[variavel] = False
        case '!':
            if existe_variavel_1:
                variaveis[variavel] = not variaveis[operando_1]
            else:
                variaveis[variavel] = not operando_1
        case '+':
            if existe_variavel_1 and existe_variavel_2:
                variaveis[variavel] = variaveis[operando_1] + variaveis[operando_2]
            elif existe_variavel_1 and not(existe_variavel_2):
                variaveis[variavel] = variaveis[operando_1] + operando_2
            elif not(existe_variavel_1) and existe_variavel_2:
                variaveis[variavel] = operando_1 + variaveis[operando_2]
            else:
                variaveis[variavel] = operando_1 + operando_2
        case '-':
            if operando_2 != None:
                if existe_variavel_1 and existe_variavel_2:
                    variaveis[variavel] = variaveis[operando_1] - variaveis[operando_2]
                elif existe_variavel_1 and not(existe_variavel_2):
                    variaveis[variavel] = variaveis[operando_1] - operando_2
                elif not(existe_variavel_1) and existe_variavel_2:
                    variaveis[variavel] = operando_1 - variaveis[operando_2]
                else:
                    variaveis[variavel] = operando_1 - operando_2
            else:
                if existe_variavel_1:
                    if type(variaveis[operando_1]) == int or type(variaveis[operando_1]) == float:
                        variaveis[variavel] = -variaveis[operando_1]
                    else:
                        print(f'Operação inválida: {instrucao}')
                        exit()
        case '*':
            if existe_variavel_1 and existe_variavel_2:
                variaveis[variavel] = variaveis[operando_1] * variaveis[operando_2]
            elif existe_variavel_1 and not(existe_variavel_2):
                variaveis[variavel] = variaveis[operando_1] * operando_2
            elif not(existe_variavel_1) and existe_variavel_2:
                variaveis[variavel] = operando_1 * variaveis[operando_2]
            else:
                variaveis[variavel] = operando_1 * operando_2
        case '/':
            if existe_variavel_2:
                if variaveis[operando_2] == 0 or variaveis[operando_2] == 0.0:
                    print('Divisão por zero')
                    exit()
            else:
                if operando_2 == 0 or operando_2 == 0.0:
                    print('Divisão por zero')
                    exit()

            if existe_variavel_1 and existe_variavel_2:
                variaveis[variavel] = variaveis[operando_1] / variaveis[operando_2]
            elif existe_variavel_1 and not(existe_variavel_2):
                variaveis[variavel] = variaveis[operando_1] / operando_2
            elif not(existe_variavel_1) and existe_variavel_2:
                variaveis[variavel] = operando_1 / variaveis[operando_2]
            else:
                variaveis[variavel] = operando_1 / operando_2
        case '%':
            if variaveis[operando_2] == 0 or variaveis[operando_2] == 0.0 or operando_2 == 0 or operando_2 == 0.0:
                print('Divisão por zero')
                exit()
                
            if existe_variavel_1 and existe_variavel_2:
                variaveis[variavel] = variaveis[operando_1] % variaveis[operando_2]
            elif existe_variavel_1 and not(existe_variavel_2):
                variaveis[variavel] = variaveis[operando_1] % operando_2
            elif not(existe_variavel_1) and existe_variavel_2:
                variaveis[variavel] = operando_1 % variaveis[operando_2]
            else:
                variaveis[variavel] = operando_1 % operando_2
        case '//':
            if variaveis[operando_2] == 0 or variaveis[operando_2] == 0.0 or operando_2 == 0 or operando_2 == 0.0:
                print('Divisão por zero')
                exit()
                
            if existe_variavel_1 and existe_variavel_2:
                variaveis[variavel] = variaveis[operando_1] // variaveis[operando_2]
            elif existe_variavel_1 and not(existe_variavel_2):
                variaveis[variavel] = variaveis[operando_1] // operando_2
            elif not(existe_variavel_1) and existe_variavel_2:
                variaveis[variavel] = operando_1 // variaveis[operando_2]
            else:
                variaveis[variavel] = operando_1 // operando_2
        case _:
            print(f'Operador "{operador}" não existe')
            exit()

if __name__ == '__main__':
    # lista = codigointermediario.programa()
    # lista = trab4.exe1.programa()
    # lista = trab4.exe2.programa()
    # lista = trab4.exe3.programa()
    lista = parserTP03.main2()
    # print(lista)

    labels = {}
    # (nome, linha)
    for (indice, item) in enumerate(lista):
        if item[0] in tipos.values():
            if item[0] == 'label':
                labels[item[1]] = indice

    # print(labels)

    # (nome, valor)
    variaveis = {}
    ponteiro_execucao = 0

    while ponteiro_execucao < len(lista):
        executa = lista[ponteiro_execucao]

        if not instrucaoIsValid(executa):
            print('Instrução inválida')
            break

        if executa[0] == 'call':
            if executa[1] == 'print':
                # se for string, usar posicao 2
                # se for variável, usar posicao 3
                if executa[2]:
                    print(executa[2])
                elif executa[3]:
                    if executa[3] in variaveis:
                        print(f'{variaveis[executa[3]]}')
                    else:
                        print(f'Variável "{executa[3]}" não existe')
                        exit()
                else:
                    print(f'Instrução inválida: {executa}')
                    exit()
            elif executa[1] == 'scan':
                valor = input()
                
                match executa[3]:
                    case 'int':
                        variaveis[executa[2]] = int(valor)
                    case 'float':
                        variaveis[executa[2]] = float(valor)
                    case 'string':
                        variaveis[executa[2]] = valor
                    case _:
                        print(f'Instrução inválida: {executa}')
                        exit()               
        elif executa[0] == 'jump':
            if executa[1] in labels:
                # print(f'Pulando para label "{executa[1]}" na linha {labels[executa[1]]}')
                ponteiro_execucao = labels[executa[1]]
            else:
                print(f'Label "{executa[1]}" não existe')
                exit()
        elif executa[0] == 'if':
            # verificar se a variavel existe, caso nao exista encerrar o programa
            # verificar se ela é true, pular para a posicao 2
            # senão, pular para a posicao 3
            if existeVariavel(executa[1], variaveis):
                if variaveis[executa[1]]:
                    # print(f'Variavel "{executa[1]}" é verdadeira')
                    ponteiro_execucao = labels[executa[2]]
                else:
                    # print(f'Variavel "{executa[1]}" é falsa')
                    ponteiro_execucao = labels[executa[3]]
            else:
                print(f'Variável "{executa[1]}" não existe')
                exit()
        elif executa[0] in operadores_logicos_relacionais_atibuicao or executa[0] in operadores_aritmeticos:
            executaOperacao(executa, variaveis)
        
        ponteiro_execucao += 1

    # print(variaveis)