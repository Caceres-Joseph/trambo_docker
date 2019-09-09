from flask import Flask, render_template, request, redirect
from flask_restful import Resource, Api

app = Flask(__name__)


#+--------------------
# Index
#---------------------
@app.route("/")
def home():
    return render_template("index.html")



#+--------------------
# Insert data
#---------------------
@app.route('/handle_data', methods=['POST'])
def handle_data():
    fName = request.form['fName']
    print(fName)
    return redirect('/')
 

    # your code
    # return a response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

 