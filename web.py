# 晴れる屋のメタゲームにアクセスして分布を取得するプログラム
from bs4 import BeautifulSoup
import requests

url = "https://www.hareruyamtg.com/ja/deck/20/metagame/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")

# デッキ情報を抽出
decks = soup.find_all("li", class_="deckSearch-metaList__list__item")
for deck in decks:
    name = deck.find("span", class_="deckSearch-metaList__list__item__name").text
    count = deck.find("span", class_="deckSearch-metaList__list__item__count").text
    percent = deck.find("span", class_="deckSearch-metaList__list__item__percent").text
    print(f"{name}、{count}、{percent}")
