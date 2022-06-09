
import requests
import re
import pandas as pd
from autoscraper import AutoScraper
from flask import Flask,render_template,request

app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data',methods=['GET','POST'])
def data():
    
    url = request.form['url']
    want_list =request.form['want_list']

    scrape_obj = AutoScraper()

    result = scrape_obj.build(url,want_list)
    data= request.form
    #print(result)
    return render_template('index.html', u_data=result)

  
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)