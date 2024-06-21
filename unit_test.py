import unittest
from unittest.mock import patch
import requests

# ここでは、Fibonacci APIのエンドポイントを仮定しています。
API_URL = "https://redfawn62.sakura.ne.jp/fib?n="

def get_fibonacci(n):
    response = requests.get(f"{API_URL}/{n}")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

class TestFibonacciAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_fibonacci_success(self, mock_get):
        # モックのレスポンスを設定します
        mock_response = unittest.mock.Mock()
        expected_json = {'result': [0, 1, 1, 2, 3, 5]}  # 例としてn=5のFibonacci数列を返すと仮定
        mock_response.status_code = 200
        mock_response.json.return_value = expected_json
        mock_get.return_value = mock_response

        # 実際の関数を呼び出してテストします
        n = 5
        result = get_fibonacci(n)
        self.assertEqual(result, expected_json)

    @patch('requests.get')
    def test_get_fibonacci_failure(self, mock_get):
        # モックのレスポンスを設定します（エラーの場合）
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
        mock_get.return_value = mock_response

        # エラーハンドリングをテストします
        n = 5
        with self.assertRaises(requests.exceptions.HTTPError):
            get_fibonacci(n)

if __name__ == '__main__':
    unittest.main()
