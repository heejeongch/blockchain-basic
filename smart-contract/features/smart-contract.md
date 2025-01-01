# Smart Contract

## 🧾 스마트 컨트랙트란 ?
> - 스마트 컨트랙트는 블록체인에서 자동으로 실행되는 프로그램이다
> - 사람이 개입하지 않고 계약 조건이 충족되면 자동으로 실행된다
> - 중개인 없이 신뢰성 있는 거래를 가능하게하며, 투명성, 보안성, 자동화가 핵심이다
> - 블록체인에 배포되며, 변경이 불가능하고 투명하게 실행된다
> - 대표적으로 이더리움 블록체인에서 사용되며, NFT, DeFi(탈중앙화 금융), DAO 등 다양한 분야에서 활용된다

## 📦 스마트 컨트랙트 특장
### 1. 자동화 - Automation
- 특정 조건이 충족되면 자동으로 실행된다
- ex) A가 B에게 10ETH를 송금한다 라는 조건을 코드로 작성해, 조건 충족 시 자동 실행

### 2. 탈중앙화 - Decentralization
- 블록체인 위에 배포되므로 특정 기관이나 개인이 통제할 수 없다
- 모든 참여자가 동일한 상태를 확인하고 신뢰할 수 있다

### 3. 불변성 - Immutability
- 스마트 컨트랙트는 한 번 배포되면 코드가 수정 불가능하다
- 잘못된 코드를 배포할 경우 새로운 컨트랙트를 배포해야 한다

### 4. 투명성 - Transparency
- 블록체인에 배포된 스마트 컨트랙트는 누구나 소스 코드를 확인할 수 있다
- 모든 트랜잭션 기록이 공개적으로 조작이 불가능하다

## ☄️ 스마트 컨트랙트의 사용 사례
### 1. 금융 - Defi
- 중개인 없이 대출, 스테이킹, 이자 지급이 자동으로 이루어진다
- ex) AAVE, Compound, Uniswap

### 2. NFT
- 디지털 자산(그림, 음악, 게임 아이템 등)을 토큰화하고 소유권 증명을 제공한다
- ex) OpenSea, Axie Infinity

### 3. 공급망 관리
- 물류 및 제품 유통과정을 블록체인에 기록하여, 투명성과 추적성을 확보한다
- 물품이 지정된 장소에 도착했는지 자동 검증 및 결제 가능하다

### 4. 투표 시스템
- 선거 및 투표 시스템에서 부정 방지 및 투표 결과의 신뢰성을 보장한다

### 5. 탈중앙화 자율 조직 - DAO
- 코드로 운영되는 조직으로 스마트 컨트랙트로 거버넌스(의사결정)가 이루어진다
- 특정 제안에 대한 투표와 실행이 자동으로 진행된다 

## 📊 스마트 컨트랙트 작동방식
### 1. 스마트 컨트랙트 배포
- Solidity 등 스마트 컨트랙트 언어로 작성한 후 블록체인에 배포

### 2. 트랜잭션 요청
- 사용자는 MetaMask와 같은 블록체인 지갑을 통해 컨트랙트와 상호작용한다
- ex) ERC-20 토큰 전송, NFT 민팅 등

### 3. 블록체인 검증 및 실행
- 트랜잭션은 블록에 기록되고, 모든 노드가 컨트랙트를 실행해 상태를 업데이트 한다
- 가스비를 지불해야 스마트 컨트랙트가 실행된다

## 📟 스마트 컨트랙트 구현 예시
### 1. 간단한 스마트 컨트랙트
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleContract {
    uint public value;

    // 값 설정
    function setValue(uint _value) public {
        value = _value;
    }

    // 값 조회
    function getValue() public view returns (uint) {
        return value;
    }
}
```
- 기능 : 값을 저장하고 조회하는 간단한 스마트 컨트랙트

### 2. ERC-20 토큰 컨트랙트(기본 구조)
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyToken {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 18;
    uint public totalSupply = 1000000 * (10 ** uint(decimals));

    mapping(address => uint) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        return true;
    }
}
```
- 기능 : 간단한 ERC-20 토큰 발행
- `balanceOf` : 각 계정의 잔액 관리
- `transfer()` : 토큰 전송 기능

## ❇️ 스마트 컨트랙트 장단점
### 1. 장점
- 자동화 및 신뢰성 : 계약이 자동으로 실행되어 사기 및 오류 방지
- 비용 절감 : 중개인이 필요없어 비용이 절감됨
- 보안성 : 블록체인에 기록되어 변조 불가능
- 투명성 : 누구나 트랜잭션 기록을 조회할 수 있음

### 2. 단점
- 코드 오류 리스크 : 스마트 컨트랙트에 버그 발생 시 수정 불가
- 초기 개발 비용 : 고도로 숙련된 개발자가 필요
- 가스비 부담 : 복잡한 스마트 컨트랙트는 가스비가 많이 발생

## 💪🏼 스마트 컨트랙트 개발 시 보안 주의 사항
- Reentrancy Attack (재진입 공격) 방지
- Integer Overflow/Underflow 방지
- Access Control (접근 제어) 구현
- State Update 순서 조정 (값 업데이트 후 트랜잭션 실행)

## 결론
> - 스마트 컨트랙트는 탈중앙화 애플리케이션의 핵심
> - NFT, DeFi, DAO 등 다양한 분야에서 빠르게 확산되고 있음
> - 보안성과 효율성을 강화하는 방식으로 지속적으로 발전하고 있다