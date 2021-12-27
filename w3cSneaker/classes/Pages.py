import cherrypy
import os



from classes.Anuncio import Anuncio
from classes.Marcas import Marcas

local_dir = os.path.dirname(__file__)
local_foto = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'image'))
local_js = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'js'))



class PageHome():
    topo = open("template/topo.html").read()
    footer = open("template/footer.html").read()
    @cherrypy.expose()
    def index(self):        
        return self.ExibirAnuncio()
    def ExibirAnuncio(self):
        html = self.topo
        html += ''' 
                    <aside class="sidebar">
                    <div class="menuzin"><!--Depois muda isso aq foi só pra testar-->
                        <h1>Filtros</h1><br>
                        <form action="#">
                            <h3>Modelo</h3>
                            <input type="radio" name="Genero" id="tGenero">
                            <label for="">Masculino</label> <br>
                            <input type="radio" name="Genero" id="tGenero1">
                            <label for="">Feminino</label> <br>
                            <input type="radio" name="Genero" id="tGenero1">
                            <label for="">Infantil</label> <br> <br>

                            <h3>Preço</h3>
                            <input type="radio" name="Preço" id="tPreço">
                            <label for="">R$: 300 ou menos</label> <br>
                            <input type="radio" name="Preço" id="tPreço1">
                            <label for="">R$: 400-500</label> <br>
                            <input type="radio" name="Preço" id="tPreço2">
                            <label for="">R$: 500-600</label> <br>
                            <input type="radio" name="Preço" id="tPreço3">
                            <label for="">R$: 600-700</label> <br>
                            <input type="radio" name="Preço" id="tPreço4">
                            <label for="">R$: 700-800</label> <br>
                            <input type="radio" name="Preço" id="tPreço5">
                            <label for="">R$: 800 ou mais</label> <br> <br>
                            

                            <h3>Marca</h3>
                            <input type="radio" name="Marca" id="tMarca">
                            <label for="">Nike</label> <br>
                            <input type="radio" name="Marca" id="tMarca1">
                            <label for="">Air Jordan</label> <br>
                            <input type="radio" name="Marca" id="tMarca2">
                            <label for="">Adidas</label> <br>
                            <input type="radio" name="Marca" id="tMarca1">
                            <label for="">New Balance</label> <br>
                            <input type="radio" name="Marca" id="tMarca2">
                            <label for="">Fila</label> <br>
                        </form>
                    </div>
            
                </aside>
                <section class="conteudo">        
                    <div class="texto">
                        <h2>Novidades</h2>
                        <div class="novidades">'''
        objAnuncio = Anuncio()
        values = objAnuncio.ReadAnuncios()
        for key in values:
            html+= "<div class='sombra'>" 
            html+= "<img src='../image/{}'>" .format(key["foto_produto"])
            html+= "<span> {} </span>"  .format(key["nome_produto"])
            html+= "<span> {} á vista</span>" .format(key["preco_produto"])
            html += "<script src='../js/app.js'></script>" 
            html+= "<a  href='/pgAnuncio/AlterarAnuncio?id_produto=%s'>Alterar</a>" %(key["id_produto"])
            html+= "<a class='event' onclick='ConfirmAnuncio(%s)'>Excluir</a>"%(key["id_produto"])
                   
            html+=  "<a href='/pgDetalhes/Detalhes?id_produto={}'>+ Detalhes</a>"  .format(key["id_produto"])
            html+= "</div>" 
                            
        html += '''
                        </div>                                                                        
                    </div>
                </section>                 
                '''        
        html += self.footer
        return html
    @cherrypy.expose()
    def ExcluirAnuncio(self,id_produto):
        objAnuncio = Anuncio()
        objAnuncio.set_id_produto(int(id_produto))
        if objAnuncio.DeleteAnuncio() > 0:
            raise cherrypy.HTTPRedirect("/pgHome")
        else:
            '''
                 <p>Não foi possível excluir o Anuncio...<p>
                <p>[<a href="/">Voltar</a>]</p>
            '''
   

