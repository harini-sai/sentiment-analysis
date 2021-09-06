# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:40:01 2021

@author: Harini
"""

#!pip install -q transformers
from transformers import pipeline
senti_pipeline=pipeline("sentiment-analysis")

from flask import *  
app = Flask(__name__)  

@app.route('/')
def senti():
    return render_template('1.html')
@app.route('/result',methods = ['POST'])  
def resl():  
      text2=request.form['text1']   
      if text2: 
          r=senti_pipeline(text2)
          return render_template('t1.html',res=r[0]['label'],scr=r[0]['score'])
  
if __name__ =="__main__":  
    app.run(host='127.0.0.1', port=8080, debug = True, use_reloader=False)  
    
    
    
    
