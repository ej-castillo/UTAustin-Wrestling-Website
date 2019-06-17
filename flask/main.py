import os
from flask import Flask

def create_app(test_config=None)
	app = Flask(__name__)

	@app.route("/"):
	def home():
		return 'Hello, world!'

if __name__ == "__main__":
	app,run(debug=True)