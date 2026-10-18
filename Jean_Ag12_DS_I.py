import time
from colorama import Fore, Style, init

# Inicializa o colorama (necessário para o funcionamento correto no Windows)
init()

# 1. Utilizando uma lista para armazenar as informações do reservatório
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]

# 2. Função responsável por definir a cor e exibir o alerta
def exibir_alerta(nivel_atual):
    """
    Busca o nível informado na lista, exibe a mensagem com a cor correspondente
    e restaura o estilo padrão do terminal.
    """
    encontrado = False
    
    for item in niveis_reservatorio:
        if item["nivel"] == nivel_atual:
            # Exibe a situação com a cor configurada e aplica o Style.RESET_ALL no final
            print(f"[MONITORAMENTO] Nível {item['nivel']}: {item['cor']}{item['situacao']}{Style.RESET_ALL}")
            encontrado = True
            break
            
    if not encontrado:
        print(f"[ERRO] Nível {nivel_atual} inválido para o sistema do reservatório.")

# 3. Simulação do ambiente real de monitoramento
if __name__ == "__main__":
    print("=== INICIANDO SISTEMA DE MONITORAMENTO HIDRÁULICO ===")
    print("Simulando oscilação do nível da água no reservatório...\n")
    
    # Lista de simulação (testando os níveis de 1 a 5 e um caso de erro)
    niveis_para_teste = [1, 2, 3, 4, 5, 4, 3]
    
    for nivel in niveis_para_teste:
        exibir_alerta(nivel)
        time.sleep(1)  # Pequena pausa de 1 segundo para simular o tempo real
        
    print("\n=== SIMULAÇÃO CONCLUÍDA ===")
    print("Sistema de monitoramento identificou nível da água em situação normal.")