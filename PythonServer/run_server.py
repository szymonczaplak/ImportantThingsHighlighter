from extractor import ImportantThingsExtractor
import flask
from flask import request, jsonify, after_this_request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
extractor = ImportantThingsExtractor()

@app.route('/', methods=['POST'])
def hello():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    try:
        content = request.json
    except:
        raise Exception("error while json parsing")
    with open('content.json', 'w+', encoding='utf-8', errors='ignore') as f:
        f.write(str(content))
    try:
        important_things = extractor.extract(content['html'])
    except:
        raise Exception("error while extracting")

    jsonResp = {'important_things': important_things}
    print(jsonResp)
    return jsonify(jsonResp)

#http://127.0.0.1:5000/
app.run(port=8000)
