from classes.Conexao import *

class Anuncio():
    def __init__(self):
        self.__id_produto = 0
        self.__nome_produto = ''
        self.__preco_produto = 0
        self.__marca_produto = ''
        self.__estado_produto = ''
        self.__descricao_produto = ''
        self.__foto_produto = ''
        self.__conn = Conexao()

    def set_id_produto(self, id_produto):
        if id_produto > 0:
            self.__id_produto = id_produto
    def get_id_porduto(self):
        return self.__id_produto
    def set_nome_produto(self,nome_produto):
        if len(nome_produto) > 0:
            self.__nome_produto = nome_produto
    def get_nome_produto(self):
        return self.__nome_produto
    def set_preco_porduto(self,preco_produto):        
        self.__preco_produto = preco_produto
    def get_preco_produto(self):
        return self.__preco_produto  
    def set_marca_produto(self,marca_produto):
        if len(marca_produto) > 0:
            self.__marca_produto = marca_produto
    def get_marca_produto(self):
        return self.__marca_produto
    def set_estado_produto(self,estado_produto):
        if len(estado_produto) > 0:
            self.__estado_produto = estado_produto
    def get_estado_produto(self):
        return self.__estado_produto
    def set_descricao_produto(self,descricao_produto):
        if len(descricao_produto) > 0:
            self.__descricao_produto = descricao_produto
    def get_descricao_produto(self):
        return self.__descricao_produto
    def set_foto_porduto(self,foto_produto):
        if len(foto_produto) > 0:
            self.__foto_produto = foto_produto
    def get_foto_produto(self):
        return self.__foto_produto

    def CreateAnuncio(self):
        sql = "insert into Anuncio(nome_produto,preco_produto,marca_produto, estado_produto, descricao_produto,foto_produto) values(':nome_produto', ':preco_produto',':marca_produto',':estado_produto',':descricao_produto',':foto_produto')"
        sql = sql.replace(':nome_produto', self.__nome_produto)
        sql = sql.replace(':preco_produto', self.__preco_produto)
        sql = sql.replace(':marca_produto', self.__marca_produto)
        sql = sql.replace(':estado_produto', self.__estado_produto)
        sql = sql.replace(':descricao_produto', self.__descricao_produto)
        sql = sql.replace(':foto_produto', self.__foto_produto)
        return self.__conn.execSql(sql)
    def UpdateAnuncio(self):
        sql = "update Anuncio set nome_produto = ':nome_produto', preco_produto = ':preco_produto', marca_produto = ':marca_produto', estado_produto = ':estado_produto', descricao_produto = ':descricao_produto', foto_produto = ':foto_produto' where id_produto = :id_produto "
        sql = sql.replace(':nome_produto', self.__nome_produto)
        sql = sql.replace(':preco_produto', self.__preco_produto)
        sql = sql.replace(':marca_produto', self.__marca_produto)
        sql = sql.replace(':estado_produto', self.__estado_produto)
        sql = sql.replace(':descricao_produto', self.__descricao_produto)
        sql = sql.replace(':foto_produto', self.__foto_produto)
        sql = sql.replace(':id_produto', str(self.__id_produto))
        return self.__conn.execSql(sql)
    def DeleteAnuncio(self):
        sql = "delete from Anuncio where id_produto = :id_produto"
        sql = sql.replace(':id_produto', str(self.__id_produto))
        return self.__conn.execSql(sql)
    def ReadAnuncio(self,id_produto = 0):
        if id_produto != 0:
            self.__id_produto = id_produto
        sql = "select * from Anuncio where id_produto = :id_produto"
        sql = sql.replace(':id_produto', str(self.__id_produto))
        return self.__conn.execSelect(sql)

    def ReadAnuncios(self, id = 0):
        sql = "select * from Anuncio"
        return self.__conn.execSelect(sql)

    
