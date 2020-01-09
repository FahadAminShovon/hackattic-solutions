import requests,json

def getImageUrl(link):
    try:
        PROBLEM_URL =  link
        getProblem = requests.get(PROBLEM_URL)
        getProblem = getProblem.json()
        QR_URL = list(getProblem.keys())[0]
        QR_URL = getProblem[QR_URL]
        return QR_URL
    except :
        return None

def downloadImage(link):
    imageUrl = getImageUrl(link)
    xx = requests.get(imageUrl).content
    f = open("img.png","wb")
    f.write(xx)

if __name__=="__main__":
    downloadImage("https://hackattic.com/challenges/reading_qr/problem?access_token=84edafdf68f8408b")
