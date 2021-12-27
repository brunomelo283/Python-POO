import sqlite3

class Conexao():
    def __init__(self):
        self.__conexao = None
        self.__cursor = None

    def __abrirConexao(self):
        self.__conexao = sqlite3.connect("db/w3c.db")
        self.__conexao.row_factory = sqlite3.Row  
        self.__cursor = self.__conexao.cursor()

    def __fecharConexao(self):
        self.__cursor.close()
        self.__conexao.close()

    def execSql(self, sql):        
        rows = -10 
        if len(sql) > 0:
            self.__abrirConexao()

            self.__cursor.execute(sql) 
            rows = self.__cursor.rowcount 
            self.__conexao.commit()

            self.__fecharConexao()
        return rows

    def execSelect(self, sql):
        dados = ''
        if len(sql) > 0:
            self.__abrirConexao()

            self.__cursor.execute(sql)
            dados = self.__cursor.fetchall()             
            self.__fecharConexao()
        return dados