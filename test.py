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

#ET = db.EngTime()

#print(ET.GameRegularVerb())

#for i in couch["technicalwords"]:
#    for doc in couch["technicalwords"].find({"selector":{"_id":i}}):
#        print(doc['word'])
ET = db.EngTime()
def games():
    onegame = ET.RandomVerbs("regular")
    doc = {"verb":onegame['verb1'],
           "real":onegame['translate']}
    listem = []
    listem.append(onegame['translate'])

    while len(listem)<4:
        while True:
            for i in listem:
                result = ET.RandomVerbs("regular")
                if i != result['translate'] and len(listem) < 4:
                    listem.append(result['translate'])
            break
    a = 0
    while True:
        a +=1
        rnd = random.randint(0,len(listem)-1)
        doc["t"+str(a)] = str(listem[rnd])
        listem.pop(rnd)
        if len(listem) ==0:
            break
    return doc



print(games())
print(games())
print(games())
print(games())
print(games())
print(games())
print(games())
print(games())

def GameRegularVerb():
    try:
        onegame = ET.RandomVerbs("regular")
        twogame = ET.RandomVerbs("regular")
        treegame = ET.RandomVerbs("regular")
        fourgame = ET.RandomVerbs("regular")

        doc ={"verb":onegame['verb1'],
              "real":onegame['translate']}

        secimlistem =[onegame['translate'],
                      twogame['translate'],
                      treegame['translate'],
                      fourgame['translate']]
        a = 0
        while True:
            a +=1
            rnd = random.randint(0,len(secimlistem)-1)
            doc["t"+str(a)] = str(secimlistem[rnd])
            secimlistem.pop(rnd)
            if len(secimlistem) ==0:
                break
        return doc
    except:
        docx={}
        return docx

