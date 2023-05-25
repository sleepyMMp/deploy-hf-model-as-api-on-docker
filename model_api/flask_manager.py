from flask import Flask
from flask import request
from models.load_model import Model

app = Flask(__name__)
model = Model()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/chat', methods=['POST'])
def qa():
    question = request.form.get("question")
    context = request.form.get("context")
    return model.predict(question, context)

app.run()