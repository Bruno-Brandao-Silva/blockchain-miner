# Blockchain Miner

Este projeto implementa uma blockchain simples em Python, incluindo funções para minerar blocos, calcular hashes e verificar a integridade da cadeia. Além disso, ele fornece ferramentas para analisar estatísticas de mineração e realizar testes de integridade na blockchain.
![Captura de tela 2024-04-09 015007](https://github.com/Bruno-Brandao-Silva/blockchain-miner/assets/72681281/3f5f7ce6-02bf-4771-a036-baafc5dfffa4)
![Captura de tela 2024-04-09 015012](https://github.com/Bruno-Brandao-Silva/blockchain-miner/assets/72681281/ad6a47dc-99d2-40e3-96be-8832af9aca89)
![Captura de tela 2024-04-09 015030](https://github.com/Bruno-Brandao-Silva/blockchain-miner/assets/72681281/5db8bfc1-6143-43af-aaef-ee475195f1d9)

## Conteúdo

- [Blockchain Miner](#blockchain-miner)
  - [Conteúdo](#conteúdo)
  - [Sobre o Projeto](#sobre-o-projeto)
  - [Pré-requisitos](#pré-requisitos)
  - [Instruções de Uso](#instruções-de-uso)
  - [Funcionalidades](#funcionalidades)

## Sobre o Projeto

O projeto consiste em uma implementação básica de blockchain em Python, com classes para representar blocos e a blockchain em si. Ele inclui funções para minerar novos blocos com prova de trabalho (proof-of-work) e verificar a integridade da cadeia.

A blockchain é uma estrutura de dados distribuída e descentralizada, utilizada principalmente em criptomoedas como o Bitcoin, para manter um registro seguro e imutável de transações.

## Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Este projeto foi desenvolvido em Python 3.

Além disso, é necessário ter as bibliotecas `hashlib`, `time`, `json`, `statistics` e `matplotlib` instaladas. Você pode instalá-las via `pip`:

```bash
pip install matplotlib
```

## Instruções de Uso

1.Clone o repositório:

```bash
git clone https://github.com/seu-usuario/blockchain-miner.git
cd blockchain-miner
```

2.Execute o arquivo principal para analisar estatísticas da blockchain e realizar testes de integridade:

```bash
python blockchain.py
```

## Funcionalidades

- `Block`: Classe que representa um bloco na blockchain, com métodos para calcular o hash do bloco.
- `Blockchain`: Classe que mantém uma lista de blocos e oferece métodos para adicionar blocos, verificar a integridade da cadeia e minerar novos blocos.
- `proof_of_work`: Função que implementa o algoritmo de prova de trabalho para minerar um bloco com um determinado nível de dificuldade.
- `discover_blocks`: Função para descobrir os tempos de mineração de blocos para diferentes níveis de dificuldade e repetições.
- `blockchain_statistics_analysis`: Função para analisar estatísticas da blockchain, incluindo média de tempos de mineração, mediana e desvio padrão.
- `blockcain_integrity_test`: Função para testar a integridade da blockchain modificando manualmente os blocos e verificando se a cadeia permanece válida.
