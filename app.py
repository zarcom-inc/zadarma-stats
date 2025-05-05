from flask import Flask, jsonify
from zadarma import ZadarmaAPI

app = Flask(__name__)

API_KEY = "70211b1629ec99473479"
API_SECRET = "0e299c732d3ab6c66c18"

api = ZadarmaAPI(API_KEY, API_SECRET)

@app.route("/")
def index():
    return "Zadarma API is working."

@app.route("/balance")
def get_balance():
    try:
        response = api.call('/v1/info/balance/')
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
