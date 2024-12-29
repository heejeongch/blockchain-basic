"""
- 이전 블록 해시
- 트랜잭션 데이터: 해당 블록에 저장될 트랜잭션
- 타임스탬프: 블록 생성 시간
- 현재 블록 해시: 현재 블록의 고유 해시값

- PoW: 난이도와 논스를 사용해 블록을 생성하는 데 연산 작업을 수행
- 다수 트랜잭션 처리: 한 블록에 여러 개의 트랜잭션을 포함
- 머클 트리: 트랜잭션을 해시화하여 머클 루트를 블록에 저장
"""
import hashlib
import time


"""
머클트리 생성 함수
- 트랜잭션 리스트를 해시화하고 해시를 쌍으로 묶어서 계속 합쳐나가며 최종적으로 머클루트 생성
- 트랜잭션이 홀수면 마지막 트랜잭션 복제해서 짝수로 만들어준다
- 머클 루트는 트랜잭션 무결성 보장함
"""
def merkle_root(transactions):
    if len(transactions) == 1:
        return transactions[0]

    # 짝수개가 아닐 경우에 마지막 트랜잭션을 복제해준다
    if len(transactions) % 2 != 0:
        transactions.append(transactions[-1])

    # 해시 쌍을 병합해 새로운 해시 생성해주기
    new_level = []
    for i in range(0, len(transactions), 2):
        new_hash = hashlib.sha256((transactions[i] + transactions[i + 1]).encode()).hexdigest()
        new_level.append(new_hash)

    return merkle_root(new_level)

class Block:
    def __init__(self, previous_hash, transactions, difficulty):
        # 이전 블록 해시
        self.previous_hash = previous_hash

        # 다수 트랜잭션 리스트
        self.transactions = transactions

        self.timestamp = time.time()
        self.difficulty = difficulty

        # 논스 초기화
        self.nonce = 0

        # 머클 루트 생성
        self.merkle_root = merkle_root(transactions)

        # 작업증명 수행 후 해시 저장
        self.hash = self.mine_block()

    # 블록 해시 계산 함수
    def calculate_hash(self):
        block_data = (f"{self.previous_hash}{self.merkle_root}{self.timestamp}{self.nonce}")
        return hashlib.sha256(block_data.encode()).hexdigest()

    """
    작업 증명 - 난이도에 맞는 해시 찾기
    - 난이도에 따라 특정 개수의 앞자리가 0인 해시값을 찾을때까지 논스를 반복 증가 시키면서 해시를 재계산
    - 채굴이 성공하면 논스와 해시값이 출력
    - 난이도가 높을수록 연산량이 증가하여 블록 생성이 더 오래 걸림 
    - 51% 공격 방지를 위함 
    """
    def mine_block(self):
        # 난이도에 따른 타겟 해시
        target = '0' * self.difficulty

        while True:
            self.nonce += 1
            calculated_hash = self.calculate_hash()

            if calculated_hash[:self.difficulty] == target:
                print(f"블록 채굴 성공!!! Nonce: {self.nonce}, Hash: {calculated_hash}")
                return calculated_hash

    def __str__(self):
        return (f"Block Data (Merkle Root): {self.merkle_root}\n"
                f"Transactions: {self.transactions}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Nonce: {self.nonce}\n"
                f"Hash: {self.hash}\n")

# 제네시스 블록 생성
def create_genesis_block(difficulty):
    return Block("0", ["Genesis Block"], difficulty)

# 새로운 블록 생성
def create_new_block(previous_block, transactions, difficulty):
    return Block(previous_block.hash, transactions, difficulty)

# 블록체인 초기화
difficulty = 4
blockchain = [create_genesis_block(difficulty)]

# 새로운 블록 추가 (다수 트랜잭션 포함)
new_block_1 = create_new_block(blockchain[-1], ["A -> B (10 BTC)", "B -> C (5 BTC)"], difficulty)
blockchain.append(new_block_1)

new_block_2 = create_new_block(blockchain[-1], ["C -> D (3 BTC)", "D -> E (8 BTC)"], difficulty)
blockchain.append(new_block_2)

# 블록체인 출력
for block in blockchain:
    print(block)
    print("-" * 60)