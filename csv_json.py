from flask import Flask, render_template, request
import requests
import csv
import json

app = Flask(__name__)

@app.route('/convert', methods=['POST'])

def convert():
    fname1 = request.form['path1']
    fname2 = request.form['path2']
    name = request.form['name']
    j = []

    
    f1 = open (fname1,'rU')
    f2 = open (fname2,'w')
    c = 0
    d = 0    
    
    reader = csv.DictReader(f1, delimiter=",", lineterminator='\n')
    

    for row in reader :
        del(row[" timestamp"])
        del(row["Pressure"])
        del(row["Humidity"])
        del(row["Temperature"])
        del(row[""])
        row["Station"]=name
        j.append(row)
        c=c+1
    
    
    for row in j : 

        json.dump(row,f2)
        
        if(d!=c-1):
           
            f2.write(',')
        
        f2.write('\n')
        d=d+1
    
    
    tempf="JSON Parsed! Path of Parsed JSON File --> " + fname2 
    return render_template('json.html', temp=tempf)

@app.route('/')

def index1():
	
    return render_template('index.html')

if __name__ == '__main__':
    
    app.run(debug=True)