from pyzbar.pyzbar import decode
import json
from PIL import Image
from downloadImage import downloadImage
import requests

def solve(token):
    get_link = "https://hackattic.com/challenges/reading_qr/problem?access_token="+token
    downloadImage(get_link)
    d = decode(Image.open('img.png'))
    message = d[0].data.decode('ascii')
    post_url = "https://hackattic.com/challenges/reading_qr/solve?access_token="+token
    data = json.dumps({"code":message})
    response = requests.post(url=post_url,data=data)
    return response


if __name__ == "__main__":
    token = "84edafdf68f8408b"
    print(solve(token))