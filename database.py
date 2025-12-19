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
        #Respeitar as conexões entre as tabelas
        cursor.execute('PRAGMA foreign_keys = ON;')

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

        #tabela Vendas
        cursor.execute("""
    create table if not exists vendas(
        id integer primary key autoincrement,
        cliente_id integer,
        data text,
        valor_real real,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)            
        )
""")
        #tabela itens_venda
        cursor.execute("""
    create table if not exists itens_venda(
                       id integer primary key autoincrement,
                       venda_id integer,
                       produto_id integer,
                       quantidade integer,
                       valor_unitario real,
                       FOREIGN KEY(venda_id) REFERENCES vendas(id),
                       FOREIGN KEY(produto_id) REFERENCES produtos(id)
                       )
""")

        self.conexao.commit()
        self.desconectar()


#Testando a classe Banco de Dados
if __name__ == "__main__":
    banco = BancoDeDados('techvendas.db')
    banco.criar_tabelas()

