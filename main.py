

import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    return response

def extract_word_count_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    words = text.split()
    return len(words)

def main():
    url = "https://docs.github.com/en"
    response = fetch_page(url)

    if response.status_code == 200:
        word_count = extract_word_count_from_html(response.text)
        print(f"O site {url} possui cerca de {word_count} palavras.")
    else:
        print("Erro ao acessar a página.")

if __name__ == "__main__":
    main()
