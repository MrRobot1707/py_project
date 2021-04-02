import pyqrcode
from pyqrcode import QRCode 

s = 'https://www.youtube.com/watch?v=EatzcaVJRMs'

url = pyqrcode.create(s)

url.svg("myyoutube.svg",scale = 8)