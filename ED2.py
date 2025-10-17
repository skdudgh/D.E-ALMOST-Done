import rsa
import chardet
from pathlib import Path

# RSA 키 생성 (1024비트)
public_key, private_key = rsa.newkeys(1024)

# 경로 설정
base_path = Path(__file__).parent / "information"
base_path.mkdir(exist_ok=True)

ed_path = base_path / "ED.txt"

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding'], raw_data

def encrypt():
    if not ed_path.exists():
        print("ED.txt file is not exist. type first.")
        return

    encoding, raw_data = detect_encoding(ed_path)
    try:
        content = raw_data.decode(encoding)
    except Exception as e:
        print(f"Encoding Error: {e}")
        return

    if not content.strip():
        print("There is nothing to enctypt.")
        return

    content_bytes = content.encode()
    max_length = 117
    encrypted_blocks = []

    for i in range(0, len(content_bytes), max_length):
        block = content_bytes[i:i+max_length]
        try:
            encrypted_block = rsa.encrypt(block, public_key)
            encrypted_blocks.append(encrypted_block)
        except Exception as e:
            print(f"Encryption failed: {e}")
            return

    # 암호화된 바이너리로 ED.txt 덮어쓰기
    with open(ed_path, 'wb') as f:
        for block in encrypted_blocks:
            f.write(len(block).to_bytes(2, 'big'))
            f.write(block)

    print("Encryption done: Saved in ED.txt")

def decrypt():
    if not ed_path.exists():
        print("ED.txt file is not exist. run encrypt() first.")
        return

    decrypted_bytes = b''
    with open(ed_path, 'rb') as f:
        while True:
            length_bytes = f.read(2)
            if not length_bytes:
                break
            block_length = int.from_bytes(length_bytes, 'big')
            block = f.read(block_length)
            try:
                decrypted_bytes += rsa.decrypt(block, private_key)
            except Exception as e:
                print(f"Decryption failed: {e}")
                return

    decrypted_text = decrypted_bytes.decode()

    # 복호화된 텍스트로 ED.txt 덮어쓰기
    ed_path.write_text(decrypted_text, encoding='utf-8')
    print("Decryption Done")

# 실행 예시
encrypt()
decrypt()
