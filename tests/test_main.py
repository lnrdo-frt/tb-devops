# tests/test_main.py
import pytest
from main import fetch_page, extract_word_count_from_html

def test_fetch_page_status_code():
    response = fetch_page("https://docs.github.com/en")
    assert response.status_code == 200

def test_fetch_page_invalid_url():
    response = fetch_page("https://url-invalida-que-nao-existe-abc123.com")
    assert response.status_code != 200

def test_extract_word_count_basic_html():
    html = "<html><body><p>Olá mundo</p></body></html>"
    count = extract_word_count_from_html(html)
    assert count == 2

def test_extract_word_count_empty_html():
    html = ""
    count = extract_word_count_from_html(html)
    assert count == 0

def test_extract_word_count_large_html():
    html = "<p>palavra </p>" * 100
    count = extract_word_count_from_html(html)
    assert count == 100
