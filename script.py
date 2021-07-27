# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:40:01 2021

@author: Harini
"""
from flask import *  
app = Flask(__name__)  

@app.route('/')
def senti():
    return render_template('1.html')
@app.route('/result',methods = ['POST'])  
def resl():  
      text=request.form['text1']   
      if text:  
          r='fd'
          return render_template('t1.html',res=r)
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
    
    
    
#     <script>
# 	function myfn(){
# 	const ip=document.getElementById("text");
# 	if(ip){
# 	document.getElementById("res").innerHTML="positive";
# 	}}
#     </script>