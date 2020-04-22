from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return 'Junior Data Scientist * ( Data Engineering & Machine Learning ) Specialist'



if __name__=="__main__":
	app.run()