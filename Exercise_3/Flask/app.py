from flask import Flask, render_template, request, redirect
from flask_restful import Resource, Api
import redis

app = Flask(__name__)


#+--------------------
# Redis
#---------------------
#Connect 
r = redis.Redis(
    host='redis',
    port=6379 )

#Clear
r.flushdb()


#+--------------------
# Page 
#---------------------
@app.route("/")
def home():
    return render_template("index.html", data=r.scan_iter(), r=r )



#+--------------------
# Post method
#---------------------
@app.route('/handle_data', methods=['POST'])
def handle_data():
    dpi = request.form['dpi']
    name = request.form['name']
    r.set(dpi,name)
    return redirect('/')
 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=500)

 

