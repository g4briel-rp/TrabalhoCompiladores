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
    'tkn_atribuicao': 16,
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
class maquina:
    def __init__(self, lista):
        self.lista = lista

    def getList(self):
        return self.lista

    def currentPosition(self):
        return self.lista[0]
    
    def getType(self):
        return self.currentPosition()[0]

    def erro(self, mensagem, tipo, token, linha, coluna):
        print(f'Erro: {mensagem} | era esperado "{tipo}" e foi passado "{token}" | linha {linha}, coluna {coluna}')
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
            print(f'{token} consumido!')
            return True
        else:
            self.erro('token incorreto', tipo, token, atual[2], atual[3])
            return False

    def inicia(self):
        self.function()

    def function(self):
        self.consome('tkn_program')
        self.consome('tkn_variavel')
        self.consome('tkn_ponto_virgula')
        self.declarations()
        self.consome('tkn_begin')
        self.stmtList()
        self.consome('tkn_end')
        self.consome('tkn_ponto')

    def declarations(self):
        self.consome('tkn_var')
        self.declaration()

    def declaration(self):
        self.listaIdent()
        self.consome('tkn_dois_pontos')
        self.tipo()
        self.consome('tkn_ponto_virgula')
        self.restoDeclaration()

    def listaIdent(self):
        self.consome('tkn_variavel')
        self.restoIdentList()

    def restoIdentList(self):
        while self.getType() != 38:
            self.consome('tkn_virgula')
            self.consome('tkn_variavel')
    
    def tipo(self):
        if self.getType() == tipos_tokens['tkn_integer']:
            self.consome('tkn_integer')
        elif self.getType() == tipos_tokens['tkn_real']: 
            self.consome('tkn_real')
        elif self.getType() == tipos_tokens['tkn_string']:
            self.consome('tkn_string')
    
    def restoDeclaration(self):
        if self.getType() == tipos_tokens['tkn_variavel']:
            self.declaration()
            self.restoDeclaration()
    
    def verificaRecursaoStmtList(self):
        if self.getType() == tipos_tokens['tkn_for'] or self.getType() == tipos_tokens['tkn_read'] or self.getType() == tipos_tokens['tkn_write'] or self.getType() == tipos_tokens['tkn_while'] or self.getType() == tipos_tokens['tkn_atribuicao'] or self.getType() == tipos_tokens['tkn_if'] or self.getType() == tipos_tokens['tkn_begin'] or self.getType() == tipos_tokens['tkn_break'] or self.getType() == tipos_tokens['tkn_continue'] or self.getType() == tipos_tokens['tkn_ponto_virgula']:
            return True
        
        return False

    def stmtList(self):
        if self.verificaRecursaoStmtList():
            self.stmt()
            self.stmtList()

    def stmt(self):
        if self.getType() == tipos_tokens['tkn_for']:
            self.forStmt()
        elif self.getType() == tipos_tokens['tkn_read'] or self.getType() == tipos_tokens['tkn_write']:
            self.ioStmt()
        elif self.getType() == tipos_tokens['tkn_while']:
            self.whileStmt()
        elif self.getType() == tipos_tokens['tkn_atribuicao']:
            self.atrib()
        elif self.getType() == tipos_tokens['tkn_if']:
            self.ifStmt()
        elif self.getType() == tipos_tokens['tkn_begin']:
            self.bloco()
        elif self.getType() == tipos_tokens['tkn_break']:
            self.consome('tkn_break')
            self.consome('tkn_ponto_virgula')
        elif self.getType() == tipos_tokens['tkn_continue']:
            self.consome('tkn_continue')
            self.consome('tkn_ponto_virgula')
        elif self.getType() == tipos_tokens['tkn_ponto_virgula']:
            self.consome('tkn_ponto_virgula')
        
    def forStmt(self):
        self.consome('tkn_for')
        self.atrib()
        self.consome('tkn_to')
        self.endFor()
        self.consome('tkn_do')
        self.stmt()

    def endFor(self):
        if self.getType() == tipos_tokens['tkn_variavel']:
            self.consome('tkn_variavel')
        elif self.getType() == tipos_tokens['tkn_numero_inteiro']:
            self.consome('tkn_numero_inteiro')

    def ioStmt(self):
        if self.getType() == tipos_tokens['tkn_read']:
            self.consome('tkn_read')
            self.consome('tkn_abre_parenteses')
            self.consome('tkn_variavel')
            self.consome('tkn_fecha_parenteses')
            self.consome('tkn_ponto_virgula')
        elif self.getType() == tipos_tokens['tkn_write']:
            self.consome('tkn_write')
            self.consome('tkn_abre_parenteses')
            self.out()
            self.consome('tkn_fecha_parenteses')
            self.consome('tkn_ponto_virgula')

    def out(self):
        if self.getType() == tipos_tokens['tkn_string']:
            self.consome('tkn_string')
        elif self.getType() == tipos_tokens['tkn_variavel']:
            self.consome('tkn_variavel')
        elif self.getType() == tipos_tokens['tkn_numero_inteiro']:
            self.consome('tkn_numero_inteiro')
        elif self.getType() == tipos_tokens['tkn_numero_real']:
            self.consome('tkn_numero_real')

    def whileStmt(self):
        self.consome('tkn_while')
        self.expr()
        self.stmt()

    def atrib(self):
        self.consome('tkn_variavel')
        self.consome('tkn_atribuicao')
        self.expr()

    def expr(self):
        self.operationOR()

    def operationOR(self):
        self.operationAND()
        self.restOperationOR()

    def restOperationOR(self):
        if self.getType() == tipos_tokens['tkn_or']:
            self.consome('tkn_or')
            self.operationAND()
            self.restOperationOR()
    
    def operationAND(self):
        self.operationNOT()
        self.restOperationAND()

    def restOperationAND(self):
        if self.getType() == tipos_tokens['tkn_and']:
            self.consome('tkn_and')
            self.operationNOT()
            self.restOperationAND()

    def operationNOT(self):
        if self.getType() == tipos_tokens['tkn_not']:
            self.consome('tkn_not')
            self.operationNOT()
        else:
            self.rel()

    def rel(self):
        self.operationADD()
        self.restRel()

    def restRel(self):
        if self.getType() == tipos_tokens['tkn_igual']:
            self.consome('tkn_igual')
            self.operationADD()
        elif self.getType() == tipos_tokens['tkn_dif']:
            self.consome('tkn_dif')
            self.operationADD()
        elif self.getType() == tipos_tokens['tkn_menor']:
            self.consome('tkn_menor')
            self.operationADD()
        elif self.getType() == tipos_tokens['tkn_menor_igual']:
            self.consome('tkn_menor_igual')
            self.operationADD()
        elif self.getType() == tipos_tokens['tkn_maior']:
            self.consome('tkn_maior')
            self.operationADD()
        elif self.getType() == tipos_tokens['tkn_maior_igual']:
            self.consome('tkn_maior_igual')
            self.operationADD()

    def operationADD(self):
        self.operationMULT()
        self.restOperationADD()

    def restOperationADD(self):
        if self.getType() == tipos_tokens['tkn_add']:
            self.consome('tkn_add')
            self.operationMULT()
            self.restOperationADD()
        elif self.getType() == tipos_tokens['tkn_sub']:
            self.consome('tkn_sub')
            self.operationMULT()
            self.restOperationADD()

    def operationMULT(self):
        self.uno()
        self.restOperationMULT()

    def restOperationMULT(self):
        if self.getType() == tipos_tokens['tkn_mult']:
            self.consome('tkn_mult')
            self.uno()
            self.restOperationMULT()
        elif self.getType() == tipos_tokens['tkn_divisao']:
            self.consome('tkn_divisao')
            self.uno()
            self.restOperationMULT()
        elif self.getType() == tipos_tokens['tkn_mod']:
            self.consome('tkn_mod')
            self.uno()
            self.restOperationMULT()
        elif self.getType() == tipos_tokens['tkn_div']:
            self.consome('tkn_div')
            self.uno()
            self.restOperationMULT()

    def uno(self):
        if self.getType() == tipos_tokens['tkn_add']:
            self.consome('tkn_add')
            self.uno()
        elif self.getType() == tipos_tokens['tkn_sub']:
            self.consome('tkn_sub')
            self.uno()
        else:
            self.fator()

    def fator(self):
        if self.getType() == tipos_tokens['tkn_numero_inteiro']:
            self.consome('tkn_numero_inteiro')
        elif self.getType() == tipos_tokens['tkn_numero_real']:
            self.consome('tkn_numero_real')
        elif self.getType() == tipos_tokens['tkn_variavel']:
            self.consome('tkn_variavel')
        elif self.getType() == tipos_tokens['tkn_abre_parenteses']:
            self.consome('tkn_abre_parenteses')
            self.expr()
            self.consome('tkn_fecha_parenteses')
        elif self.getType() == tipos_tokens['tkn_string']:
            self.consome('tkn_string')

    def ifStmt(self):
        self.consome('tkn_if')
        self.expr()
        self.consome('tkn_then')
        self.stmt()
        self.elsePart()

    def elsePart(self):
        if self.getType() == tipos_tokens['tkn_else']:
            self.consome('tkn_else')
            self.stmt()

    def bloco(self):
        self.consome('tkn_begin')
        self.stmtList()
        self.consome('tkn_end')
        self.consome('tkn_ponto_virgula')

if __name__ == '__main__':
    analisador_sintatico = maquina(parser.executar())
    analisador_sintatico.inicia()