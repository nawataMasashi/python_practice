import requests

#API連携用URL
jsonApi = "https://jsonplaceholder.typicode.com/posts"


def apiRequests():
    try:
        #GETメソッドでリクエストを送信する
        response = requests.get(jsonApi)
        #ステータスコードを確認する(失敗・成功)
        print("StatusCode:", response.status_code)

        #ステータスコード200以外はエラーを表示
        if response.status_code != 200:
            print("APIリクエストに失敗しました")
            return
        
        #jsonのデータを取得する
        data = response.json()
        titles = []
        #二次元配列のため、配列分回す
        for title in data :
            #タイトルのみ取得
            titles.append(title['title'])
            print(title['title'])
    except requests.exceptions.Timeout:
        #タイムアウトした場合
        print("タイムアウト")
    except requests.exceptions.RequestException as e:
        #リクエストエラーが発生した場合
        print(f"リクエストエラーが発生しました: {e}")

if __name__ == "__main__" :
    apiRequests()