import pandas as pd
import pathlib
import glob
import os
from sqlalchemy import create_engine,text

#os.getcwd()
filepath = __file__ #現在実行中のファイルディレクトリを取得.pyまで
csvpath = "readCsv/"
username=os.getenv("SQL_USERNAME")
userpass=os.getenv("SQL_PASSWORD")

readPath = pathlib.Path(filepath).parent #現在のディレクトリのカレントディレクトリを取得

def dataSave () :
    #読み込みファイルのディレクトリを取得
    NPath = pathlib.Path(readPath / csvpath)
    #読み込みファイル名称を取得する
    All_file = NPath.glob('*')

    #sqlへ接続
    engine = create_engine(f"postgresql://{username}:{userpass}@localhost:5432/csvtest")

    #対象ファイルをすべて読み込む
    for file in All_file :
        #csvファイル読み込み
        Rcsv = pd.read_csv(file, encoding='UTF-8')
        #csvの行数だけ繰り返し
        for index, row in Rcsv.iterrows():
            #sql構文作成
            sqltxt = text(f"INSERT INTO csvsave (name, price, seller, debugger) VALUES ('{row['名称']}',{row['値段']},'{row['発売元']}','{row['開発者']}')")
            #DBへ接続
            with engine.begin() as connection:
                #SQLを実行
                connection.execute(sqltxt)
    engine.dispose

if __name__ == "__main__":
    dataSave()
