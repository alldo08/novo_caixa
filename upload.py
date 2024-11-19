import requests

# URL onde você fará o upload do arquivo
url_upload = 'https://allldo.pythonanywhere.com/upload_db'

# Nome do arquivo local que você deseja fazer o upload
nome_arquivo_local = 'vendas.db'

# Abra o arquivo local para leitura binária
with open(nome_arquivo_local, 'rb') as arquivo:
    # Faça uma solicitação POST para o URL de upload, enviando o arquivo como um arquivo multipart
    response = requests.post(url_upload, files={'file': arquivo})

# Verifique se a solicitação foi bem-sucedida (código de status HTTP 200)
if response.status_code == 200:
    print("Arquivo de banco de dados enviado com sucesso.")
else:
    # Imprima uma mensagem de erro se a solicitação falhar
    print("Erro ao fazer upload do arquivo:", response.status_code)
