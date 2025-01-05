# 스마트 컨트랙트 취약점

> 스마트 계약의 보안은 블록체인 개발에서 가장 중요한 부분 중 하나이다. 특히 Reentrancy와 Overflow/Underflow는 
> 많은 해킹 사건에서 악용된 대표적인 취약점이다. 

## Reentrancy - 재진입 공격
> - Renntrancy는 스마트 계약이 외부 스마트 계약에 이더리움을 전송할 떄 발생할 수 있는 취약점이다.
> - 공격자가 함수를 반복적으로 호출하여 예상보다 많은 자금을 인출할 수 있게 만든다.

### 동작 방식
1. 사용자가 스마트 계약에서 이더리움을 출금 요청한다.
2. 스마트 계약은 사용자의 외부 계약(또는 지갑)으로 이더리움을 전송한다.
3. 외부 계약이 콜백 함수를 통해 다시 스마트 계약의 출금 함수를 호출한다.
4. 이 과정에서 스마트 계약이 출금 기록을 업데이트하기 전에 또 다른 출금이 이루어진다.

```solidity
pragma solidity ^0.8.0;

contract VulnerableContract {
    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "Insufficient funds");

        // ETH 전송
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // 출금 후 잔액 초기화
        balances[msg.sender] = 0;
    }
}
```

### 취약점 분석
- 잔액을 0으로 초기화하는 부분이 이더리움 전송 이후에 실행된다.
- 공격자는 재진입하여 여러 번 withdraw를 호출해 잔액이 0으로 초기화되기 전에 반복적으로 출금할 수 있다.

### 해결 방법
1. `Checks-Effects-Interactions` 패턴 적용: 상태를 먼저 변경한 후, 외부 호출을 진행한다.
2. `Reentrancy Guard` 사용: nonReentrant modifier를 사용해 재진입을 방지한다.
```solidity
function withdraw() public nonReentrant {
    uint256 amount = balances[msg.sender];
    require(amount > 0, "Insufficient funds");

    balances[msg.sender] = 0;

    (bool success, ) = msg.sender.call{value: amount}("");
    require(success, "Transfer failed");
}
```

## Overflow/Underflow 
> - Overflow: 변수 값이 최대값을 초과하여 다시 0부터 시작하는 현상
> - Underflow: 변수 값이 0보다 작아져 최대값으로 순환하는 현상

### 예시코드
```solidity
pragma solidity ^0.4.24;

contract OverflowExample {
    uint8 public value = 255;

    function increment() public {
        value += 1;  // 255 + 1 = 0 (Overflow 발생)
    }

    function decrement() public {
        value -= 1;  // 0 - 1 = 255 (Underflow 발생)
    }
}
```

### 취약점 분석
- uint8의 최대값은 255이다. 이 상태에서 1을 더하면 0으로 순환(Overflow)한다.
- value가 0일 때 decrement를 호출하면 255로 순환(Underflow)한다.

### 해결 방법
1. Solidity 0.8.x 이상 사용: 최선 버전의 Solidity는 기본적으로 오버플로우와 언더플로우를 감지하고 예외를 발생시킨다.
2. SafeMath 라이브러리 사용: 예전에는 SaftMath 라이브러리를 사용해 덧셈과 뺄셈을 안전하게 처리했다.

### 실제 해킹 사례
- The DAO 해킹(2016): Reentrancy 취약점을 악용해 약 260만 ETH가 탈취된 사건
- BatchOverflow 공격: ERC20 토큰의 오버플로우 취약점을 이용해 공격자가 무제한으로 토큰을 생성한 사례

## 결론
> - Reentrancy는 외부 호출 후 상태 업데이트를 지연시킬 때 발생한다. `Checks-Effects-Interactions` 패턴을 반드시 준수한다.
> - Overflow/Underflow는 최신 Solidity(0.8.x 이상)를 사용하면 기본적으로 방지된다.
> - 스마트 계약을 작성할 때는 항상 보안 감사를 진행하고, 잠재적인 취약점을 미리 대비하는 것이 중요하다. 