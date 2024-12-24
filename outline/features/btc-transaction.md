# 비트코인 트랜잭션 분석

## 비트코인 트랜잭션 기본 개념
- 트랜잭션: 비트코인 네트워크에서 자금을 송금하는 데이터 패킷
- 입력: 보내는 비트코인의 출처이자, 보유하고 있는 비트코인
- 출력: 비트코인을 수신할 대상 주소와 금액
- 잔돈: 남은 잔액을 자신에게 돌려받는 과정
- 수수료: 마이너에게 지급되는 트랜잭션 처리 비용

## 트랜잭션 데이터 확인 방법
1. Blockchain 탐색기 사용
    - Blockchain Explorer
    - Blockchair
    - 트랜잭션ID(TXID)를 입력해 트랜잭션의 세부 정보를 확인
2. [Blockchain.com](https://blockchain.com)에서 트랜잭션 분석하기
   - 예시 TXID (f854aebfa105b7197f6f9a2c7ad542e9e1fd23264b3d3c2c86f9a3d70b7c7792)
   ```json
   {
    "hash": "f854aebfa105b7197f6f9a2c7ad542e9e1fd23264b3d3c2c86f9a3d70b7c7792",
    "size": 225,
    "weight": 900,
    "block_height": 812345,
    "time": 1699998000
   }
   ```
   - hash: 트랜잭션의 고유 식별자
   - size: 트랜잭션의 데이터 크기(=byte)
   - block height: 해당 트랜잭션이 포함된 블록의 번호
   - time: 트랜잭션이 블록에 포함된 시간(unix 시간)
    ```json
    "inputs": [
      {
        "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
        "value": 0.5
      }
   ]
   ```
   - address: 송금자의 주소
   - value: 송금액
    ```json
   "outputs": [
      {
        "address": "bc1qdst8z7u6e04f9kmm9k9p7j0nr7mzmd5s5jjy65",
        "value": 0.48
      },
      {
        "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
        "value": 0.01
      }
    ]
    ```
   - address: 수신자의 주소
   - value(윗): 송금액 0.48
   - value(아래): 잔돈 0.01
3. 수수료 계산 
   > 수수료 = 입력 - 출력(합계)
4. 트랜잭션 분석 도구
    ```python
    from bitcoinrpc.authproxy import AuthServiceProxy
    
    # 비트코인 노드 연결
    rpc_user = "user"
    rpc_password = "password"
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332" % (rpc_user, rpc_password))
    
    # 트랜잭션 조회
    txid = "f854aebfa105b7197f6f9a2c7ad542e9e1fd23264b3d3c2c86f9a3d70b7c7792"
    tx = rpc_connection.getrawtransaction(txid, True)
    
    # 트랜잭션 정보 출력
    print(tx)
   ```
5. 트랜잭션 해석
   - 수수료가 높을수록 블록에 포함될 확률이 증가
   - 잔돈 처리: 송금 후 남은 금액은 다시 송금자의 지갑으로 돌아옴
   - UTXO 모델: 비트코인은 사용하지 않은 트랜잭션 출력을 사용해 트랜잭션을 생성
   - 미확인 트랜잭션: 트랜잭션이 블록에 포함되지 않으면 펜딩 상태
   - Confirm 횟수: 6회 이상의 확인이 이루어지면 트랜잭션이 안정적이라고 간주

## 결론
> 비트코인 트랜잭션은 투명성과 보안성을 기반으로 이루어집니다.
> 트랜잭션을 분석하면 송금 내역을 명확하게 파악할 수 있으며, 블록체인 탐색기와 코드 분석을 통해 깊이 있게 다를 수 있습니다. 