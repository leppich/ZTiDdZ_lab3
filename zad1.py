import base64

def encrypt_base64(text):
    text_bytes = text.encode('utf-8')
    encrypted_text = base64.b64encode(text_bytes)
    return encrypted_text.decode('utf-8')

original_text = input("Enter text: ")
encrypted_result = encrypt_base64(original_text)
print("Original Text:", original_text)
print("Encrypted Result:", encrypted_result)