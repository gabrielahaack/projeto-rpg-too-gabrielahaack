from model.enums import StatusMissao
class Missao:
    _ORDEM = [
        StatusMissao.PENDENTE,
        StatusMissao.EM_ANDAMENTO,
        StatusMissao.CONCLUIDA,
    ]

    def __init__(self, nome, descricao, recompensa):
        if recompensa < 0:
            raise ValueError('A recompensa não pode ser negativa.')
        self.__nome = nome
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = StatusMissao.PENDENTE

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def recompensa(self):
        return self.__recompensa

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if not isinstance(novo_status, StatusMissao):
            raise TypeError('O status precisa ser um StatusMissao.')

        posicao_atual = self._ORDEM.index(self.__status)
        posicao_nova = self._ORDEM.index(novo_status)

        if posicao_nova == posicao_atual:
            raise ValueError(
                f'A missão {self.__nome} já está com o status {self.__status.value}.')
        if posicao_nova < posicao_atual:
            raise ValueError(
                f'Não é possível voltar de {self.__status.value} para {novo_status.value}.')
        if posicao_nova > posicao_atual + 1:
            raise ValueError(
                f'Não é possível pular etapas: de {self.__status.value} '
                f'direto para {novo_status.value}.')

        self.__status = novo_status

    def iniciar_missao(self):
        if self.status is StatusMissao.PENDENTE:
            self.status = StatusMissao.EM_ANDAMENTO
            return f'A missão {self.nome} começou! O objetivo é {self.descricao}.'
        else:
            return f'A missão {self.nome} já foi iniciada!!!'

    def calcular_recompensa(self):
        if self.status is not StatusMissao.CONCLUIDA:
            return 0
        return self.recompensa

    def concluir_missao(self, heroi):
        # 1º muda o status (se a transição for inválida, o setter levanta o
        # erro e o herói não recebe nada); 2º calcula e entrega o XP, pois a
        # recompensa só é paga com a missão já concluída.
        self.status = StatusMissao.CONCLUIDA
        xp = self.calcular_recompensa()
        heroi.ganhar_experiencia(xp)
        return f'Missão {self.nome} concluída! {heroi.nome} recebeu {xp} de XP.'

    def exibir_dados(self):
        msg = f'''
[{self.__class__.__name__}]
Nome: {self.nome}
Descrição: {self.descricao}
Recompensa: {self.recompensa}
Status: {self.status.value}
'''
        return msg

    def __str__(self):
        return f'missão [{self.__class__.__name__}]: {self.nome} | status: {self.status.value}'


class MissaoCaca(Missao):
    XP_POR_INIMIGO = 10

    def __init__(self, nome, descricao, recompensa, inimigos):
        super().__init__(nome, descricao, recompensa)
        if inimigos <= 0:
            raise ValueError('A missão de caça precisa ter ao menos 1 inimigo.')
        self.__inimigos = inimigos

    @property
    def inimigos(self):
        return self.__inimigos

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return base
        return base + self.inimigos * self.XP_POR_INIMIGO

    def exibir_dados(self):
        return super().exibir_dados() + f'Inimigos a derrotar: {self.inimigos}\n'


class MissaoColeta(Missao):
    XP_POR_ITEM = 5

    def __init__(self, nome, descricao, recompensa, itens):
        super().__init__(nome, descricao, recompensa)
        if itens <= 0:
            raise ValueError('A missão de coleta precisa ter ao menos 1 item.')
        self.__itens = itens

    @property
    def itens(self):
        return self.__itens

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return base
        return base + self.itens * self.XP_POR_ITEM

    def exibir_dados(self):
        return super().exibir_dados() + f'Itens a coletar: {self.itens}\n'


class MissaoEntrega(Missao):
    XP_POR_KM = 8

    def __init__(self, nome, descricao, recompensa, distancia_km):
        super().__init__(nome, descricao, recompensa)
        if distancia_km <= 0:
            raise ValueError('A distância da entrega precisa ser positiva.')
        self.__distancia_km = distancia_km

    @property
    def distancia_km(self):
        return self.__distancia_km

    def calcular_recompensa(self):
        base = super().calcular_recompensa()
        if self.status is not StatusMissao.CONCLUIDA:
            return base
        return base + self.distancia_km * self.XP_POR_KM

    def exibir_dados(self):
        return super().exibir_dados() + f'Distância: {self.distancia_km} km\n'


        
