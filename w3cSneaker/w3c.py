import cherrypy
import os
from classes.Pages import *

local_dir = os.path.dirname(__file__)

class Principal():
    @cherrypy.expose()
    def index(self):    
        return  '''<script>                        
                        window.location.href = "/pgHome";
                    </script>'''


local_config = {
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":local_dir},
}

root = Principal() 
root.pgHome = PageHome()
root.pgAnuncio = PageAnuncio() 
root.pgCadastrar = PageCadastro()
root.pgLogin = PageLogin()
root.pgDetalhes = PageDetalhes()
root.pgMarcas = PageMarcas()

cherrypy.quickstart(root,config=local_config)