class PageDetalhes():
    topo = open("template/topo.html").read()
    footer = open("template/footer.html").read()
    @cherrypy.expose()
    def index(self):        
        return self.Detalhes()
    @cherrypy.expose()
    def Detalhes(self,id_produto):
        objAnuncio = Anuncio()
        objAnuncio.set_id_produto(int(id_produto))
        html = self.topo
        html += '''
        <h1>Detalhes</h1>
        <section class="conteudo-detalhes">              

           <div class="detalhes-principal">'''
        value = objAnuncio.ReadAnuncio(int(id_produto))
        html+="<img src='../image/%s' alt=''> "  %(value[0]["foto_produto"])
        html+= '''
            <div class="check">
                <div class="check-texto">'''
        html+=  "<h3>Estado: {}</h3>" .format(value[0]["estado_produto"])
        html+= '''                                   
                </div>                
                <div class="check-img">
                    <img src="../image/check.png" alt="">
                    <p>100% Verificado</p> 
                </div> 
                
            </div>
            </div>
            <div class="detalhes-texto">
        '''
        html+= "<h1>%s</h1>"  %(value[0]["nome_produto"])
        html +=  "<h2>R$ {}</h2>" .format(value[0]["preco_produto"])
        html+= ''' <h3>Tamanho</h3>
            <div class="tamanho">
                <div>37</div>
                <div>38</div>
                <div>39</div>
                <div>40</div>
                <div>41</div>
                <div>42</div>
            </div>'''
        html += "<h2>Marca: %s</h2>" %(value[0]["marca_produto"])
        html+=   "<p class='descr'>%s<p>" %(value[0]["descricao_produto"])
        html+=    '''
                        
                <button>Adcionar ao carrinho</button>
                
            </div>
        </section>
            '''
        return html


class PageAnuncio():
    topo = open("template/topo.html").read()
    footer = open("template/footer.html").read()
    @cherrypy.expose()
    def index(self):
        return self.FormAnuncio()
    def FormAnuncio(self,fId_produto=0,fNome_produto='',fPreco_produto=0,fEstado_produto='',fDescricao_produto=''):
        html = self.topo
        html += '''<section class="conteudo-anuncio">                
        <div class="anuncio">
            <h1>Anunciar Produto</h1>
            <form action="InserirAnuncio" id="formAnuncio" method="post" enctype="multipart/form-data">
                <input type="hidden" name="id_produto" id="id_produto" value="{}" >
                <label for="nome_produto">Nome do Produto</label> 
                <input type="text" name="nome_produto" id="nome_produto" value='{}'>
                <label for="preco_produto">Preço do Produto</label>
                <input type="number" step=0.1 name="preco_produto" id="preco_produto" value='{}' ><br/>
                <label for="marca_produto">Marca do Produto</label>
                <select id="marca_produto" name="marca_produto"> ''' .format (fId_produto,fNome_produto,fPreco_produto)
        objMarca = Marcas()
        values = objMarca.ReadMarcas()
        for key in values:
             html+= "<option value='%s'>%s</option> " %(key["marca"], key["marca"])        
        
        html+= '''
            </select>
            <label for="estado_produto">Estado do Produto</label>
            <input type="text" name="estado_produto" id="estado_produto" value='{}'><br/>
            <label for="descricao_produto">Descrição do Produto</label><br/>
            <textarea name="descricao_produto" id="descricao_produto" cols="220" rows="9">{}</textarea><br/>
            <label class="foto" for="foto_produto">Foto do Produto</label><br/>
            <input type="file" name="foto_produto" id="foto_produto">
            <input type="submit" name="enviar" id"enviar" value="Enviar">
        </form>
        </div>
        </section>''' .format(fEstado_produto,fDescricao_produto)
        html += self.footer
        return html
    
    @cherrypy.expose()
    def AlterarAnuncio(self,id_produto): 
        objAnuncio = Anuncio()
        objAnuncio.set_id_produto(int(id_produto))
        values = objAnuncio.ReadAnuncio()
        return self.FormAnuncio(values[0]["id_produto"], values[0]["nome_produto"], values[0]["preco_produto"],values[0]["estado_produto"],values[0]["descricao_produto"])
    
        
        

    @cherrypy.expose()
    def InserirAnuncio(self,id_produto,nome_produto,preco_produto,marca_produto,estado_produto,descricao_produto,foto_produto,enviar):                        
        objAnuncio = Anuncio()        
        objAnuncio.set_nome_produto(nome_produto)
        objAnuncio.set_preco_porduto(str(preco_produto))
        objAnuncio.set_marca_produto(marca_produto)
        objAnuncio.set_estado_produto(estado_produto)
        objAnuncio.set_descricao_produto(descricao_produto)
        objAnuncio.set_foto_porduto(foto_produto.filename)
        upload_path = os.path.normpath(local_foto) 
        upload_file = os.path.join(upload_path, foto_produto.filename)                                
        foto = open(upload_file, 'wb') 
        flag = 1
        while flag != 0:
            data = foto_produto.file.read(8192)
            if not data:
                flag = 0
            foto.write(data)            
        foto.close
        retorno = 0

        if int(id_produto) == 0:
            retorno = objAnuncio.CreateAnuncio()                 
        else:
            objAnuncio.set_id_produto(int(id_produto))
            retorno = objAnuncio.UpdateAnuncio()            
        if retorno > 0:
            return '''
                    <script>
                        alert("O anuncio %s foi armazenado no banco de dados.");
                        window.location.href = "/pgAnuncio";
                    </script>
                ''' % (nome_produto)
        else:
            return '''
                    Erro ao armazenar o Anuncio <b>%s</b>.<br />
                    <a href="/">Voltar</a>         
                ''' % (nome_produto)
    
    
