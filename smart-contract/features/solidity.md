# 🚀 Solidity - 스마트 컨트랙트 핵심

## 🌍 Solidity란?
> - Solidity는 이더리움 블록체인에서 스마트 컨트랙트를 작성하기 위한 프로그래밍 언어이다
> - 비탈릭 부테린과 이더리움 개발팀이 설계했다
> - EVM에서 실행되며 스마트 컨트랙트, NFT, DeFi 등 다양한 블록체인 애플리케이션을 개발하는데 사용된다

## ❇️ Solidity의 특징
### 1. 이더리움 기반 스마트 컨트랙트 언어
- 이더리움 및 다양한 EVM 호환 블록체인에서 사용된다
- BNB Chain, Polygon, Avalanche 등도 Solidity 기반 스마트 컨트랙트를 지원한다

### 2. 객체 지향 언어
- JavaScript, Python, C++과 유사한 문법을 사용하여 개발자 친화적이다
- 상속, 라이브러리 사용 등 객체지향 프로그래밍(OOP) 기능을 포함하고 있다

### 3. 컴파일 언어
- Solidity 코드는 EVM 바이트코드로 컴파일되어 실행된다
- 작성된 컨트랙트는 Solc(Solidity Compiler)를 사용해 바이트코드와 ABI(Application Binary Interface)로 변환된다

### 4. 정적 타입 언어
- 데이터 타입이 정적(Static Type)으로 선언된다
- ex) unit, address, bool 등 데이터 타입을 명시적으로 선언해야한다

## 📦 Solidity 개발 환경 구축
### 1. 필수 설치 프로그램
- IDE : 코드 환경
- Node.js & npm : 패키지 관리
- Hardhat / Truffle : 스마트 컨트랙트 개발 프레임워크
- MetaMask : 이더리움 지갑
- Ganache : 로컬 블록체인

### 2. 프로젝트 초기화 (Hardhat)
```bash
mkdir my-contract
cd my-contract
npx hardhat
```
- Hardhat은 테스트 및 배포를 쉽게 도와주는 도구이다

## 🛠️ Solidy 기본 문법
### 1. 스마트 컨트랙트 기본 구조
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MyContract {
    uint public value;  // 상태 변수

    // 값 설정 (Setter)
    function setValue(uint _value) public {
        value = _value;
    }

    // 값 조회 (Getter)
    function getValue() public view returns (uint) {
        return value;
    }
}
```

### 2. 주요 키워드 설명
- `pragma solidity ^0.8.0;`: Solidity 버전 설정
- `contract`: 스마트 컨트랙트를 정의하는 키워드
- `public`: 외부에서 접근 가능한 함수 및 변수
- `view`: 상태를 변경하지 않고 조회만 하는 함수

### 3. 데이터 타입
```solidity
uint256 number = 100;           // 부호 없는 정수 (0 이상의 정수)
int256 temperature = -20;       // 부호 있는 정수
address owner = msg.sender;     // 지갑 주소
bool isActive = true;           // 불리언 값 (true/false)
string name = "Solidity";       // 문자열
```

### 4. 함수 작성
```solidity
function add(uint _a, uint _b) public pure returns (uint) {
    return _a + _b;
}
```
- `pure`: 상태를 변경하지 않고 입력값만 처리하는 함수
- `returns`: 반환 타입을 명시 

### 5. 이벤트와 트랜잭션 로그
```solidity
event Transfer(address indexed from, address indexed to, uint256 value);

function transfer(address _to, uint256 _amount) public {
    emit Transfer(msg.sender, _to, _amount);
}
```
- event는 트랜잭션 발생 시 블록체인 로그에 기록된다
- 프론트엔드에서 이벤틀르 감지해 UI 업데이트에 활용할 수 있다

## ❌ Solidity 개발 시 유의사항
### 1. 무한 루프 방지
- Solidity에서는 무한루프가 발생하면 전체 가스가 소모되어 트랜잭션이 실패한다
- 불필요한 for 루프는 피해야한다

### 2. 상태 변경 우선 순위
- 상태 변수는 트랜잭션 실행이 완료된 후에 변경된다
- state-changing 코드는 반드시 함수의 마지막 부분에 작성한다

##  📌 Solidity의 미래
> - Solidity는 블록체인의 핵심 언어로 자리잡고 있으며, 스마트 컨트랙트 및 디앱 개발의 표준이다.
> - EVM 호환 블록체인(BNB, Polygon)이 증가하면서 Solidity의 수요는 계속 증가하고 있다. 