from collections import Counter

def count() :
    '''ユーザーから入力を受け取り、各単語の出現回数をカウントするプログラムを作成してください。
例： "apple banana apple orange banana apple" → {'apple': 3, 'banana': 2, 'orange': 1}'''
    #入力を受け付ける
    user_input = input()
    #入力した文字をスペースで分割し、配列へ保存
    testList = user_input.split()
    #Countorで各要素ごとの数を参照する
    word_count = Counter(testList)
    for key, value in word_count.items():
        print(f"{key}: {value}")

def FizzBuzz() :
    '''1 から 100 までの数字をループし、
3 の倍数のとき "Fizz"
5 の倍数のとき "Buzz"
両方の倍数のとき "FizzBuzz"
それ以外のときは数字を出力するプログラムを作成してください。'''
    fizz = "Fizz"
    buzz = "Buzz"
    #1から100まで処理する
    for x in range(1, 101) :
        #3と5の倍数
        if x % 15 == 0:
            print(fizz + buzz)
        #3の倍数の場合
        elif x % 3 == 0:
            print(fizz)
        #5の倍数の場合
        elif x % 5 == 0:
            print(buzz)
        #それ以外の場合
        else :
            print(x)

if __name__ == "__main__" :
    FizzBuzz()
    count()
#push test
