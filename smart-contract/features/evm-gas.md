# 🚀 이더리움 구조: EVM과 가스 비용

## 🌍 이더리움(Ethereum)이란?
> - 이더리움은 탈중앙화 애플리케이션을 개발할 수 있는 블록체인 플랫폼이다
> - 비트코인과 달리 단순 결제 기능에 그치지 않고, 스마트 컨트랙트를 실행할 수 있다
> - 비탈릭 부테린이 갭라하였으며, 탈중앙화 금융(DeFi), NFT, DAO와 같은 다양한 프로젝트가 이더리움 위에서 운영된다

## 🛠️ 이더리움의 주요 구성 요소
### 1. EVM(Ethereum Virtual Machine)
- EVM(이더리움 가상머신)은 이더리움 네트워크에서 스마트 컨트랙트를 실행하는 환경이다
- EVM은 모든 노드에서 동일하게 작동하며, 스마트 컨트랙트가 블록체인에서 예측 가능하게 실행되도록 한다

### `EVM의 주요 역할`
1. 스마트 컨트랙트 실행
   - 스마트 컨트랙트 코드는 EVM 바이트코드로 변환되어 실행된다
   - Solidity로 작성된 코드를 EVM이 이해할 수 있는 언어로 컴파일한다
2. 탈중앙 컴퓨팅 환경
   - EVM은 각 노드에서 동일하게 동작하므로 스마트 컨트랙트는 네트워크 전체에서 동일한 결과를 보장한다
3. 안전한 실행 환경
   - 컨트랙트가 의도하지 않은 동작을 하지 않도록 격리된 환경에서 실행된다
   - 악의적인 코드도 블록체인 전체에 영향을 주지 않는다

### 2. 스마트 컨트랙트(Smart Contract)
- 스마트 컨트랙트는 EVM에서 실행되며, 조건이 충족되면 자동으로 트랜잭션을 수행한다
- 투표 시스템, 디지털 자산 관리, NFT 발행 등 다양한 용도로 사용된다

### 3. 트랜잭션(Transaction)
- 이더리움에서 상태(State)를 변경하는 작업은 트랜잭션을 통해 수행된다
- 트랜잭션은 EVM에서 실행되고, 결과는 블록체인에 기록된다

## ⛽️ 가스란?
### 1. 가스의 정의
- 가스는 이더리움 네트워크에서 트랜잭션을 실행하는 데 필요한 연산 비용이다
- 스마트 컨트랙트 실행, 토큰전송, DApp 사용 등 모든 작업에 가스가 소모된다

### 2. 가스의 역할
1. 네트워크 보호
   - 무한 루프 같은 악성 코드의 실행을 방지한다
   - 연산량에 따라 가스비가 부과되기 때문에 비효율적인 코드는 실행이 어렵다
2. 자원 사용량 측정
   - 트랜잭션이 네트워크 자원을 얼마나 사용하는지 측정한다
   - 복잡한 연산일수록 더 많은 가스를 필요로한다
3. 채굴자 보상
   - 트랜잭션을 처리하는 노드(채굴자/검증자)는 가스비를 보상으로 받는다
   - 높은 가스비를 지불하는 트랜잭션이 우선 처리된다 

### 3. 가스비 계산 방법
> 가스비 공식 : `가스비 = 가스 한도(gas limit) * 가스 가격(gas price)`
- 가스 한도(gas limit) : 트랜잭션에 사용할 최대 가스량
- 가스 가격(gas price) : 가스 1단위당 지불할 이더의 양(단위: Gwel)
- 1Gwel = 0.000000001 ETH

### 4. 가스비 최적화 방법
1. 효율적인 스마트 컨트랙트 작성
   - 중복 코드 제거
   - 루프안에서 상태 변경 최소화
   - 연산 비용이 큰 연산(스토리지 저장, 복잡한 연산) 피하기
2. 상태 변수 최소화
   - 상태 변수(State Variable)를 최소한으로 사용
   - 상태 변수는 EVM에서 가장 많은 가스를 소비
3. 호출 방식 변경
   - call 대신 delegatecall, staticcall 사용으로 가스비 절감 가능

### 5. 가스비 예측 및 조회
```python
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
w3 = Web3(Web3.HTTPProvider(infura_url))

# 현재 가스 가격 조회
gas_price = w3.eth.gas_price
print(f"Current Gas Price: {gas_price / 10**9} Gwei")
```

### 6. 가스비 절감 기술(Layer 2)
1. 레이어 2 솔루션
   - Optimism, Abitrum, zkSync 등은 이더리움 메인넷의 부하를 줄이고 가스비를 절감한다
   - 트랜잭션을 Layer 2에서 처리하고 최종 결과만 이더리움 메인넷에 기록한다
2. 롤업(Roll up)
   - 수백 개의 트랜잭션을 하나의 트랜잭션으로 묶어 가스비를 크게 절감한다
   - Optimistic Rollup과 zk-Rollup 방식이 대표적이다

## 결론
> - EVM은 스마트 컨트랙트 실행 환경이며, 가스비는 네트워크 유지 비용을 측정하고 불필요한 연산을 방지하는 역할을 한다
> - 스마트 컨트랙트를 설계 할 때에는 가스비 최적화가 매우 중요하다