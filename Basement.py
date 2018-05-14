import pymongo
import requests
import json
from flask import Flask,request,render_template,session,jsonify
import sys,csv,re
from textblob import TextBlob,wordnet
from DataBase import Database


app=Flask(__name__)
app.secret_key="Vikram"
client=pymongo.MongoClient()
db=client['contentStore']
contentStore=db["StoreSentence"]
app_id = '553c5fda'
app_key = '28977489f79c280d4ec2e45c408e93ee'
language = 'en'



@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.before_first_request
def database_init():
    Database.initialize()

@app.route('/homepage', methods=['POST','GET'])
def show_results():
    match_sen=[]
    word_def=[]
    word_domain=[]
    wordname=request.form['wordname']
    session["wordname"]=wordname
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + wordname.lower()

    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

  #  print("code {}\n".format(r.status_code))
    store_json = json.loads(r.text)
    # print(store_json["results"][0]["lexicalEntries"][0]["entries"][0]["senses"])
    for s in store_json["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]:
        word_def=s["definitions"]
    #    word_domain=s["domains"]
    contents = [search['Data'] for search in contentStore.find({})]
    for content in contents:
        for s in content:
            if wordname in s:
                match_sen.append(s)
    return render_template('yourword.html', wordname = session['wordname'],list_sen=match_sen,w_def=word_def,w_domain=word_domain,loop=10)

if __name__=="__main__":
    app.run(debug=True)

