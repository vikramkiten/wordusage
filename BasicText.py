import sys
import csv
import re
import pymongo
from flask import Flask,render_template,request,session,jsonify


class SentenceExtract:
    client=pymongo.MongoClient()
    db = client["contentStore"]
    contentStore=db.StoreSentence
    getsentences=[]

    def extractsen(self):
        global getsentences
        global db
        getsentences = []
        getfile = open('csvffile.txt', 'r',encoding=('utf8'))
        getfilecontents = getfile.read()
        for x in getfilecontents.split('.'):
            getsentences.append(x)
        getfile.close()
        datasheet={"Book":"Think Fast and Slow","Author":"Dan Kahneman","Data":getsentences}
        SentenceExtract.db.StoreSentence.insert(datasheet)

    def json(self):
        return {
        "Book":"Thinking Fast and Slow",
        "Author":"Dane Kahneman",
        "Data":self.getsentences

        }

if __name__== "__main__":
    sa = SentenceExtract()
    sa.extractsen()





