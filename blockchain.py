import hashlib
import time
import json
import statistics
import matplotlib.pyplot as plt


class Block:
    # Classe que representa um bloco da Blockchain
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Função para calcular o hash do bloco
        data = str(self.index) + str(self.timestamp) + \
            str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    # Classe que representa a Blockchain
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        # Função para adicionar um bloco na Blockchain
        self.chain.append(block)

    def get_previous_block(self):
        # Função para obter o último bloco da Blockchain
        return self.chain[-1]

    def is_valid_chain(self):
        # Função para verificar se a Blockchain é válida
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.calculate_hash():
                return False

        return True

    def mining_block(self, data, difficulty):
        # Função para minerar um bloco
        index = len(self.chain)
        timestamp = time.time()
        previous_hash = self.get_previous_block().hash if index > 0 else ""

        block = Block(index, timestamp, data, previous_hash)
        start_time = time.time()

        block = proof_of_work(block, difficulty)
        end_time = time.time()
        block_time = end_time - start_time

        print(f"\t\tBloco {block.index} encontrado em {block_time:.2f}s")
        self.add_block(block)
        return block_time

    def print_chain(self):
        # Função para imprimir a Blockchain
        for block in self.chain:
            print(json.dumps(block, default=lambda o: o.__dict__, indent=4))


def proof_of_work(block, difficulty):
    # Função para encontrar um nonce válido através do algoritmo de prova de trabalho (proof-of-work)
    while block.hash[:difficulty] != "0" * difficulty:
        block.nonce += 1
        block.hash = block.calculate_hash()

    return block


def discover_blocks(difficulty, num_blocks):
    # Função para descobrir os tempos de mineração de blocos para diferentes níveis de dificuldade
    blockchain = Blockchain()
    _time = 0

    for _ in range(num_blocks):
        data = "Block data"
        block_time = blockchain.mining_block(data, difficulty)
        _time += block_time

    return _time/num_blocks


def blockchain_statistics_analysis(max_difficulty, n, num_blocks):
    # Função para analisar estatísticas da Blockchain

    initial_time = time.localtime()
    mean_times = []
    median_times = []
    std_deviations = []
    all_times = []

# Loop para diferentes níveis de dificuldade
    for j in range(1, max_difficulty+1):
        times = []
        print(f"Dificuldade: {j}")
# Loop para executar a descoberta de blocos n vezes
        for i in range(n):
            print("\tConjunto ", i+1, ":")
            times.append(discover_blocks(j, num_blocks))

        mean_time = statistics.mean(times)
        median_time = statistics.median(times)
        std_deviation = statistics.stdev(times)

        mean_times.append(mean_time)
        median_times.append(median_time)
        std_deviations.append(std_deviation)
        all_times += times
        print(f"Tempo médio: {mean_time:.2f}s")
        print(f"Mediana de tempo: {median_time:.2f}s")
        print(f"Desvio padrão: {std_deviation:.2f}s")

# Plotagem dos gráficos
    axis_x_parity = [i for i in range(1, max_difficulty+1) for _ in range(n)]
    axis_x = [i for i in range(1, max_difficulty+1)]

    _, ax1 = plt.subplots()
    ax1.plot(axis_x_parity, all_times, marker='o')
    ax1.set_xlabel('Dificuldade')
    ax1.set_ylabel('Tempo')
    ax1.set_title('Gráfico de tempo por dificuldade')
    ax1.set_xticks(range(1, max_difficulty+1, 1))

    _, ax2 = plt.subplots()
    ax2.plot(axis_x, mean_times, label='Média')
    ax2.plot(axis_x, median_times, label='Mediana')
    ax2.plot(axis_x, std_deviations, label='Desvio padrão')
    ax2.set_xlabel('Dificuldade')
    ax2.set_ylabel('Tempo')
    ax2.set_title('Gráfico de tempo por dificuldade')
    ax2.legend()
    ax2.set_xticks(range(1, max_difficulty+1, 1))

# Print de informações sobre a execução
    final_time = time.localtime()
    print("inicio: ", time.strftime("%d/%m/%Y %H:%M:%S", initial_time))
    print("termino: ", time.strftime("%d/%m/%Y %H:%M:%S", final_time))
    print(f"duracao:  {time.mktime(final_time) - time.mktime(initial_time)}s")
    plt.show()

    with open('statistic.csv', 'w') as f:
        f.write('Dificuldade,Tempo Medio,Mediana de Tempo,Desvio Padrao\n')
        for i in range(len(axis_x)):
            f.write(
                f'{axis_x[i]},{mean_times[i]},{median_times[i]},{std_deviations[i]}\n')
    with open('data.csv', 'w') as f:
        f.write('Dificuldade,Tempo\n')
        for i in range(len(axis_x_parity)):
            f.write(f'{axis_x_parity[i]},{all_times[i]}\n')


def blockcain_integrity_test(print_chain=False):
    # Função para testar a integridade da Blockchain

    # Criando Blockchain válida
    print("Criando Blockchain válida...")
    blockchain = Blockchain()
    blockchain.mining_block("Block 1", 4)
    blockchain.mining_block("Block 2", 4)
    blockchain.mining_block("Block 3", 4)
    if print_chain:
        blockchain.print_chain()
    print("Blockchain válida? ", blockchain.is_valid_chain())

# Teste 1 modificando manualmente o primeiro bloco
    print("Alterando manualmente bloco 1...")
    blockchain.chain[0].data = "Block 5"
    if print_chain:
        blockchain.print_chain()
    print("Blockchain válida? ", blockchain.is_valid_chain())

# Criando Blockchain válida
    print("Criando Blockchain válida...")
    blockchain = Blockchain()
    blockchain.mining_block("Block 1", 4)
    blockchain.mining_block("Block 2", 4)
    blockchain.mining_block("Block 3", 4)
    if print_chain:
        blockchain.print_chain()
    print("Blockchain válida? ", blockchain.is_valid_chain())

# Teste 2 modificando manualmente o bloco do meio
    print("Alterando manualmente bloco 2...")
    blockchain.chain[1].data = "Block ???"
    if print_chain:
        blockchain.print_chain()
    print("Blockchain válida? ", blockchain.is_valid_chain())


# Criando Blockchain válida
    print("Criando Blockchain válida...")
    blockchain = Blockchain()
    blockchain.mining_block("Block 1", 4)
    blockchain.mining_block("Block 2", 4)
    blockchain.mining_block("Block 3", 4)
    if print_chain:
        blockchain.print_chain()
    print("Blockchain válida? ", blockchain.is_valid_chain())

# Teste 3 modificando manualmente o último bloco
    print("Alterando manualmente bloco 3...")
    blockchain.chain[2].data = "Block 2345"
    if print_chain:
        blockchain.print_chain()
    print("Blockchain válida? ", blockchain.is_valid_chain())


# Executa a análise de estatísticas da Blockchain (max_difficulty, n, num_blocks)
blockchain_statistics_analysis(5, 15, 15)

# Executa o teste de integridade da Blockchain (opcional boolean print_chain)
blockcain_integrity_test(print_chain=True)
