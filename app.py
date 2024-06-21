#!//usr/local/bin/python
# -*- coding: utf-8 -*-

# ライブラリのインポート
from flask import Flask, request, jsonify

# 与えられたn番目のフィボナッチ数を計算して返す
def calculation_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 変数がint型であり正の整数が代入されているか判定
def check_positive_int(value):
    if isinstance(value, int) and value > 0:
        return True
    return False

app = Flask(__name__)

@app.route('/fib', methods=["GET"])
def test():
    # クエリパラメータのキーを取得
    query_keys = request.args.keys()
    # クエリパラメータが 'n' のみであることをチェック
    if set(query_keys) == {'n'}:
        n = int(request.args.get('n'))
        if check_positive_int(n):
            result = calculation_fib(n)
            return jsonify({"result": result})
        else:
            return jsonify({"status": 400, "message": "n must be a positive integer."}), 400
    else:
        return jsonify({"status": 400, "message": "Query parameter key must be n only."}), 400


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"status": 404, "message": "Page not found."}), 404


if __name__ == '__main__':
    app.run()