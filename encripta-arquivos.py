import os
import pyaes

file_name = "teste.txt"

# Verifica se o arquivo existe
if not os.path.exists(file_name):
    raise FileNotFoundError(f"Arquivo {file_name} não encontrado!")

# Lê o conteúdo do arquivo
with open(file_name, "rb") as file:
    file_data = file.read()

# Gera uma chave de 16 bytes
key = os.urandom(16)
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografa os dados
crypto_data = aes.encrypt(file_data)

# Cria o arquivo criptografado
new_file = f"{file_name}.encrypted"
with open(new_file, "wb") as encrypted_file:
    encrypted_file.write(crypto_data)

# Exclui o arquivo original
os.remove(file_name)

print(f"Arquivo {file_name} foi criptografado e salvo como {new_file}.")
print(f"A chave de criptografia (hex): {key.hex()}")
