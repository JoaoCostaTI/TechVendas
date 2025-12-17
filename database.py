import sqlite3

class BancoDeDados():
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
        self.conexao = None
    
    def conectar(self):
        self.conexao = sqlite3.connect(self.nome_banco)
    
    def desconectar(self):
        if self.conexao:
            self.conexao.close()

    def criar_tabelas(self):
        self.conectar()
        cursor = self.conexao.cursor()

        #Tabela Clientes
        cursor.execute('CREATE TABLE IF NOT EXISTS clientes(' \
        'ID integer primary key autoincrement,' \
        'nome text,' \
        'cpf text,' \
        'email text)')

        #Tabela Produtos
        cursor.execute('CREATE TABLE IF NOT EXISTS produtos(' \
        'ID integer primary key autoincrement,' \
        'nome text,' \
        'preco real,' \
        'estoque integer)')

        self.conexao.commit()
        self.desconectar()

#Testando a classe Banco de Dados
if __name__ == "__main__":
    banco = BancoDeDados('techvendas.db')
    banco.criar_tabelas()
    
