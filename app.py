import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/firebird")
def firebird_proxy():
    url = f"https://router.firebird.finance/aggregator/v1/route?{request.query_string.decode()}"

    res = requests.get(
        url=url,
        headers={
            'API-KEY': 'firebird_ramses_prod_200323'
        }
    )

    if res.status_code == 200:
        return jsonify(res.json())
    else:
        return res.text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
