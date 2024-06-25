import hashlib
from simplecrypt import encrypt, decrypt 
value = "Hi. What's up, dawg? Are you ok? Because I know a very good therapist."
def SHA256():
    result = hashlib.sha256(value.encode())
    print("SHA256 encrypted data: ", result.hexidigest())
SHA256()
def MD5():
    result = hashlib.md5(value.encode())
    print("MD5 encrypted data: ", result.hexidigest())
MD5()
message = "Hi. What's up, dawg? Are you ok? Because I know a very good therapist."
hex_string = ''
def encryption():
    global hex_string
    ciphercode = encrypt('BEWARE', message)
    hex_string = ciphercode.hex
    print("Encryption", hex_string)
def decryption():
    global hex_string
    byte_str = bytes.fromhex(hex_string)
    original = decrypt('BEWARE', message)
    final_message = original.decode("utf-8")
    print("Decryption", final_message)
encryption()
decryption()