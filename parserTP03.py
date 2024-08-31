import parserTP01 as parser

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
    'tkn_atribuicao': 16,
    'tkn_program': 17,
    'tkn_var': 18,
    'tkn_integer': 19,
    'tkn_real': 20,
    'tkn_tipo_string': 21,
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

dic_variavies = {}
class gerador:
    def __init__(self):
        self.contador_for = 0
        self.contador_while = 0
        self.contador_if = 0
        self.contador_var_temp = 0

    def geraLabel(self, sigla):
        if sigla == 'f':
            self.contador_for += 1
            return f'inicio_for_{self.contador_for}', f'verdade_for_{self.contador_for}', f'falsidade_for_{self.contador_for}'
        elif sigla == 'w':
            self.contador_while += 1
            return f'inicio_while_{self.contador_while}', f'verdade_while_{self.contador_while}', f'falsidade_while_{self.contador_while}'
        elif sigla == 'i':
            self.contador_if += 1
            return f'verdade_if_{self.contador_if}', f'falsidade_if_{self.contador_if}', f'fim_if_{self.contador_if}'
    
    def geraVariavelTemp(self):
        self.contador_var_temp += 1
        dic_variavies[f'var_temp_{self.contador_var_temp}'] = 'float'
        return f'var_temp_{self.contador_var_temp}'
    
    def getVariavelTemp(self):
        return f'var_temp_{self.contador_var_temp}'
