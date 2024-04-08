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
class maquina:
    def __init__(self, lista):
        self.lista = lista

    def getList(self):
        return self.lista

    def currentPosition(self):
        return self.lista[0]
    
    def getType(self):
        return self.currentPosition()[0]
    
    def getLexema(self):
        return self.currentPosition()[1]

    def erro(self, mensagem, linha, coluna):
        print(f'Erro: {mensagem} na linha {linha}, coluna {coluna}')
        exit()

    def consome(self, tipo, lexema):
        atual = self.currentPosition()
        
        token = ''
        if atual[0] in tipos_tokens.values():
            for key, value in tipos_tokens.items():
                if value == atual[0]:
                    token = key
                    break
        
        if token == tipo:
            if atual[1] == lexema or lexema == None:
                self.lista.pop(0)
                print(f'{token} {lexema} consumido!')
                return True
            else:
                self.erro('lexema incorreto', atual[2], atual[3])
                return False
        else:
            self.erro('token incorreto', atual[2], atual[3])
            return False

    def function(self):
        self.consome('tkn_program', 'program')
        self.consome('tkn_variavel', None)
        self.consome('tkn_ponto_virgula', ';')
        self.declarations()
        pass

    def declarations(self):
        self.consome('tkn_var', 'var')
        self.declaration()
        self.consome('tkn_begin', 'begin')
        self.stmtList()

    def declaration(self):
        self.listaIdent()
        self.consome('tkn_dois_pontos', ':')
        self.tipo()
        self.consome('tkn_ponto_virgula', ';')
        self.restoDeclaration()

    def listaIdent(self):
        self.consome('tkn_variavel', None)
        self.restoIdentList()

    def restoIdentList(self):
        while self.getType() != 38:
            self.consome('tkn_virgula', ',')
            self.consome('tkn_variavel', None)
    
    def tipo(self):
        if self.getType() == 42:
            self.consome('tkn_integer', 'integer')
        elif self.getType() == 43: 
            self.consome('tkn_real', 'real')
        elif self.getType() == 44:
            self.consome('tkn_string', 'string')
        else:
            print('Erro: tipo de variável incorreto')
            exit()
    
    def restoDeclaration(self):
        if self.getType == 18:
            self.consome('tkn_var', 'var')
            self.declaration()
            self.restoDeclaration()
    
    def stmtList(self):
        self.stmt()

    def stmt(self):
        if self.getType() == 24:
            self.forStmt()
        elif self.getType() == 33 or self.getType() == 34:
            self.ioStmt()
        elif self.getType() == 26:
            self.whileStmt()
        elif self.getType() == 16:
            self.atribStmt()
            self.consome('tkn_ponto_virgula', ';')
        elif self.getType() == 30:
            self.ifStmt()
        elif self.getType() == 22:
            self.bloco()
        elif self.getType() == 28:
            self.consome('tkn_break', 'break')
            self.consome('tkn_ponto_virgula', ';')
        elif self.getType() == 29:
            self.consome('tkn_continue', 'continue')
            self.consome('tkn_ponto_virgula', ';')
        elif self.getType() == 35:
            self.consome('tkn_ponto_virgula', ';')

# paramos na descrição das instruções linha 31 do miniPascal.gmr

if __name__ == '__main__':
    analisador_sintatico = maquina(parser.executar())
    analisador_sintatico.function()