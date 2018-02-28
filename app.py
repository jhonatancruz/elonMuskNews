from flask import Flask, render_template
from getNews import *

app= Flask(__name__)


@app.route("/")
def main():
    elon= elonMuskNews("elon musk")
    elon.getData()
    allNews= elon.getEverything()
    # headline=elon.getHeadline(1)
    # url= elon.getUrl(1)
    # imgUrl= elon.getImgUrls(1)
    # providedBy= elon.getProvidedBy(1)
    print("finished")
    return render_template("home.html", allNews=allNews)

# def retrieveData():
#     elon= elonMuskNews("elon musk")
#     elon.getData()
#     everything= elon.getEverything()
#     # position= input()
#     # count=0
#     # for x in everything:
#     #     count+=1
#     #
#     print(everything["headlines"][0])
#
# retrieveData()

if __name__== "__main__":
    app.run(debug=True)
