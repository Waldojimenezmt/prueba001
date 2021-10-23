#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:44:43 2021

@author: waldo
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def index():
    name = "Bienvenidos al Index"
    return render_template('index.html', name=name)

@app.route('/info/')
def info():
    name = "Este mensaje sale de Info.html"
    return render_template('info.html', name=name)

if(__name__=='__main__'):
    app.run(debug=True, port=8000)