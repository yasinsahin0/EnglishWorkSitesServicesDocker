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


@app.route('/addVerb', methods=['POST'])
def addVerb():
    verb1 = request.form["verb1"]
    verb2 = request.form["verb2"]
    verb3 = request.form["verb3"]
    translate = request.form[desc_translate]
    verbtype = request.form["verbtype"]
    ex1 = request.form["ex1"]
    ex1trans = request.form["ex1translate"]
    ex2 = request.form["ex2"]
    ex2trans = request.form["ex2translate"]
    ex3 = request.form["ex3"]
    ex3trans = request.form["ex3translate"]
    ET = database.EngTime()
    result = ET.addVerb(verb1,verb2,verb3,translate,
                        verbtype,ex1,ex1trans,ex2,ex2trans,ex3,ex3trans)
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

@app.route('/controlverb',methods=['POST'])
def controlverb():
    verb = request.form["verb"]
    ET = database.EngTime()
    result = ET.controlVerb(verb)
    if result:
        return "var"
    else:
        return "yok"

if __name__ == '__main__':
    app.run()
