from flask import Flask, jsonify, request

import database
import database as db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'

desc_word = "word"
desc_translate = "translate"
desc_sentence1 = "sentence1"
desc_sentence1Trans = "sentence1translate"
desc_sentence2 = "sentence2"
desc_sentence2Trans = "sentence2translate"
desc_image = "image"


@app.route('/test', methods=['POST'])
def test():
    return "test"


@app.route('/addWordsEveryday', methods=['POST'])
def addWordsEveryday():
    word = request.form[desc_word]
    translate = request.form[desc_translate]
    sentence1 = request.form[desc_sentence1]
    sentence1Trans = request.form[desc_sentence1Trans]
    sentence2 = request.form[desc_sentence2]
    sentence2Trans = request.form[desc_sentence2Trans]
    image = request.form[desc_image]
    ET = database.EngTime()
    result = ET.addWordsEveryday(word, translate, sentence1, sentence1Trans, sentence2, sentence2Trans, image)
    if not result:
        return "ex"
    else:
        return "ok"


@app.route('/addVerb', methods=['POST'])
def addVerb():
    verb1 = request.form["verb1"]
    verb2 = request.form["verb2"]
    verb3 = request.form["verb3"]
    translate = request.form[desc_translate]
    verbtype = request.form["verbtype"]
    exp = request.form["explanation"]
    ET = database.EngTime()
    result = ET.addVerb(verb1,verb2,verb3,translate,verbtype,exp)
    if not result:
        return "ex"
    else:
        return "ok"

@app.route('/randomverb',methods=['POST'])
def randomverb():
    verb_type = request.form["type"]
    ET = database.EngTime()
    result = ET.RandomVerbs(verb_type)
    return result
if __name__ == '__main__':
    app.run()
