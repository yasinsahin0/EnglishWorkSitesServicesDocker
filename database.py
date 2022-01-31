import couchdb
import random
couch = couchdb.Server("http://admin:admin@194.195.246.167:5984/")


class EngTime():
    def __init__(self):

        self.verbs = couch["verbs"]

        ### Descriptive
        self.word = "word"
        self.translate = "translate"
        self.sentence1 = "sentence1"
        self.sentence1Trans = "sentence1translate"
        self.sentence2 = "sentence2"
        self.sentence2Trans = "sentence2translate"
        self.image = "image"


    def addVerb(self,verb1,verb2,verb3,translate,verbtype,ex1,ex1t,ex2,ex2t,ex3,ex3t,):
        doc = {"verb1":verb1,
               "verb2":verb2,
               "verb3":verb3,
               "translate":translate,
               "type":verbtype,
               "ex1":ex1,
               "ex1translate":ex1t,
               "ex2":ex2,
               "ex2translate":ex2t,
               "ex3":ex3,
               "ex3translate":ex3t,}
        self.verbs.save(doc)
        return True


    def RandomVerbs(self,type):
        listem = []
        a = 0
        database = couch["verbs"]
        for doc in database.find({"selector":{"type":type}}):
            a +=1
            lis = [doc["verb1"],doc["verb2"],doc["verb3"],doc["translate"],doc["type"],
                   doc["ex1"],doc["ex1translate"],
                   doc["ex2"],doc["ex2translate"],
                   doc["explanation"]]
            listem.append(lis)
        rnd = random.randint(0,len(listem)-1)
        parcaliste = listem[rnd]
        res_dict ={"verb1":parcaliste[0],
                   "verb2":parcaliste[1],
                   "verb3":parcaliste[2],
                   "translate":parcaliste[3],
                   "type":parcaliste[4],
                   "ex1":parcaliste[5],
                   "ex1translate":parcaliste[6],
                   "ex2":parcaliste[7],
                   "ex2translate":parcaliste[8],
                   "explanation":parcaliste[9]}
        return res_dict

    def controlVerb(self,verb):
        database = couch["verbs"]
        for doc in database.find({"selector":{"verb1":verb}}):
            return True
        return False
