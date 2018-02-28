import bs4 as bs
import urllib.request
import requests
from bs4 import BeautifulSoup


class elonMuskNews:

    #to save data so that it is easily retreivalable later
    urls=[]
    headlines=[]
    imgUrls=[]
    providedBy=[]

    def __init__(self, query):
        """ This function will run as soon as a object of class is initiated"""
        self.query= query

    def getData(self):
        global news
        """" This methods grabs news from a specific query """
        URL ='https://news.google.com/news/search/section/q/'+self.query+'/'+self.query+'?hl=en&gl=US&ned=us'
        response= requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        # most_recent_news= soup.find_all("a", { "class" : "nuEeue hzdq5d ME7ew" })
        most_recent_news= soup.find_all("c-wiz", { "class" : "M1Uqc kWyHVd" })
        news={"headlines":[], "urls":[], "imgUrls":[], "providedBy":[]}
        # grabs the url for the images in chronological order
        for topNews in most_recent_news:
            news["imgUrls"].append(topNews.get('data-thumbnail-url'))
            headlineNDate=[]
            for data in topNews:
                href=data.get("href")
                dataSplit=data.text
                headlineNDate.append(str(dataSplit))
                if href != None:
                    news['urls'].append(href)
                else:
                    pass
            headline=headlineNDate[0]
            providedBy=headlineNDate[1][0:-1]
            news['headlines'].append(headlineNDate[0])
            news['providedBy'].append(headlineNDate[1][0:-1])



        # add the different query to variables
        allHeadlines= news["headlines"]
        allUrls = news["urls"]
        allImgUrls= news["imgUrls"]
        allProvidedBy= news["providedBy"]

        #appending all news credentials to a list so that it is easily retreivalable
        elonMuskNews.headlines.append(allHeadlines)
        elonMuskNews.urls.append(allUrls)
        elonMuskNews.imgUrls.append(allImgUrls)
        elonMuskNews.providedBy.append(allProvidedBy)

    def getHeadline(self,num):
        return(elonMuskNews.headlines[0][num])

    def getUrl(self,num):
        return(elonMuskNews.urls[0][num])

    def getImgUrls(self, num):
        return(elonMuskNews.imgUrls[0][num])

    def getProvidedBy(self, num):
        return(elonMuskNews.providedBy[0][num])

    def getAllSelected(self,num):
        return(elonMuskNews.headlines[0][num], elonMuskNews.urls[0][num] ,elonMuskNews.imgUrls[0][num], elonMuskNews.providedBy[0][num])

    def getEverything(self):
        #to print everything in a nice format(20 entries every time)
        # count=0
        # for x in range(20):
        #     print(elonMuskNews.headlines[0][count])
        #     print(elonMuskNews.urls[0][count])
        #     print(elonMuskNews.imgUrls[0][count])
        #     print(elonMuskNews.providedBy[0][count])
        #     print(" ")
        #     count+=1
        return(news)
        # return(elonMuskNews.headlines, elonMuskNews.urls, elonMuskNews.imgUrls, elonMuskNews.providedBy)
