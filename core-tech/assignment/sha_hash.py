import hashlib


def sha256_hash(data):
    # sha256 객체 생성
    sha256 = hashlib.sha256()

    # 데이터를 바이트로 인코딩해서 업데이트
    sha256.update(data.encode('utf-8'))

    # 해시 결과를 16진수로 변환
    return sha256.hexdigest()


def sha512_hash(data):
    # sha512 객체 생성
    sha512 = hashlib.sha512()
    sha512.update(data.encode('utf-8'))

    return sha512.hexdigest()

def sha256_file(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()

data4sha256 = "This is data to encode sha256 hash"
data4sha512 = "This is data to encode sha512 hash"
sha_256_hash_result = sha256_hash(data4sha256)
sha_512_hash_result = sha256_hash(data4sha512)
print(f'{data4sha256}의 sha 256 해시값 : {sha_256_hash_result}')
print(f'{data4sha512}의 sha 256 해시값 : {sha_512_hash_result}')