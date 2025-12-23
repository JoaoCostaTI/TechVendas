from models import Cliente, Produto
from database import BancoDeDados

class ClienteDAO:
    def __init__(self):
        self.banco = BancoDeDados('techvendas.db')

    def salvar(self, cliente):
        #Conecta no Banco
        self.banco.conectar()

        #Cria o cursor
        cursor = self.banco.conexao.cursor()

        #Destrincha os dados do cliente em uma tupla
        dados_cliente = (cliente.nome, cliente.cpf, cliente.email)

        #Insere os valores na tabela clientes no banco
        cursor.execute('INSERT INTO clientes (nome, cpf, email) VALUES (?,?,?)', dados_cliente)

        cliente.id = cursor.lastrowid
        self.banco.conexao.commit()
        self.banco.desconectar()
    
    def listar_todos(self):
        self.banco.conectar()

        cursor = self.banco.conexao.cursor()

        cursor.execute('SELECT * FROM Clientes')

        clientes = cursor.fetchall()

        self.banco.desconectar()

        lista_clientes = []

        for c in clientes:
            cliente = Cliente(c[1], c[2], c[3], c[0])
            lista_clientes.append(cliente)

        return lista_clientes
    
class ProdutoDAO:
    def __init__(self):
        self.banco = BancoDeDados('techvendas.db')

    def salvar(self, produto):
        self.banco.conectar()
        cursor = self.banco.conexao.cursor()
        dados_produto = (produto.nome, produto.preco, produto.estoque)

        cursor.execute('INSERT INTO produtos (nome, preco, estoque) values(?,?,?)', dados_produto)

        produto.id = cursor.lastrowid
        self.banco.conexao.commit()
        self.banco.desconectar()

    def listar_todos(self):
        self.banco.conectar()
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        self.banco.desconectar()
        
        lista_produtos = []

        for p in produtos:
            produto = Produto(p[1], p[2], p[3], p[0])
            lista_produtos.append(produto)
        return lista_produtos

'''
dao = ClienteDAO()

# 1. Teste Salvar

c1 = Cliente("Bruno", "123.456", "bruno@email.com")

dao.salvar(c1)

print(f"Cliente salvo com ID: {c1.id}") # Se aparecer um número, venceu!

# 2. Teste Listar

todos = dao.listar_todos()

for c in todos:
    print(f'{c.id} - {c.nome} ({c.email})')
'''

produtos_dao = ProdutoDAO()
p1 = Produto('Pera', 12.99, 287)
produtos_dao.salvar(p1)

print(f'Produto salvo com ID {p1.id}')

todos = produtos_dao.listar_todos()

for p in todos:
    print(f"{p.id} - {p.nome} ({p.estoque})")

