import codigointermediario

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

def instrucaoIsValid(instrucao):
    if instrucao[0] in tipos.values():
        return True
    return False

def existeVariavel(variavel, variaveis):
    if variavel in variaveis:
        return True
    return False

if __name__ == '__main__':
    lista = codigointermediario.programa()
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
                        print(f'Valor da variavel {executa[3]}: {variaveis[executa[3]]}')
                    else:
                        print(f'Variável "{executa[3]}" não existe')
                        exit()
                else:
                    print(f'Instrução inválida: {executa}')
                    exit()
            elif executa[1] == 'scan':
                valor = input()
                variaveis[executa[2]] = valor
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
        elif executa[0] == '<':
            operando_1 = executa[2]
            operando_2 = executa[3]

            if type(operando_1) == str and type(operando_2) == str:
                if existeVariavel(executa[2], variaveis) and existeVariavel(executa[3], variaveis):
                    if variaveis[executa[2]] < variaveis[executa[3]]:
                        variaveis[executa[1]] = True
                    else:
                        variaveis[executa[1]] = False
            elif type(operando_1) == str and type(operando_2) != str:
                if existeVariavel(executa[2], variaveis):
                    if int(variaveis[executa[2]]) < executa[3]:
                        variaveis[executa[1]] = True
                    else:
                        variaveis[executa[1]] = False
            elif type(operando_1) != str and type(operando_2) == str:
                if existeVariavel(executa[3], variaveis):
                    if executa[2] < int(variaveis[executa[3]]):
                        variaveis[executa[1]] = True
                    else:
                        variaveis[executa[1]] = False
            else:
                if executa[2] < executa[3]:
                    variaveis[executa[1]] = True
                else:
                    variaveis[executa[1]] = False
        
        # continuar para as outras instruções
        
        ponteiro_execucao += 1

    print(variaveis)