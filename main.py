

import requests
from bs4 import BeautifulSoup


url = "https://docs.github.com/en"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()
    words = text.split()
    print(f"O site {url} possui cerca de {len(words)} palavras.")
else:
    print("Erro ao acessar a página.")