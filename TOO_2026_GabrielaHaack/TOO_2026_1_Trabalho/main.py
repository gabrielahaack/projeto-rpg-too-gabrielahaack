from model.heroi import Heroi
from model.missao import MissaoCaca, MissaoColeta, MissaoEntrega
from model.enums import ClasseHeroi, StatusMissao
 
 
def main():
    heroi = Heroi('Arthur', ClasseHeroi.GUERREIRO, 100, 100, 15, 5)
 
    caca = MissaoCaca('Lobos da Floresta', 'eliminar os lobos', 100, 5)
    coleta = MissaoColeta('Ervas Raras', 'coletar ervas medicinais', 40, 6)
    entrega = MissaoEntrega('Carta Real', 'entregar a carta ao rei', 60, 10)
 
    missoes = [caca, coleta, entrega]
 
    print('=== MISSÕES DISPONÍVEIS ===')
    for missao in missoes:
        print(missao.exibir_dados())
        # mesmo método, resultado diferente em cada tipo (polimorfismo)
        print(f'Recompensa agora: {missao.calcular_recompensa()} XP')
 
    print('\n=== CICLO COMPLETO DA MISSÃO DE CAÇA ===')
    print('--- Herói ANTES ---')
    print(heroi.exibir_dados())
 
    print()
    print(caca.iniciar_missao())
    print(f'Recompensa em andamento: {caca.calcular_recompensa()} XP')
    print(caca.concluir_missao(heroi))
    print(f'Recompensa após concluir: {caca.calcular_recompensa()} XP')
 
    print('\n--- Herói DEPOIS ---')
    print(heroi.exibir_dados())
 
    print('\n=== COMPLETANDO AS DEMAIS MISSÕES ===')
    for missao in missoes[1:]:
        print(missao.iniciar_missao())
        print(missao.concluir_missao(heroi))
 
    print('\n--- Herói no final ---')
    print(heroi.exibir_dados())
 
    print('\n=== TESTANDO ERROS ===')
    nova = MissaoColeta('Cogumelos', 'coletar cogumelos', 30, 3)
 
    # 1) pular etapa: concluir sem ter iniciado
    try:
        nova.concluir_missao(heroi)
    except ValueError as erro:
        print(f'Erro: {erro}')
 
    # 2) retroceder: voltar uma missão concluída para pendente
    try:
        caca.status = StatusMissao.PENDENTE
    except ValueError as erro:
        print(f'Erro: {erro}')
 
    # 3) status que não é do enum (texto livre)
    try:
        nova.status = 'EM ANDAMENTO'
    except TypeError as erro:
        print(f'Erro: {erro}')
 
main()
