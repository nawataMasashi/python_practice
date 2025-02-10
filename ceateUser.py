import pandas as pd
import numpy as np
from faker import Faker
import os
from sqlalchemy import create_engine,text, Integer, String

user_columns = ['id', 'name', 'age', 'email']
username=os.getenv("SQL_USERNAME")
userpass=os.getenv("SQL_PASSWORD")

def createuser() :
    #配列を定義
    data = []
    fk_jp = Faker("ja_JP") #日本語に変換
#    np.random.seed(42) #シード値を固定
    #配列にランダムに値を設定
    for i in range(1,10) :
        name = fk_jp.name() #名前をランダムに取得
        email = fk_jp.email() #メールアドレスをランダムに取得
        data.append([np.random.randint(1,100), name,np.random.randint(20,100),email])
    #データフレーム作成
    df = pd.DataFrame(
        data = data,
        columns = user_columns
    )
    #20歳以上の場合に登録する
    df = df[df["age"] >=20]
    #接続設定
    engine = create_engine(f"postgresql://{username}:{userpass}@localhost:5432/csvtest")
    #書き込み
    df.to_sql("users", con=engine, if_exists="append", index=False, dtype={"id": Integer(), "name":String(50), "age":Integer(), "email":String(100)})


if __name__ == "__main__" :
    createuser()