#  Inicie o servidor
import requests

url = "http://localhost:8000/myia/invoke"
data = {"question": "Quantos parâmetros tem o maior modelo Llama 3.1?"}

response = requests.post(url, json=data)
print(response.json())
