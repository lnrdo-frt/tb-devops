

import requests
from bs4 import BeautifulSoup

url = "https://www.python.org"  # Você pode mudar para qualquer site
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    words = text.split()
    print(f"A página {url} contém aproximadamente {len(words)} palavras.")
else:
    print("Erro ao acessar a página.")