import urllib2
import json

class quoteData:
  def __init__(self, quote, author):
    self.quote = quote
    self.author = author


def getResponseFromIndieHacks(pageIndex) :
  req = urllib2.Request('https://indie-hackers.firebaseio.com/loadingQuotes/' + str(pageIndex) + '.json')
  response = urllib2.urlopen(req)
  return response.read()

def getQuote(responseJson):
  return responseJson["quote"]

def getAuthor(responseJson):
  return responseJson["byline"]

def isValidResponse(response):
  if response == "null" or not(response):
    return False
  return True

def processResult(quoteDataList):
  f = open("quote_dump.txt", "w")
  for quoteData in quoteDataList:
    f.write("quote: " + quoteData.quote + "\n")
    f.write("author: " + quoteData.author + "\n")
    f.write("\n")
  f.close()




quoteDataList = []

for i in range(0, 100):
  print i
  response = None
  try:
    response = getResponseFromIndieHacks(i)
    if not(isValidResponse(response)):
      print "Invalid response: " + response + "\nfor index i: " + i
      continue
    responseJson = json.loads(response)
    quote = getQuote(responseJson)
    author = getAuthor(responseJson)
    quoteDataList.append(quoteData(unicode(quote).encode('utf-8'), unicode(author).encode('utf-8')))
  except ValueError:
    print "Exception parsing json for response: " + response
    continue

processResult(quoteDataList)



