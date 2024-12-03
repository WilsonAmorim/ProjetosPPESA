# importamos o módulo getpass
import getpass
 
def main():
  # vamos obter o nome do usuário logado no sistema
  usuario = getpass.getuser() 
   
  # e mostramos o resultado
  print("O usuário logado no momento é:", usuario)
  
if __name__== "__main__":
  main()