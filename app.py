from flask import Flask, request, url_for , render_template ,jsonify
from imageHelper import imageHelper

app = Flask(__name__)

#driver.get('http://www.google.com')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/print', methods=["GET", "POST"])
def month_increment():
    if request.method == "POST":
        try:
            data = request.get_json()
            print(data)
            imageHelper.renderHTML(data)
        except Exception as e:
            print(e)
        finally:
            pass
    return jsonify(200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0:5000')
