# 해시 함수와 암호화

## 1. 해시 함수(Hash Function)
> 해시 함수는 임의의 입력 데이터를 받아서 고정 길이 값(=해시 값)으로 변환하는 함수이다.
- 단방향성: 결과값(해시 값)으로부터 원래 데이터를 복원할 수 없다.
- 고유성: 서로 다른 입력 데이터는 거의 항상 다른 해시값을 갖는다.
- 고속성: 데이터 크기에 상관없이 빠르게 계산된다.
- 민감성: 입력 데이터가 조금만 변경되어도 완전히 다른 해시값이 나온다.

### SHA-256(Secure Hash Algorithm 256bit)
> SHA-256은 SHA-2 알고리즘의 한 종류로서, 256bit(32byte)의 해시 값을 생성하는 해시함수이다.
- 비트 길이: 256bit(64자리 16진수)
- 속도: 빠르고 효율적
- 보안성: 충돌(다른 입력이 같은 해시 값 생성) 가능성이 매우 낮다.
- 사용처
  - 비트코인 및 다양한 블록체인 네트워크에서 블록 해시 생성에 사용
  - 디지털 서명, 데이터 무결성 검증
- 예시
    ```python
    import hashlib
    
    data = "Hello, Blockchain!"
    hash_result = hashlib.sha256(data.encode()).hexdigest()
    print("SHA-256 Hash:", hash_result)
    ```
    ```bash
  # 출력값
  SHA-256 Hash: f0a7c5e863e1dba04f1db14493b6ea4e8c5ec01ad9ae10a4206e44e0b223849f
    ```

## 2. 암호화(Encryption)
> 암호화는 데이터를 암호문(ciphertext)으로 변환하여 비인가자가 내용을 해독하지 못하도록 하는 기술이다.
> 복호화(decryption)를 통해 암호문을 다시 원래의 데이터로 복원할 수 있다. 암호화는 크게 대칭키 임호화와 비대칭키 암호화로 나뉜다.

### RSA(Rivest Shamir Adleman) - 비대칭 암호화
> RSA는 공개키 암호화(Public Key Encryption) 알고리즘입니다.
- 비대칭 구조
  - 공개키(Public Key): 데이터를 암호화하는 데 사용된다.
  - 개인키(Private Key): 암호화된 데이터를 복호화하는 데 사용된다.
- 보안성: 큰 숫자의 소인수 분해가 어려운 수학적 문제에 기반하여 매우 안전하다.
- 속도: 대칭키 암호화보다 느리다. 하지만, 보안성이 매우 높아 중요한 데이터에 사용된다.
- 활용 분야
  - SSL/TLS (인터넷 보안 프로토콜)
  - 전자 서명
  - 블록체인 트랜잭션 서명
- 예시
    ```python
    from Crypto.PublicKey import RSA
    
    # 키 생성
    key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    private_key = key.export_key()
    
    print("Public Key:", public_key)
    print("Private Key:", private_key)
    ```

### ECC(Elliptic Curve Cryptography) - 비대칭 암호화
> ECC는 타원 곡선 암호화로 RSA보다 짧은 키 길이로도 동등한 보안 수준을 제공한다.
- 보안성: RSA보다 더 높은 보안성을 갖지만, 연산이 복잡하다.
- 속도: RSA보다 빠르고 효율적이어서 모바일이나 IoT 환경에 적합하다.
- 키 길이 차이: RSA 2048 비트 = ECC 256 비트 보안수준
- 활용분야
  - 비트코인 및 이더리움 지갑(ECDSA: 타원 곡선 디지털 서명 알고리즘)
  - 전자 서명
  - 스마트 계약(DeFi)
- 예시
  ```python
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives import serialization
    
    # 키 생성
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()
    
    # 키 출력
    print("Private Key:", private_key)
    print("Public Key:", public_key)
    ```

### RSA vs ECC 
|        | RSA           | ECC             |
|--------|---------------|-----------------|
| 키 길이   | 2048bit 이상    | 256bit          |
| 보안 수준  | ECC보다 낮음      | RSA보다 강력        |
| 속도     | 느림            | 빠름              |
| 연산 복잡도 | 쉬움            | 복잡              |
| 활용 분야  | 웹 보안, SSL/TLS | 암호화폐 지갑, 디지털 서명 |
| 실제 적용  | 대규모 시스템       | 모바일, IoT, 블록체인  |

## 결론
> - SHA-256: 데이터를 해시하는데 사용, 보안성과 속도가 뛰어나다
> - RSA: 비대칭 암호화의 대표적 기술, 주로 보안성이 중요한 분야에서 사용한다
> - ESS: RSA보다 짧은 키 길이로 높은 보안성을 제공, 특히 암호화폐와 모바일 환경에서 활발하게 사용한다.