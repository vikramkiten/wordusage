import pymongo
from flask import Flask

client=pymongo.MongoClient()
db=client['contentStore']
contentStore=db["StoreSentence"]

def finddata():
        gotlist=[]
        search_word=input("Enter the word to get sentence::")
        contents=[search['Data'] for search in contentStore.find({})]
        for content in contents:
                for s in content:
                        if search_word in s:
                                print(s)




finddata()