from flask import Flask
from flask_cors import CORS

import requests

app = Flask(__name__)

CORS(app)

@app.route("/")
def testApi():
  quote = requests.get("https://api.chucknorris.io/jokes/random")
  out = quote.json()["value"].replace("Chuck Norris", "Yael")
  return {"Fact about Yael": out}

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)