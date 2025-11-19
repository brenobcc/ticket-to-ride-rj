class Rota:
    def __init__(self, rota_id: int, cor: str, tamanho: int):
        self.rota_id = rota_id
        self.cor = cor
        self.tamanho = tamanho

        self.jogador = None   # Jogador que conquistou a rota
        self.cidade_origem = None
        self.cidade_destino = None