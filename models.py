class Cliente:
    def __init__(self, nome, cpf, email, id = None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
    
class Produto:
    def __init__(self, nome, preco, estoque, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    #proteger preço
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, value):
        if value < 0:
            raise ValueError(f'Erro! Preço não pode ser negativo! ')
        self._preco = value
    
    #Proteger estoque
    @property
    def estoque(self):
        return self._estoque
    @estoque.setter
    def estoque(self, value):
        if value < 0:
            raise ValueError('Erro! Estoque não pode ser negativo! ')
        self._estoque = value

class Venda:
    def __init__(self, cliente_id, data, valor_total, id = None):
        self.id = id
        self.cliente_id = cliente_id
        self.data = data
        self.valor_total = valor_total

class ItemVenda:
    def __init__(self, venda_id, produto_id, quantidade, valor_unitario, id = None):
        self.id = id
        self.venda_id = venda_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario

try:
    p1 = Produto('Batata', -9.99, 10)
    print(p1)
except ValueError as e:
    print(e)