import pyqrcode
import png
from pyqrcode import QRCode
  
  
# Desired data content of my QR Code 
myData = """COVID-19 CONTACT TRACING INFORMATION

Full-Name: Adrian Remoquillo Esguerra 
Address: Sherlock Holmes - 221B Baker St., London
Sex: Male						
Age: 18 years old
Contact Number: 0912-345-6789
Date of Birth: February 14, 2003

Has any severe symptoms related to COVID-19?
> None

Are you fully vaccinated?	
> Yes	

Last place you have been:
> Natural History Museum

Last 5 people you were with:
> Tom Holland
> Robert Downey Jr.
> Chris Evans
> Chris Hemsworth
> Scarlett Johansson"""
  
# Generate QR code
QR = pyqrcode.create(myData)
  
# Create and save into png file 
QR.png("myQRCode.png", 6)