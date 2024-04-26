def repeat_key(key, length):
    if not key:
        raise ValueError("Key cannot be empty")
    return key * (length // len(key)) + key[:length % len(key)]


def apply_xor(text, key):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(text, key))


def XOR_cipher(text, key):
    repeated_key = repeat_key(key, len(text))
    ciphered_text = apply_xor(text, repeated_key)
    return ciphered_text


def XOR_uncipher(ciphered_text, key):
    repeated_key = repeat_key(key, len(ciphered_text))
    original_text = apply_xor(ciphered_text, repeated_key)
    return original_text


text = "Hello, world!"
key = "secret_key"

ciphered_text = XOR_cipher(text, key)
print("Зашифрованный текст:", ciphered_text)

original_text = XOR_uncipher(ciphered_text, key)
print("Расшифрованный текст:", original_text)
