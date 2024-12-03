from fasthtml.common import FastHTML, serve
import os
import getpass

#teste = os.system('os.getlogin()')
#path = os.getlogin()
usuario = getpass.getuser() 
app = FastHTML()

@app.get("/")
def homepage():
    return f"<h1>Seu Usuário {usuario}</h1>"

serve()

# python -m http.server -b ::