class PageCadastro():
    content = open("template/cadastrar.html").read()    
    @cherrypy.expose()
    def index(self):
        html = self.content          
        return html

class PageLogin():
    content = open("template/login.html").read()    
    @cherrypy.expose()
    def index(self):
        html = self.content          
        return html







class PageMarcas():
    topo = open("template/topo.html").read()
    footer = open("template/footer.html").read()
    @cherrypy.expose()
    def index(self):
        return self.Form()
    
    def Form(self,fId=0,fMarca = ""):
        html = self.topo
        html += '''      
        <section class="conteudo-anuncio">                
        <div class="anuncio">
            <h1>Cadastrar uma Marca</h1>
            <form name="formInserir" action="InserirMarca" method="post">            
                <label for="nome">Nome da marca</label> 
                <input type="hidden" id="id" name="id" value="%s" />
                <input type="text" name="marca" id="marca" value="%s" required>                            
                <br>
                <input type="submit" name="enviar" id"enviar" value="Enviar">
            </form>  
        </div>
        
        ''' % (fId, fMarca)
        html += self.ExibirMarca()
        html += '</section>'
        html += self.footer
        return html
    def ExibirMarca(self):
        html = '''<table class="alinha">
                    <tr>
                        <th>ID</th>
                        <th>Marca</th>
                        <th>Ação</th>
                    </tr>  '''
        
        objMarca = Marcas()
        values = objMarca.ReadMarcas()
        for key in values:
            html += "<tr>" \
                    "<td>%s</td>" \
                    "<td>%s</td>" \
                    "<td style='text-align:center'>[<a href='alterarMarca?id=%s'><img class='acao' src='../image/editar.png'></a>] " \
                    "[<a href='ExcluirMarca?id=%s'><img class='acao' src='../image/delete.png'></a>]" \
                    "</tr> \n" % (key["id"], key["marca"], key["id"], key["id"])

        html += "</table><br/>"
        return html

    @cherrypy.expose()
    def InserirMarca(self,id,marca,enviar):
        if len(marca) > 0:
            objMarca = Marcas()
            objMarca.set_marca(marca)
            retorno = 0

            if int(id) == 0:
                retorno = objMarca.CreateMarca()
            else:
                objMarca.set_id(int(id))
                retorno = objMarca.UpdateMarca()
            
            if retorno > 0:
                return '''
                    <script>
                        alert("A marca %s foi armazenado no banco de dados.");
                        window.location.href = "/pgMarcas";
                    </script>
                ''' % (marca)
            else:
                  return '''
                    Erro ao armazenar a marca <b>%s</b>.<br />
                    <a href="/">Voltar</a>         
                ''' % (marca)
        else:
           return '''
                O nome da marca precisa ser informado.<br />
                <a href="/">Voltar</a>
            '''
    
    @cherrypy.expose()
    def ExcluirMarca(self, id):
        objMarca = Marcas()
        objMarca.set_id(int(id))
        if objMarca.DeleteMarca() > 0:
            raise cherrypy.HTTPRedirect("/pgMarcas")
        else:
            '''
                 <p>Não foi possível excluir a Marca...<p>
                <p>[<a href="/">Voltar</a>]
            '''


    @cherrypy.expose()
    def alterarMarca(self,id): 
        objMarca = Marcas()
        objMarca.set_id(int(id))
        values = objMarca.ReadMarca(id)
        return self.Form(values[0]["id"], values[0]["marca"])

   
    

