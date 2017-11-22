from flask import Flask
app = Flask(__name__)
@app.route('/')
def root():
  return "Hello Napier!", 404
if __name__ == "__main___":
  app.run(host='0.0.0.0', debug=True)
