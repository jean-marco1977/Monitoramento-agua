# 💧 Sistema de Monitoramento Hidráulico Residencial
### Projeto Jean Marco Carneiro Turma FMO
`Python` `GitHub`

## 📝 Sobre o Projeto
Este é um script em **Python** desenvolvido para monitorar o nível de água em um reservatório e exibir alertas visuais coloridos diretamente no terminal de acordo com a situação atual.

O objetivo do sistema é auxiliar no controle hidráulico residencial ou industrial, permitindo uma rápida identificação visual de níveis críticos ou de alerta.

## 🧮 Lógica Utilizada
O sistema mapeia o status do reservatório através de uma estrutura de dados indexada de 1 a 5, onde cada nível corresponde a uma criticidade e uma cor específica no terminal:

*   **Nível 1:** Muito baixo (crítico) 🟥
*   **Nível 2:** Baixo 🟨
*   **Nível 3:** Médio 🟩
*   **Nível 4:** Alto 🟦
*   **Nível 5:** Muito alto (alerta) 🪟

*(Nota: O script utiliza a biblioteca `colorama` para renderizar as cores de forma nativa e multiplataforma no terminal).*

## 📂 Estrutura do Código
O programa foi construído com a seguinte lógica em Python (`App.py`):

```python
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
```

## 🚀 Como Executar o Programa

### Pré-requisitos
Antes de começar, você precisará ter o **Python 3.x** e a biblioteca **colorama** instalados em sua máquina.

Para instalar a dependência necessária, execute:
```bash
pip install colorama
```

### Passo a Passo

1. **Clone o repositório** (or baixe o arquivo `App.py`):
   ```bash
   git clone https://github.com/jean-marco1977/Monitoramento-agua
   ```
2. **Navegue até a pasta** do projeto:
   ```bash
   cd nome-do-repositorio
   ```
3. **Execute o script** pelo terminal ou prompt de comando:
   ```bash
   python Jean_Ag12_DS_I.py
   ```
4. **Interaja com a simulação** visualizando as mudanças de estado e alertas coloridos impressos em tempo real a cada segundo.
