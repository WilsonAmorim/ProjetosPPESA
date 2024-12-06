from fasthtml.common import FastHTML, serve
import os
import getpass
import wmi
#teste = os.system('os.getlogin()')
#path = os.getlogin()
app = FastHTML()


path = os.path.join('..','Documents and Settings',getpass.getuser(),'Desktop')


@app.get("/")
def homepage():
    return f"<h1>Seu Usuário {path}</h1>"

serve()

# python -m http.server -b ::
