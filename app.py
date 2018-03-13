from flask import Flask, render_template
from getNews import *
import schedule, time
from threading import Thread

app= Flask(__name__)


def refreshNews():
    print("retrieving data")
    global allNews, allTesla, allspaceX, allboringCompany
    #all elon musk news
    elon= elonMuskNews("elon musk")
    elon.getData()
    allNews= elon.getEverything()

    # all tesla news
    tesla= elonMuskNews("tesla")
    tesla.getData()
    allTesla= tesla.getEverything()

    #all spacex news
    spaceX= elonMuskNews("spacex")
    spaceX.getData()
    allspaceX= spaceX.getEverything()

    #all boring company news
    boringCompany= elonMuskNews("boring company")
    boringCompany.getData()
    allboringCompany= boringCompany.getEverything()

def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)


@app.route("/")
def main():
    return render_template("home.html", allNews=allNews, allTesla=allTesla, allspaceX=allspaceX,
                            allboringCompany=allboringCompany)

refreshNews()

if __name__== "__main__":
    schedule.every(30).minutes.do(refreshNews)
    t = Thread(target=run_schedule)
    t.start()
    app.run(debug=True)
