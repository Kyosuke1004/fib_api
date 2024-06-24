#!//usr/local/bin/python
# -*- coding: utf-8 -*-

# ライブラリのインポート
from flask import Flask, request, jsonify
import functions

app = Flask(__name__)

@app.route('/fib/')
def default():
    return jsonify({'status': 400, 'message': 'Please enter /fib?n=<number> at the end of the URL'})

@app.route('/fib', methods=["GET"])
def fib():
    # クエリパラメータのキーを取得
    query_keys = request.args.keys()
    # クエリパラメータが 'n' のみであることをチェック
    if set(query_keys) == {'n'}:
        n = request.args.get('n')
        # 与えられた変数が正の整数かチェック
        if functions.check_positive_int(n):
            result = functions.calculation_fib(int(n))
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