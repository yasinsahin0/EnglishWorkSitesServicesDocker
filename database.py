import couchdb

couch = couchdb.Server("http://admin:admin@194.195.246.167:5984/")


class EngTime():
    def __init__(self):

        self.wordDatabaseEvery = couch["everydaywords"]
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

    def addWordsEveryday(self,word,word2,word3,translate,image):
        doc = {"word":word,
               "word2":word2,
               "word3":word3,
               "translate":translate,
               "image":image}
        return self.wordDatabaseEvery.save(doc)

    def addWordsTechnical(self,word,word2,word3,translate,image):
        doc = {"word":word,
               "word2":word2,
               "word3":word3,
               "translate":translate,
               "image":image}
        return self.wordDatabaseTechnical.save(doc)

    def addSentenceSimplePresent(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectenceSPT.save(doc)

    def addSentencePresentContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectencePCT.save(doc)

    def addSentenceSimplePast(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectenceSPASTT.save(doc)

    def addSentencePastContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectencePCONTT.save(doc)

    def addSentencePresentPerfect(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectencePPT.save(doc)

    def addSentencePresentPerfectContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectencePPCT.save(doc)

    def addSentencePastPerfect(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectencePPERFT.save(doc)

    def addSentencePastPerfectContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectencePPCONTT.save(doc)

    def addSentenceSimpleFuture(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectenceSFT.save(doc)

    def addSentenceFutureContinuous(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectenceFCT.save(doc)

    def addSentenceFuturePerfect(self,sentence,translate,explanation,image):
        doc = {"sentence":sentence,
               "translate":translate,
               "explanation":explanation,
               "image":image}
        return self.sectenceFPT.save(doc)


ET = EngTime()
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