class maquina:
    def __init__(self, lista):
        self.lista = lista
        self.gerador = gerador()

    def getList(self):
        # print(self.lista)
        return self.lista

    def currentPosition(self):
        return self.lista[0]
    
    def getType(self):
        return self.currentPosition()[0]
    
    def getLexema(self):
        return self.currentPosition()[1]
    
    def getLinha(self):
        return self.currentPosition()[2]
    
    def getColuna(self):
        return self.currentPosition()[3]

    def erro(self, mensagem, tipo, token, linha, coluna):
        print(f'Erro: {mensagem} | era esperado "{tipo}" e foi passado "{token}" | linha {linha}, coluna {coluna}')
        exit()

    def erroVariavelNaoDeclarada(self, variavel, linha, coluna):
        print(f'Erro: variável ("{variavel}") não foi declarada | linha {linha}, coluna {coluna}')
        exit()

    def consome(self, tipo):
        atual = self.currentPosition()
        
        token = ''
        if atual[0] in tipos_tokens.values():
            for key, value in tipos_tokens.items():
                if value == atual[0]:
                    token = key
                    break
        
        if token == tipo:
            self.lista.pop(0)
            # print(f'{token} consumido!')
            return True
        else:
            self.erro('token incorreto', tipo, token, atual[2], atual[3])
            return False

    def inicia(self):
        # self.getList()
        lista_final = []

        lista_final.extend(self.function())

        for i in range(self.gerador.contador_var_temp, 0, -1):
            lista_final.insert(0, ('=', f'var_temp_{i}', 'float', None))

        # for item in lista_final:
        #     print(item)

        print(f'Analisador Semântico e Geração de Código - OK')

        return lista_final

    def function(self):
        lista_function = []

        self.consome('tkn_program')
        self.consome('tkn_variavel')
        self.consome('tkn_ponto_virgula')
        lista_function.extend(self.declarations())
        self.consome('tkn_begin')
        lista_function.extend(self.stmtList())
        self.consome('tkn_end')
        self.consome('tkn_ponto')

        return lista_function

    def declarations(self):
        lista_declarations = []

        self.consome('tkn_var')
        lista_declarations.extend(self.declaration())

        return lista_declarations

    def declaration(self):
        lista_declaration = []

        variaveis = self.listaIdent()
        self.consome('tkn_dois_pontos')
        lista_declaration.extend(self.tipo(variaveis))
        self.consome('tkn_ponto_virgula')
        lista_declaration.extend(self.restoDeclaration())

        for item in lista_declaration:
            # print(item)
            dic_variavies[item[1]] = item[2]

        # print(dic_variavies)

        return lista_declaration

    def listaIdent(self):
        lista_listaIdent = []

        lista_listaIdent.append(self.getLexema())
        self.consome('tkn_variavel')
        lista_listaIdent.extend(self.restoIdentList())

        return lista_listaIdent

    def restoIdentList(self):
        lista_restoIdentList = []

        if self.getType() == tipos_tokens['tkn_virgula']:
            self.consome('tkn_virgula')
            lista_restoIdentList.append(self.getLexema())
            self.consome('tkn_variavel')
            lista_restoIdentList.extend(self.restoIdentList())

        return lista_restoIdentList
    
    def tipo(self, variaveis):
        lista_tipo = []

        if self.getType() == tipos_tokens['tkn_integer']:
            self.consome('tkn_integer')
            for var in variaveis:
                lista_tipo.append(('=', var, 'int', None))
        elif self.getType() == tipos_tokens['tkn_real']: 
            self.consome('tkn_real')
            for var in variaveis:
                lista_tipo.append(('=', var, 'float', None))
        elif self.getType() == tipos_tokens['tkn_tipo_string']:
            self.consome('tkn_tipo_string')
            for var in variaveis:
                lista_tipo.append(('=', var, 'string', None))
        else:
            atual = self.currentPosition()
            print(f'atual: {atual}')
            token = ''
            if atual[0] in tipos_tokens.values():
                for key, value in tipos_tokens.items():
                    if value == atual[0]:
                        token = key
                        break
                    
            self.erro('token incorreto', 'tkn_integer, tkn_real ou tkn_tipo_string', token, atual[2], atual[3])
        return lista_tipo
    
    def restoDeclaration(self):
        lista_restoDeclaration = []

        if self.getType() == tipos_tokens['tkn_variavel']:
            lista_restoDeclaration.extend(self.declaration())
            lista_restoDeclaration.extend(self.restoDeclaration())

        return lista_restoDeclaration
    
    def verificaRecursaoStmtList(self):
        if self.getType() == tipos_tokens['tkn_for'] or self.getType() == tipos_tokens['tkn_read'] or self.getType() == tipos_tokens['tkn_write'] or self.getType() == tipos_tokens['tkn_while'] or self.getType() == tipos_tokens['tkn_variavel'] or self.getType() == tipos_tokens['tkn_if'] or self.getType() == tipos_tokens['tkn_begin'] or self.getType() == tipos_tokens['tkn_break'] or self.getType() == tipos_tokens['tkn_continue'] or self.getType() == tipos_tokens['tkn_ponto_virgula']:
            return True
        
        return False

    def stmtList(self, labelB = None, labelC = None):
        lista_stmtList = []

        if self.verificaRecursaoStmtList():
            lista_stmtList.extend(self.stmt(labelB, labelC))
            lista_stmtList.extend(self.stmtList(labelB, labelC))
        
        return lista_stmtList

    def stmt(self, labelB = None, labelC = None):
        lista_stmt = []

        if self.getType() == tipos_tokens['tkn_for']:
            lista_stmt.extend(self.forStmt())
        elif self.getType() == tipos_tokens['tkn_read'] or self.getType() == tipos_tokens['tkn_write']:
            lista_stmt.extend(self.ioStmt())
        elif self.getType() == tipos_tokens['tkn_while']:
            lista_stmt.extend(self.whileStmt())
        elif self.getType() == tipos_tokens['tkn_variavel']:
            lista, _ = self.atrib()
            lista_stmt.extend(lista)
        elif self.getType() == tipos_tokens['tkn_if']:
            lista_stmt.extend(self.ifStmt(labelB, labelC))
        elif self.getType() == tipos_tokens['tkn_begin']:
            lista_stmt.extend(self.bloco(labelB, labelC))
        elif self.getType() == tipos_tokens['tkn_break']:
            lista_stmt.append(('jump', labelB, None, None))
            self.consome('tkn_break')
            self.consome('tkn_ponto_virgula')
        elif self.getType() == tipos_tokens['tkn_continue']:
            lista_stmt.append(('jump', labelC, None, None))
            self.consome('tkn_continue')
            self.consome('tkn_ponto_virgula')
        elif self.getType() == tipos_tokens['tkn_ponto_virgula']:
            self.consome('tkn_ponto_virgula')
        
        return lista_stmt
        
    def forStmt(self):
        lista_for = []

        self.consome('tkn_for')
        
        extend, lexema = self.atrib()
        lista_for.extend(extend)

        self.consome('tkn_to')

        label1, label2, label3 = self.gerador.geraLabel('f')

        lista_for.append(('label', label1, None, None))
        extend2, varTemp = self.endFor(lexema)
        lista_for.extend(extend2)

        self.consome('tkn_do')

        lista_for.append(('if', varTemp, label2, label3))
        lista_for.append(('label', label2, None, None))

        lista_for.extend(self.stmt(label3, label1))

        lista_for.append(('+', lexema, lexema, 1))
        lista_for.append(('jump', label1, None, None))
        lista_for.append(('label', label3, None, None))

        # print(lista_for)
        return lista_for

    def endFor(self, lexema):
        lista_end_for = []

        varTemp = self.gerador.geraVariavelTemp()

        if self.getType() == tipos_tokens['tkn_variavel']:
            
            if self.getLexema() not in dic_variavies.keys():
                self.erroVariavelNaoDeclarada(self.getLexema(), self.getLinha(), self.getColuna())

            lista_end_for.append(('<', varTemp, lexema, self.getLexema()))
            self.consome('tkn_variavel')
        elif self.getType() == tipos_tokens['tkn_numero_inteiro']:
            lista_end_for.append(('<', varTemp, lexema, int(self.getLexema())))
            self.consome('tkn_numero_inteiro')
        else:
            atual = self.currentPosition()
            token = ''
            if atual[0] in tipos_tokens.values():
                for key, value in tipos_tokens.items():
                    if value == atual[0]:
                        token = key
                        break
                    
            self.erro('token incorreto', 'tkn_variavel ou tkn_numero_inteiro', token, atual[2], atual[3])
        
        return lista_end_for, varTemp

    def ioStmt(self):
        lista_IO = []

        if self.getType() == tipos_tokens['tkn_read']:
            self.consome('tkn_read')
            self.consome('tkn_abre_parenteses')

            if self.getLexema() not in dic_variavies.keys():
                self.erroVariavelNaoDeclarada(self.getLexema(), self.getLinha(), self.getColuna())

            lista_IO.append(('call', 'scan', self.getLexema(), dic_variavies[self.getLexema()]))
            self.consome('tkn_variavel')
            self.consome('tkn_fecha_parenteses')
            self.consome('tkn_ponto_virgula')

        elif self.getType() == tipos_tokens['tkn_write']:
            self.consome('tkn_write')
            self.consome('tkn_abre_parenteses')
            lista_IO.extend(self.outlist())
            self.consome('tkn_fecha_parenteses')
            self.consome('tkn_ponto_virgula')

        # print(lista_IO)
        return lista_IO

    def outlist(self):
        lista_outlist = []

        lista_outlist.extend(self.out())
        lista_outlist.extend(self.restOutlist())

        return lista_outlist

    def out(self):
        lista_out = []

        if self.getType() == tipos_tokens['tkn_string']:
            lista_out.append(('call', 'print', self.getLexema(), None))
            self.consome('tkn_string')
        elif self.getType() == tipos_tokens['tkn_variavel']:
            if self.getLexema() not in dic_variavies.keys():
                self.erroVariavelNaoDeclarada(self.getLexema(), self.getLinha(), self.getColuna())

            lista_out.append(('call', 'print', None, self.getLexema()))
            self.consome('tkn_variavel')
        elif self.getType() == tipos_tokens['tkn_numero_inteiro']:
            lista_out.append(('call', 'print', self.getLexema(), None))
            self.consome('tkn_numero_inteiro')
        elif self.getType() == tipos_tokens['tkn_numero_real']:
            lista_out.append(('call', 'print', self.getLexema(), None))
            self.consome('tkn_numero_real')
        else:
            atual = self.currentPosition()
            token = ''
            if atual[0] in tipos_tokens.values():
                for key, value in tipos_tokens.items():
                    if value == atual[0]:
                        token = key
                        break

            self.erro('token incorreto', 'tkn_string, tkn_variavel, tkn_numero_inteiro ou tkn_numero_real', token, atual[2], atual[3])

        return lista_out
    
    def restOutlist(self):
        lista_restoOutList = []

        if self.getType() == tipos_tokens['tkn_virgula']:
            self.consome('tkn_virgula')
            lista_restoOutList.extend(self.outlist())

        return lista_restoOutList

    def whileStmt(self):
        lista_while = []

        self.consome('tkn_while')

        resultado, extend = self.expr()
        lista_while.extend(extend)

        label1, label2, label3 = self.gerador.geraLabel('w')

        lista_while.append(('label', label1, None, None))

        varTemp = self.gerador.getVariavelTemp()
        lista_while.append(('if', varTemp, label2, label3))
        lista_while.append(('label', label2, None, None)) 

        self.consome('tkn_do')
        lista_while.extend(self.stmt(label3, label1))

        lista_while.append(('+', varTemp, resultado, 1))
        lista_while.append(('jump', label1, None, None))
        lista_while.append(('label', label3, None, None))

        return lista_while

    def atrib(self):
        lista_atrib = []

        lexema_var = self.getLexema()

        if lexema_var not in dic_variavies.keys():
                self.erroVariavelNaoDeclarada(lexema_var, self.getLinha(), self.getColuna())
        
        self.consome('tkn_variavel')
        self.consome('tkn_atribuicao')

        resultado, extend = self.expr()
        lista_atrib.extend(extend)

        varTemp = self.gerador.getVariavelTemp()

        if extend:
            lista_atrib.append(('=', lexema_var, None, varTemp))
        else:
            lista_atrib.append(('=', lexema_var, None, resultado))

        return lista_atrib, lexema_var

    def expr(self):
        lista_expr = []
        
        resultado, extend = self.operationOR()
        lista_expr.extend(extend)

        return resultado, lista_expr

    def operationOR(self):
        lista_operationOR = []

        resultado, extend = self.operationAND()
        lista_operationOR.extend(extend)
        
        lista_operationOR.extend(self.restOperationOR(resultado))

        return resultado, lista_operationOR

    def restOperationOR(self, resultant):
        lista_restOperationOR = []

        if self.getType() == tipos_tokens['tkn_or']:
            self.consome('tkn_or')
            resultado, extend = self.operationAND()
            lista_restOperationOR.extend(extend)

            varTemp = self.gerador.geraVariavelTemp()
            lista_restOperationOR.append(('||', varTemp, resultant, resultado))
            lista_restOperationOR.extend(self.restOperationOR(varTemp))
        
        return lista_restOperationOR
    
    def operationAND(self):
        lista_operationAND = []

        resultado, extend = self.operationNOT()
        lista_operationAND.extend(extend)
        lista_operationAND.extend(self.restOperationAND(resultado))

        return resultado, lista_operationAND

    def restOperationAND(self, resultant):
        lista_restOperationAND = []
        
        if self.getType() == tipos_tokens['tkn_and']:
            self.consome('tkn_and')
            resultado, extend = self.operationNOT()
            lista_restOperationAND.extend(extend)

            varTemp = self.gerador.geraVariavelTemp()
            lista_restOperationAND.append(('&&', varTemp, resultant, resultado))
            
            lista_restOperationAND.extend(self.restOperationAND(varTemp))
        
        return lista_restOperationAND

    def operationNOT(self, resultant = None):
        lista_operationNOT = []

        if self.getType() == tipos_tokens['tkn_not']:
            self.consome('tkn_not')
            resultado, extend = self.operationNOT()

            varTemp = self.gerador.geraVariavelTemp()
            lista_operationNOT.append(('!', varTemp, resultado, None))
        else:
            resultado, extend = self.rel()
            lista_operationNOT.extend(extend)

        return resultado, lista_operationNOT

    def rel(self):
        lista_rel = []

        resultado, extend = self.operationADD()
        lista_rel.extend(extend)
        lista_rel.extend(self.restRel(resultado))

        return resultado, lista_rel

    def restRel(self, resultant):
        lista_restRel = []
        
        if self.getType() == tipos_tokens['tkn_igual']:
            self.consome('tkn_igual')

            resultado, extend = self.operationADD()
            lista_restRel.extend(extend)
            
            varTemp = self.gerador.geraVariavelTemp()
            lista_restRel.append(('==', varTemp, resultant, resultado))
        elif self.getType() == tipos_tokens['tkn_dif']:
            self.consome('tkn_dif')

            resultado, extend = self.operationADD()
            lista_restRel.extend(extend)
            
            varTemp = self.gerador.geraVariavelTemp()
            lista_restRel.append(('<>', varTemp, resultant, resultado))
        elif self.getType() == tipos_tokens['tkn_menor']:
            self.consome('tkn_menor')

            resultado, extend = self.operationADD()
            lista_restRel.extend(extend)
            
            varTemp = self.gerador.geraVariavelTemp()
            lista_restRel.append(('<', varTemp, resultant, resultado))
        elif self.getType() == tipos_tokens['tkn_menor_igual']:
            self.consome('tkn_menor_igual')
            
            resultado, extend = self.operationADD()
            lista_restRel.extend(extend)
            
            varTemp = self.gerador.geraVariavelTemp()
            lista_restRel.append(('<=', varTemp, resultant, resultado))
        elif self.getType() == tipos_tokens['tkn_maior']:
            self.consome('tkn_maior')

            resultado, extend = self.operationADD()
            lista_restRel.extend(extend)
            
            varTemp = self.gerador.geraVariavelTemp()
            lista_restRel.append(('>', varTemp, resultant, resultado))
        elif self.getType() == tipos_tokens['tkn_maior_igual']:
            self.consome('tkn_maior_igual')
            
            resultado, extend = self.operationADD()
            lista_restRel.extend(extend)
            
            varTemp = self.gerador.geraVariavelTemp()
            lista_restRel.append(('>=', varTemp, resultant, resultado))

        return lista_restRel

    def operationADD(self):
        lista_operationADD = []

        resultado, extend = self.operationMULT()
        lista_operationADD.extend(extend)
        lista_operationADD.extend(self.restOperationADD(resultado))

        return resultado, lista_operationADD

    def restOperationADD(self, resultant):
        lista_restOperationADD = []
        if self.getType() == tipos_tokens['tkn_add']:
            self.consome('tkn_add')

            varTemp = self.gerador.geraVariavelTemp()
            
            resultado, extend = self.operationMULT()
            lista_restOperationADD.extend(extend)
            lista_restOperationADD.append(('+', varTemp, resultant, resultado))   
            lista_restOperationADD.extend(self.restOperationADD(varTemp))
        elif self.getType() == tipos_tokens['tkn_sub']:
            self.consome('tkn_sub')
            
            varTemp = self.gerador.geraVariavelTemp()
            
            resultado, extend = self.operationMULT()
            lista_restOperationADD.extend(extend)
            lista_restOperationADD.append(('-', varTemp, resultant, resultado))   
            lista_restOperationADD.extend(self.restOperationADD(varTemp))
        
        return lista_restOperationADD

    def operationMULT(self):
        lista_operationMULT = []

        resultado, extend = self.uno()
        lista_operationMULT.extend(extend)
        lista_operationMULT.extend(self.restOperationMULT(resultado))

        return resultado, lista_operationMULT

    def restOperationMULT(self, resultant):
        lista_restOperationMULT = []

        if self.getType() == tipos_tokens['tkn_mult']:
            self.consome('tkn_mult')
            resultado, extend = self.uno()
            lista_restOperationMULT.extend(extend)

            varTemp = self.gerador.geraVariavelTemp()
            lista_restOperationMULT.append(('*', varTemp, resultant, resultado))

            lista_restOperationMULT.extend(self.restOperationMULT(varTemp))
        elif self.getType() == tipos_tokens['tkn_divisao']:
            self.consome('tkn_divisao')
            resultado, extend = self.uno()
            lista_restOperationMULT.extend(extend)
            
            varTemp = self.gerador.geraVariavelTemp()
            lista_restOperationMULT.append(('/', varTemp, resultant, resultado))

            lista_restOperationMULT.extend(self.restOperationMULT(varTemp))
        elif self.getType() == tipos_tokens['tkn_mod']:
            self.consome('tkn_mod')
            resultado, extend = self.uno()
            lista_restOperationMULT.extend(extend)

            varTemp = self.gerador.geraVariavelTemp()
            lista_restOperationMULT.append(('%', varTemp, resultant, resultado))
            
            lista_restOperationMULT.extend(self.restOperationMULT(varTemp))
        elif self.getType() == tipos_tokens['tkn_div']:
            self.consome('tkn_div')
            resultado, extend = self.uno()
            lista_restOperationMULT.extend(extend)

            varTemp = self.gerador.geraVariavelTemp()
            lista_restOperationMULT.append(('//', varTemp, resultant, resultado))
            
            lista_restOperationMULT.extend(self.restOperationMULT(varTemp))
        
        return lista_restOperationMULT

    def uno(self):
        lista_uno = []

        if self.getType() == tipos_tokens['tkn_add']:
            lista_uno.append(self.getLexema())
            self.consome('tkn_add')
            resultado, extend = self.uno()
            lista_uno.extend(extend)
        elif self.getType() == tipos_tokens['tkn_sub']:
            lista_uno.append(self.getLexema())
            self.consome('tkn_sub')
            resultado, extend = self.uno()
            lista_uno.extend(extend)
        else:
            resultado, extend = self.fator()
            lista_uno.extend(extend)

        return resultado, lista_uno

    def fator(self):
        lista_fator = []

        if self.getType() == tipos_tokens['tkn_numero_inteiro']:
            atual = int(self.getLexema())
            self.consome('tkn_numero_inteiro')
        elif self.getType() == tipos_tokens['tkn_numero_real']:
            atual = float(self.getLexema())
            self.consome('tkn_numero_real')
        elif self.getType() == tipos_tokens['tkn_variavel']:

            atual = self.getLexema()

            if atual not in dic_variavies.keys():
                self.erroVariavelNaoDeclarada(atual, self.getLinha(), self.getColuna())

            self.consome('tkn_variavel')
        elif self.getType() == tipos_tokens['tkn_abre_parenteses']:
            self.consome('tkn_abre_parenteses')

            _, extend = self.expr()
            lista_fator.extend(extend)
            atual = self.gerador.getVariavelTemp()

            self.consome('tkn_fecha_parenteses')
        elif self.getType() == tipos_tokens['tkn_string']:
            atual = self.getLexema()
            self.consome('tkn_string')
        else:
            atual = self.currentPosition()
            token = ''
            if atual[0] in tipos_tokens.values():
                for key, value in tipos_tokens.items():
                    if value == atual[0]:
                        token = key
                        break
                    
            self.erro('token incorreto', 'tkn_numero_inteiro, tkn_numero_real, tkn_variavel, (<expr>) ou tkn_string', token, atual[2], atual[3])
        
        return atual, lista_fator

    def ifStmt(self, labelB = None, labelC = None):
        lista_ifStmt = []

        self.consome('tkn_if')
        
        _, extend = self.expr()
        lista_ifStmt.extend(extend)

        label1, label2, label3 = self.gerador.geraLabel('i')

        varTemp = self.gerador.getVariavelTemp()
        lista_ifStmt.append(('if', varTemp, label1, label2))
        lista_ifStmt.append(('label', label1, None, None))

        self.consome('tkn_then')

        lista_ifStmt.extend(self.stmt(labelB, labelC))

        lista_ifStmt.extend(self.elsePart(label2, label3))

        return lista_ifStmt

    def elsePart(self, label2, label3):
        lista_eslePart = []

        if self.getType() == tipos_tokens['tkn_else']:
            lista_eslePart.append(('jump', label3, None, None))
            self.consome('tkn_else')
            lista_eslePart.append(('label', label2, None, None))
            lista_eslePart.extend(self.stmt())
            lista_eslePart.append(('label', label3, None, None))
        else:
            lista_eslePart.append(('label', label2, None, None))

        return lista_eslePart

    def bloco(self, labelB = None, labelC = None):
        lista_bloco = []
        
        self.consome('tkn_begin')
        lista_bloco.extend(self.stmtList(labelB, labelC))
        self.consome('tkn_end')
        self.consome('tkn_ponto_virgula')

        # print(lista_bloco)
        return lista_bloco

if __name__ == '__main__':
    analisador_sintatico = maquina(parser.executar())
    lista = analisador_sintatico.inicia()


def main2():
    analisador_sintatico = maquina(parser.executar())
    lista = analisador_sintatico.inicia()
    return lista