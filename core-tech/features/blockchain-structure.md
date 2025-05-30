# 블록체인의 구조 - 블록과 체인의 구성요소
> 블록체인은 블록이라는 데이터 단위들이 체인 형태로 연결된 분산 원장 기술이다. 각 블록은 이전 블록과 해시로 연결되어 연속성과 보안성을 유지한다.

---

### 1. 블록의 기본 구조
1. 블록 헤더(Block Header): 블록의 메타데이터와 요약 정보
2. 블록 본문(Block Body): 트랜잭션 데이터
3. 해시(Hash): 이전 블록과 연결하는 고유 식별자

### 2. 블록 헤더(Block Header) - 블록의 핵심 메타데이터
- 버전: 블록의 소프트웨어 버전(규칙 및 합의 알고리즘)
- 이전 블록 해시: 이전 블록의 해시값(이전 블록과 연결)
- 머클 루트(Merkle Root): 블록 안 모든 트랜잭션의 해시값을 병합한 최종 해시값
- 타임스탬프: 블록이 생서된 시간
- 난이도 목표: 블록을 채굴하는 데 필요한 난이도 값
- 논스(Nonce): 블록 해시를 특정 조건에 맞추기 위해 사용되는 숫자(작업증명)

### 3. 블록 본문(Block Body) - 트랜잭션 데이터
- 블록의 본문에는 실제 트랜잭션 데이터가 포함된다.
- 트랜잭션은 누가 누구에게 얼마나 송금했는지 기록한 데이터이다.
- 하나의 블록 안에 여러 개의 트랜잭션이 존재할 수 있다.
- 예시
```json
{
    "from": "Alice",
    "to": "Bob",
    "amount": 1.5,
    "timestamp": 1700000000
}
```

### 4. 블록 간 해시 연결(Hash Linking)
- 블록체인에서 블록 간 연결은 해시를 통해 이루어진다.
- 각 블록은 이전 블록의 해시 값을 포함하고 있어, 체인이 끊어지지 않도록 보장된다.
- 이로 인해 블록을 조작하려면, 이전 모든 블록을 수정해야하므로 보안성이 매우높다. 
- 해시 연결 방식 예시: 각 블록은 이전 블록 해시를 포함하고, 새로운 블록이 생성될 때 마다 현재 블록의 해시가 다음 블록으로 전달된다.
```
블록 100
  이전 블록 해시: 00000000000009a7...
  머클 루트: 3f5c07...
  논스: 3498134

블록 101
  이전 블록 해시: 00000000000004b2...
  머클 루트: 7a1f08...
  논스: 8471248

블록 102
  이전 블록 해시: 00000000000007d3...
  머클 루트: b9a56c...
  논스: 5640183
```

### 5. 해시 연결의 보안성 - 위변조 방지 원리
- 블록체인은 단 하나의 블록을 수정하려면, 이후 모든 블록을 수정해야한다.
- 따라서 해킹이나 조작이 사실상 불가능하다.
  - 작업증명(Proof of Work): 새로운 블록을 생성하기 위해 팽대한 연산 작업이 필요하다.
  - 네트워크 과반수 공격(51% Attack): 체인을 조작하려면 네트워크의 과반수 이상 해시 파워가 필요하지만, 비용이 많이 들고 비효율적이다.

### 6. 머클 트리(Merkle Tree) - 트랜잭션 검증 구조
- 블록체인의 트랜잭션 데이터는 머클 트리라는 구조로 해시화됩니다.
- 모든 트랜잭션은 해시 값으로 변환된 뒤 서로 병합되어 최종적으로 머클 루트가 생성됩니다.
- 예시
  - 트랜잭션 1~4는 해시로 변환되고, 서로 병합되어 최종적으로 머클 루트를 형성한다.
  - 블록 헤더에는 머클 루트만 기록되므로, 데이터가 경량화되고 검증이 빠르게 이루어진다. 
```
        머클 루트 (abcd1234)
          /            \
     해시1(ab12)       해시2(cd34)
       /   \              /   \
 트랜잭션1  트랜잭션2  트랜잭션3  트랜잭션4
```

### 7. 블록체인의 데이터 검증 과정
1. 새 트랜잭션이 발생하면 이를 트랜잭션 풀에 임시 저장한다.
2. 블록 생성자는 트랜잭션을 모아 블록을 생성하고, 머클 트리를 통해 트랜잭션 무결성을 확인한다.
3. 생성된 블록은 네트워크에 브로드캐스트 된다. 
4. 모든 노드는 블록의 해시와 머클 루트를 검증하여, 유효성을 확인한 뒤 블록체인에 추가한다.

## Conclusion
> - 블록 헤더, 본문, 해시 연결을 통해 블록체인은 안전하고 위변조가 불가능한 데이터 구조를 형성한다.
> - 이 덕분에 블록체인은 금융 시스템, 공급망 관리, 투표 시스템 등에서 활용될 수 있다.
> - 신뢰할 수 있는 탈중앙화 시스템을 만들기 위해 블록체인은 데이터 무결성과 보안성을 최우선으로 한다. 