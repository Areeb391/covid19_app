import flask
from flask import Flask,render_template,redirect,url_for
import requests
app=Flask('__main__',template_folder='template')

@app.route('/')
@app.route('/home')
def home():
    return redirect(url_for('covid'))

@app.route('/covid',methods=['POST','GET'])
def covid():
    worldwide_url="https://corona.lmao.ninja/v2/all"
    worldwide_content=requests.get(worldwide_url)
    worldwide_data=worldwide_content.json()
    
    return render_template('index.html',data=worldwide_data)


if __name__=='__main__':
    app.run(debug=True)
