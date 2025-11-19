class Jogador:
    def __init__(self, jogador_id: int, nome: str, cor: str, trens_restantes: int, pontos: int):
        self.jogador_id = jogador_id
        self.nome = nome
        self.cor = cor
        self.trens_restantes = trens_restantes
        self.pontos = pontos

        self.cartas_vagao = []     # lista de CartaVagao
        self.Destinos = []         # lista de CartaDestino