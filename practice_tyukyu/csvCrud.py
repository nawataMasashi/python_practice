import csv
import pandas
from faker import Faker
import random
import pandas as pd
import os

csv_name = "testCsv.csv"
path = os.getenv('CSV_PATH')
csvPath = path + '\\' + csv_name

def csvCreate() :
    data = [] #データ挿入用配列
    col = ["名前", "メールアドレス", "住所", "年齢"] #カラム設定
    #書き込みデータ作成(100件作成)
    for count in range(1, 101) :
        fake = Faker("ja_jp")
        name = fake.name() #名前
        email = fake.email() #メールアドレス
        address = fake.address() #住所
        age = random.randint(1,100) #年齢
        #配列にデータを追加する
        data.append([name, email, address, age])
    #データフレーム作成
    csvData = pd.DataFrame(
        data = data,
        columns=col
    )
    #20歳以上の場合登録書き込みを行う
    csvData = csvData[csvData["年齢"] >= 20]
    #csvへ変換する
    csvData.to_csv(path + '\\' + csv_name, index=False)

def csvRead() :
    #作成したcsvを読み込む
    df = pd.read_csv(csvPath)
    #データを加工する(年齢でソート)
    df = df.sort_values("年齢")
    #ソートしたデータフレームをcsvへ書き込み
    df.to_csv(csvPath)



if __name__ == "__main__" :
    csvCreate()
    csvRead()