from unittest.mock import patch
import requests

# APIにリクエストしフィボナッチ数を返す
def test_fib_api(n, api_url = 'https://redfawn62.sakura.ne.jp/fib?n='):
    url = f"{api_url}{n}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code

# フィボナッチ数を計算し返す
def calculation_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    print('正しい形式で呼び出したケースのテスト')
    for value in range(1, 101, 5):
        result = test_fib_api(value)
        if result['result'] == calculation_fib(value):
            print(f"n={value}->{result['result']}:success")
        else:
            print(f"n={value}->{result}:false")

    print('エラーケースのテスト')
    result = test_fib_api(0)
    if result == 400:
        print(f"n=0->Error Code{result}:success")
    else:
        print(f"n=0->Error Code{result}:false")
    
    result = test_fib_api(-1)
    if result == 400:
        print(f"n=-1->Error Code{result}:success")
    else:
        print(f"n=-1->Error Code{result}:false")
    
    result = test_fib_api(1, 'https://redfawn62.sakura.ne.jp/fib?m=')
    if result ==400:
        print(f"与えるキーがn以外の時Errorコード{result}:success")

    result = test_fib_api(1, 'https://redfawn62.sakura.ne.jp/fibo')
    if result ==404:
        print(f"APIのエンドポイントが間違っている時Errorコード{result}:success")
    


if __name__ == '__main__':
    main()
