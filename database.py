import couchdb
import random
couch = couchdb.Server("http://admin:admin@194.195.246.167:5984/")


class EngTime():
    def __init__(self):

        self.verbs = couch["verbs"]
        self.words = couch["technicalwords"]


    def addVerb(self,verb1,verb2,verb3,translate,verb_type,ex1,ex1t,ex2,ex2t,ex3,ex3t):
        doc = {"verb1":verb1.lower(),
               "verb2":verb2.lower(),
               "verb3":verb3.lower(),
               "translate":translate.lower(),
               "type":verb_type,
               "ex1":ex1,
               "ex1translate":ex1t,
               "ex2":ex2,
               "ex2translate":ex2t,
               "ex3":ex3,
               "ex3translate":ex3t}
        self.verbs.save(doc)
        return True


    def RandomVerbs(self,type):
        main_list = []
        database = couch["verbs"]
        for doc in database.find({"selector":{"type":type}}):
            main_list.append([doc["verb1"],
                   doc["verb2"],
                   doc["verb3"],
                   doc["translate"],
                   doc["type"],
                   doc["ex1"],
                   doc["ex1translate"],
                   doc["ex2"],
                   doc["ex2translate"],
                   doc["ex3"],
                   doc["ex3translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"verb1":main_list[rnd][0],
                   "verb2":main_list[rnd][1],
                   "verb3":main_list[rnd][2],
                   "translate":main_list[rnd][3],
                   "type":main_list[rnd][4],
                   "ex1":main_list[rnd][5],
                   "ex1translate":main_list[rnd][6],
                   "ex2":main_list[rnd][7],
                   "ex2translate":main_list[rnd][8],
                   "ex3":main_list[rnd][9],
                   "ex3translate":main_list[rnd][10]}
        return res_dict

    def controlVerb(self,verb):
        database = couch["verbs"]
        for doc in database.find({"selector":{"verb1":verb.lower()}}):
            return True
        return False

    def GameRegularVerb(self):
        try:
            onegame = self.RandomVerbs("regular")
            twogame = self.RandomVerbs("regular")
            treegame = self.RandomVerbs("regular")
            doc ={"verb":onegame['verb1'],
                  "t1":onegame['translate'],
                  "t2":twogame['translate'],
                  "t3":treegame['translate']}
            return doc
        except:
            docx={}
            return docx
        
    def GameirRegularVerb(self):
        try:
            onegame = self.RandomVerbs("irregular")
            twogame = self.RandomVerbs("irregular")
            treegame = self.RandomVerbs("irregular")
            doc ={"verb":onegame['verb1'],
                  "t1":onegame['translate'],
                  "t2":twogame['translate'],
                  "t3":treegame['translate']}
            return doc
        except:
            docx={}
            return docx

    def addWord(self,word,translate,ex1,ex1t,ex2,ex2t):
        doc = {"word":word.lower(),
               "translate":translate.lower(),
               "ex1":ex1,
               "ex1translate":ex1t,
               "ex2":ex2,
               "ex2translate":ex2t}
        self.words.save(doc)
        return True

    def RandomWord(self):
        main_list = []
        database = couch["technicalwords"]
        for i in database:
            for doc in database.find({"selector":{"_id":i}}):
                main_list.append([ doc["word"],
                                   doc["translate"],
                                   doc["ex1"],
                                   doc["ex1translate"],
                                   doc["ex2"],
                                   doc["ex2translate"]])
        rnd = random.randint(0,len(main_list)-1)
        res_dict ={"word":main_list[rnd][0],
                   "translate":main_list[rnd][1],
                   "ex1":main_list[rnd][2],
                   "ex1t":main_list[rnd][3],
                   "ex2":main_list[rnd][4],
                   "ex2t":main_list[rnd][5]}
        return res_dict

    def controlWord(self,word):
        for doc in self.words.find({"selector":{"word":word.lower()}}):
            return True
        return False

