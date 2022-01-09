import cgi
import pyqrcode 
from pyqrcode import QRCode 
  
form = cgi.FieldStorage()


# String which represent the QR code 
qrlink = form.getvalue('QR-link')
  
# Generate QR code 
url = pyqrcode.create(qrlink) 
  
# Create and save the svg file naming "mygithub.png" 
url.svg("mygithub.svg", scale = 8) 