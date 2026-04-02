# 📦 Sistema de Priorização de Pedidos Logísticos

## 🧠 1. Descrição

Este projeto consiste em uma solução em **Python** para **análise e priorização de pedidos logísticos**, utilizando estruturas de dados e conceitos de eficiência computacional.

A aplicação simula um cenário real de logística no Brasil, onde pedidos precisam ser organizados com base em critérios como:

* urgência
* tempo estimado de entrega
* status de pagamento
* quantidade de itens

O sistema realiza a leitura de um arquivo CSV, processa os dados e gera:

* uma fila priorizada de pedidos
* análises estruturadas
* visualizações gráficas

O foco principal é aplicar, na prática:

* estruturas de dados
* algoritmos de ordenação
* análise de complexidade (**Big O**)

---

## 🛠️ 2. Tecnologias

* Linguagem: **Python**
* Bibliotecas:

  * **pandas** (manipulação de dados)
  * **matplotlib** (visualização)
  * **collections.deque** (estrutura de fila)
* Interface: **terminal | (CLI)**

---

## 🎯 3. Funcionalidades principais

### 📥 Leitura e validação de dados

* Carrega dados a partir de um arquivo CSV
* Trata erro de caminho inválido com nova solicitação ao usuário

### 🔄 Transformação | de dados

* Converte `DataFrame` → lista → tuplas
* Organiza pedidos em um dicionário para acesso rápido por ID

### 🧮 Cálculo de prioridade

Cada pedido recebe um **score de prioridade** baseado em:

* nível de urgência (alta, média, baixa)
* tempo estimado de entrega
* status do pagamento
* quantidade de itens

### 📊 Ordenação e priorização

* Ordena os pedidos com base no score calculado
* Gera um ranking do mais prioritário para o menos prioritário

### 🚚 Simulação de fila de processamento

* Utiliza `deque` para simular uma fila de pedidos
* Processa pedidos na ordem de prioridade (FIFO baseado na ordenação)

### 📈 Visualização de dados

* Gráfico de distribuição de urgência
* Gráfico com os pedidos mais prioritários

---

## ⚙️ 4. Estrutura do código

### Estruturas de dados utilizadas

* **DataFrame** → armazenamento | inicial dos dados
* **Lista** → manipulação intermediária |
* **Tuplas** → representação imutável dos pedidos
* **Dicionário** → organização por ID
* **Deque** → simulação de fila

### Funções principais

* `carregar_dados(caminho)`
  Lê o CSV e trata erros de caminho com recursão ou loop

* `df_para_lista(df)`
  Converte DataFrame em lista

* `lista_para_tuplas(lista)`
  Converte lista em tuplas (imutabilidade)

* `criar_dicionario(lista_pedidos)`
  Organiza os pedidos em estrutura de dicionário

* `calcular_prioridade(pedido)`
  Calcula o score de prioridade (O(1))

* `priorizar_pedidos(lista_pedidos)`
  Aplica cálculo + ordenação (O(n log n))

* `criar_fila_priorizada(lista_ordenada)`
  Cria fila usando `deque`

* `processar_fila(fila)`
  Simula execução dos pedidos

* `gerar_graficos(df)`
  Gera visualizações com matplotlib

* `menu()`
  Orquestra todo o fluxo do sistema

---

## ⚡ 5. Eficiência e Big O

O sistema foi projetado considerando eficiência computacional:

| Etapa                 | Complexidade      |
| --------------------- | ----------------- |
| Leitura de dados      | O(n)              |
| Transformações        | O(n)              |
| Cálculo de prioridade | O(n)              |
| Ordenação             | **O(n log n)**    |
| Fila (`deque`)        | O(1) por operação |

### 🔥 Destaque

* Uso de **Timsort (sorted)** → eficiente para grandes volumes
* Uso de **deque** → remoção em tempo constante
* Estrutura geral otimizada para desempenho em escala

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/1IMperaDOR0/sistema-de-gestao-de-produtos
```

2. Acesse a pasta do projeto:

```bash
cd sistema-de-gestao-de-produtos
```

3. Instale as dependências:

```bash
pip install pandas matplotlib
```

4. Certifique-se de que o arquivo CSV está no caminho:

```
src/data/dados_logisticos.csv
```

5. Execute o programa:

```bash
python main.py
```

---

## 📈 7. Exemplo de uso

```
DataFrame:
[exibição dos dados carregados]

Dicionário de pedidos:
1: {cidade_destino: ..., produto: ...}

Top 5 pedidos priorizados:
Score: 9.5 | Pedido: (...)

Processamento de pedidos:
Processando pedido: (...)

[Gráficos exibidos]
```

---

## 👥 Integrantes

| Nome                                  | RM     |
|---------------------------------------|--------|
| Gabriel Alexandre Fukushima Sakura    | 99522  |
| Henrique de Oliveira Gomes            | 566424 |
| Henrique Kolomyes Silveira            | 563467 |
| Lucas Henrique Viana Estevam Sena     | 566246 |
| Matheus Santos de Oliveira            | 561982 |

---

## 📜 Licença

Este projeto é de uso acadêmico e educacional.