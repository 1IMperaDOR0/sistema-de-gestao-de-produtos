# Importando a biblioteca pandas para leitura do csv e criação do DataFrame
import pandas as pd

# Importando a biblioteca matplotlib para geração de gráficos
import matplotlib.pyplot as plt

# Importando a estrutura deque para simular fila de pedidos
from collections import deque


# Função responsável por carregar os dados do arquivo CSV
def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    return df


# Função que transforma o DataFrame em uma lista
def df_para_lista(df):
    return df.values.tolist()


# Função que transforma cada item da lista em tupla (estrutura imutável)
def lista_para_tuplas(lista):
    return [tuple(item) for item in lista]


# Função que organiza os pedidos em um dicionário para facilitar a busca por ID
def criar_dicionario(lista_pedidos):
    dicionario = {}

    for i, pedido in enumerate(lista_pedidos):
        id_pedido = i + 1

        dicionario[id_pedido] = {
            "cidade_destino": pedido[1],
            "produto": pedido[2],
            "categoria": pedido[3],
            "quantidade": pedido[4],
            "valor_unitario": pedido[5],
            "urgencia": pedido[6],
            "tempo_estimado_horas": pedido[7],
            "modal": pedido[8],
            "status_pagamento": pedido[9]
        }

    return dicionario


# Função que calcula a prioridade de um pedido com base em múltiplos critérios
def calcular_prioridade(pedido):
    # Convertendo urgência para valor numérico
    urgencia = {"alta": 3, "media": 2, "baixa": 1}[pedido[6]]

    # Definindo peso baseado no tempo estimado
    demora = 3 if pedido[7] > 15 else 2 if pedido[7] > 10 else 1

    # Verificando status de pagamento
    importancia = 2 if pedido[9] == "ok" else 1

    # Considerando quantidade como fator adicional
    quantidade = pedido[4] / 10

    # Retornando score final do pedido
    return urgencia * 2 + importancia * 2 + demora + quantidade


# Função que aplica o cálculo de prioridade em todos os pedidos
def priorizar_pedidos(lista_pedidos):
    lista_com_score = []

    for pedido in lista_pedidos:
        score = calcular_prioridade(pedido)
        lista_com_score.append((pedido, score))

    # Ordenando os pedidos do maior score para o menor
    lista_ordenada = sorted(lista_com_score, key=lambda x: x[1], reverse=True)

    return lista_ordenada


# Função que cria uma fila priorizada usando deque
def criar_fila_priorizada(lista_ordenada):
    fila = deque([pedido for pedido, _ in lista_ordenada])
    return fila


# Função que simula o processamento dos pedidos (remoção da fila)
def processar_fila(fila):
    while fila:
        pedido = fila.popleft()
        print(f"Processando pedido: {pedido}")


# Função responsável por gerar gráficos a partir dos dados
def gerar_graficos(df):
    # Gráfico de distribuição de urgência
    df['urgencia'].value_counts().plot(kind='bar')
    plt.title('Distribuição de Urgência')
    plt.xlabel('Urgência')
    plt.ylabel('Quantidade')
    plt.show()

    # Criando coluna de score baseada na função de prioridade
    df['score'] = df.apply(lambda row: calcular_prioridade(tuple(row)), axis=1)

    # Gráfico com os 5 pedidos mais prioritários (no caso todos)
    df.sort_values(by='score', ascending=False).head(5).plot(
        x='produto', y='score', kind='bar'
    )

    plt.title('Top 5 pedidos mais prioritários')
    plt.show()


# Função principal que executa todo o fluxo do sistema
def menu():
    caminho = 'src/data/dados_logisticos.csv'

    # Carregando os dados do CSV
    df = carregar_dados(caminho)
    print("\nDataFrame:\n", df)

    # Convertendo para lista
    lista = df_para_lista(df)

    # Convertendo para tuplas
    lista_tuplas = lista_para_tuplas(lista)

    # Criando dicionário de pedidos
    dicionario = criar_dicionario(lista_tuplas)
    print("\nDicionário de pedidos:")
    for k, v in dicionario.items():
        print(f"{k}: {v}")

    # Aplicando priorização
    lista_priorizada = priorizar_pedidos(lista_tuplas)

    print("\nTop 5 pedidos priorizados:")
    for pedido, score in lista_priorizada[:5]:
        print(f"Score: {score} | Pedido: {pedido}")

    # Criando fila baseada na prioridade
    fila = criar_fila_priorizada(lista_priorizada)

    # Simulando processamento da fila
    print("\nProcessamento de pedidos:")
    processar_fila(fila)

    # Gerando gráficos
    gerar_graficos(df)


# Executando o programa principal
if __name__ == "__main__":
    menu()