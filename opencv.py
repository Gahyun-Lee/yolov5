from pyzbar import pyzbar
import cv2 # pip3 install  opencv-python-headless
import requests
from bs4 import BeautifulSoup


#qr 인식
def qr(frame):

    url = str()
    qr = pyzbar.decode(frame)
    
    if not qr:
        return False
    for d in qr:
        u = d.data
        url = str(u)[2:-1]
    
    cv2.waitKey(1)     
    
    return url

#QR에서 얻은 URL에서 data 추출
def getData(url):
    #url = "https://me-qr.com/text/3217540/show"
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    data = soup.p.string
    result = list(data.split(','))
    return result