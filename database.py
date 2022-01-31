import couchdb
import random
couch = couchdb.Server("http://admin:admin@194.195.246.167:5984/")


class EngTime():
    def __init__(self):

        self.wordDatabaseEvery = couch["everydaywords"]
        self.verbs = couch["verbs"]
        self.wordDatabaseTechnical = couch["technicalwords"]
        self.sectenceSPT = couch["simplepresenttense"]
        self.sectencePCT = couch["presentcontinuous"]
        self.sectenceSPASTT = couch["simplepast"]
        self.sectencePCONTT = couch["pastcontinuous"]
        self.sectencePPT = couch["presentperfect"]
        self.sectencePPCT = couch["presentperfectcont"]
        self.sectencePPERFT = couch["pastperfect"]
        self.sectencePPCONTT = couch["pastperfectcont"]
        self.sectenceSFT = couch["simplefuture"]
        self.sectenceFCT = couch["futurecont"]
        self.sectenceFPT = couch["futureperfect"]
        ### Descriptive
        self.word = "word"
        self.translate = "translate"
        self.sentence1 = "sentence1"
        self.sentence1Trans = "sentence1translate"
        self.sentence2 = "sentence2"
        self.sentence2Trans = "sentence2translate"
        self.image = "image"

    def addWordsEveryday(self,word,translate,sentence1,sentence1Trans,sentence2,sentence2Trans,image):
        doc = {self.word:word,
               self.translate:translate,
               self.sentence1:sentence1,
               self.sentence1Trans:sentence1Trans,
               self.sentence2:sentence2,
               self.sentence2Trans:sentence2Trans,
               self.image:image}
        self.wordDatabaseEvery.save(doc)
        return True
    def addVerb(self,verb1,verb2,verb3,translate,verbtype,ex1,ex1translate,ex2,ex2translate,explanation):
        doc = {"verb1":verb1,
               "verb2":verb2,
               "verb3":verb3,
               "translate":translate,
               "type":verbtype,
               "ex1":ex1,
               "ex1translate":ex1translate,
               "ex2":ex2,
               "ex2translate":ex2translate,
               "explanation":explanation}
        self.verbs.save(doc)
        return True
    def addWordsTechnical(self,word,word2,word3,translate,image):
        doc = {"word":word,
               "word2":word2,
               "word3":word3,
               "translate":translate,
               "image":image}
        self.wordDatabaseTechnical.save(doc)
        return True

    def addSentenceSimplePresent(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectenceSPT.save(doc)
        return True

    def addSentencePresentContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectencePCT.save(doc)
        return True

    def addSentenceSimplePast(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectenceSPASTT.save(doc)
        return True

    def addSentencePastContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectencePCONTT.save(doc)
        return True

    def addSentencePresentPerfect(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectencePPT.save(doc)
        return True

    def addSentencePresentPerfectContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectencePPCT.save(doc)
        return True

    def addSentencePastPerfect(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectencePPERFT.save(doc)
        return True

    def addSentencePastPerfectContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectencePPCONTT.save(doc)
        return True

    def addSentenceSimpleFuture(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectenceSFT.save(doc)
        return True

    def addSentenceFutureContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectenceFCT.save(doc)
        return True

    def addSentenceFuturePerfect(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        self.sectenceFPT.save(doc)
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
ET = EngTime()
print(ET.controlVerb("be"))
# ET.RandomVerbs("regular")
# print(ET.addWordsEveryday("a","b","c","d","e"))
# print(ET.addWordsTechnical("a","b","c","d","e"))
# print(ET.addSentenceSimplePresent("a","b","c","d"))
# print(ET.addSentencePresentContinuous("a","b","c","d"))
# print(ET.addSentenceSimplePast("a","b","c","d"))
# print(ET.addSentencePastContinuous("a","b","c","d"))
# print(ET.addSentencePresentPerfect("a","b","c","d"))
# print(ET.addSentencePresentPerfectContinuous("a","b","c","d"))
# print(ET.addSentencePastPerfect("a","b","c","d"))
# print(ET.addSentencePastPerfectContinuous("a","b","c","d"))
# print(ET.addSentenceSimpleFuture("a","b","c","d"))
# print(ET.addSentenceFutureContinuous("a","b","c","d"))
# print(ET.addSentenceFuturePerfect("a","b","c","d"))
