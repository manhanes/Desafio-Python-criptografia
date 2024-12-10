import os
import pyaes

try:
    # Nome do arquivo criptografado
    file_name = "teste.txt.encrypted"

    # Verifica se o arquivo existe
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"Arquivo {file_name} não encontrado.")

    # Lê os dados do arquivo
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Define a chave de descriptografia (idealmente, use um método seguro para armazená-la)
    key = b"testeransomwares"
    if len(key) not in [16, 24, 32]:
        raise ValueError("A chave deve ter 16, 24 ou 32 bytes.")

    # Descriptografa os dados
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    # Remove o arquivo original criptografado
    os.remove(file_name)

    # Escreve o arquivo descriptografado
    new_file_name = "teste.txt"
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypt_data)

    print(f"Arquivo descriptografado com sucesso: {new_file_name}")

except FileNotFoundError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
