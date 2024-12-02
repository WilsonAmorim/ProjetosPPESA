import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234567',
    database='ppeconecao'
)

cursor = db.cursor()
lote ="SEC LOTE 02"
comando = 'SELECT count(sigla) FROM tborgaos WHERE tborgaosidtbConvenio = 3'


cursor.execute(comando)
meusdados = cursor.fetchall()
dados = str(meusdados)
print(dados )

# CRUD

# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


# READ
# comando = f'SELECT * FROM vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)


# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


