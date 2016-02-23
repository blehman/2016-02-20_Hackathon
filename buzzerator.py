#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from flask import Flask, jsonify, render_template, request, url_for
import requests
import json
#from gnip_search_utilities import *
from simple_n_grams.simple_n_grams import *

app = Flask(__name__)
import sys
import codecs
import argparse
import fileinput
import copy
from datetime import *
import timeit
from time import sleep
from pprint import *
import ConfigParser



config = ConfigParser.RawConfigParser()
config.read('config.cfg')

@app.route('/csv/<filePath>/')
def get_csv_data(filePath):
    with open(filePath) as f:
        return json.dumps(f.read())

@app.route('/get_data/<hashtag>/<fromDate>/<toDate>/')
def get_some_data(hashtag,fromDate,toDate):
    rule = "love candy"
    parameters = {
            "query":'#'+hashtag
            ,"maxResults":"10"
            ,"fromDate":fromDate
            ,"toDate":toDate}
    def make_request(p):
        """
        Initiates a get request w/ specific parameters provided.
        """
        return requests.get(
                        config.get('creds','url')
                        , auth=(config.get('creds','user_name'), config.get('creds','password'))
                        , params=p
                        ).json()
    data = make_request(parameters)
    d = {}
    for rec in data['results']:
        d[rec['actor']['id'][15:]]=rec['actor']['displayName']
    return json.dumps(d)

@app.route('/')
def buzzing():
    return render_template('demo.html')
#practice
if __name__ == '__main__':
    app.run(debug=True,port=9090)



