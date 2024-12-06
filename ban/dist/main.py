from fasthtml.common import FastHTML, serve
import os


#teste = os.system('os.getlogin()')
path = os.getlogin()
#usuario = getpass.getpass() 
app = FastHTML()

@app.get("/")
def homepage():
    return f"<h1>Seu Usuário {path}</h1>"

serve()

# python -m http.server -b ::
