import couchdb
import database as db
import random
couch = couchdb.Server("http://admin:admin@194.195.246.167:5984/")

def DatabaseTest():
    # couch.create('everydaywords')
    # couch.create('technicalwords')
    # couch.create('simplepresenttense')
    # couch.create('presentcontinuous')
    # couch.create('simplepast')
    # couch.create('pastcontinuous')
    # couch.create('presentperfect')
    # couch.create('presentperfectcont')
    # couch.create('pastperfect')
    # couch.create('pastperfectcont')
    # couch.create('simplefuture')
    # couch.create('futurecont')
    # couch.create('futureperfect')
    return "OK."


#DatabaseTest()

#a = "AbAsdaw"
#print(a.lower())

ET = db.EngTime()

#print(ET.GameRegularVerb())

#for i in couch["technicalwords"]:
#    for doc in couch["technicalwords"].find({"selector":{"_id":i}}):
#        print(doc['word'])
