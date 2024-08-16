import requests
from bs4 import BeautifulSoup

# URLを設定
url = "https://www.hareruyamtg.com/ja/deck/1/metagame/"

# Webページにリクエストを送信
response = requests.get(url)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスからHTMLを取得
    html = response.content

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(html, "html.parser")

    # 必要なデータを取得（例として、タイトルを取得）
    title = soup.title.string
    print(f"Title of the page: {title}")

    # 特定のデータを取得（例として、特定のクラスを持つ要素を取得）
    data = soup.find_all("div", {"class": "specific-class"})
    for item in data:
        print(item.text)

else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
