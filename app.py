from flask import Flask, render_template, request
# flask 에서 Flask(웹서버를 만드는 기능)를 가져온다.
#render_template : html 파일을 읽어 웹페이지로 보여주는 기능
from scrapper import search_incruit

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") # index.html 파일을 읽어서 브라우저에 보여줘

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = search_incruit(keyword)
    data = "19기 어플리케이션 과정"
    return render_template("search.html", data=data, keyword=keyword, jobs=enumerate(jobs))

if __name__ == '__main__':
    app.run(debug=True) 