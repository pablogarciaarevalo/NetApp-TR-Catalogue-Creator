import os
from lxml import html
import requests
from pdfrw import PdfReader

# Download the catalogue site
urlCatalogue = "https://pablogarciaarevalo.com/NetApp_TR_Catalogue.html"
siteCatalogue = requests.get(urlCatalogue)
catalogue = html.fromstring(siteCatalogue.content)

# This will create a list of the current published documents
currentTRs = catalogue.xpath('//a[@class="TR-url"]/text()')

first = 3000
last = 4900

print ("")

while first <= last:
    # Requesting the document from the public website
    varUrl = "http://www.netapp.com/us/media/tr-" + str(first) + ".pdf"
    r = requests.get(varUrl)

    # Check if the document is already in the catalogue
    varTR = "TR-" + str(first)
    matching = [s for s in currentTRs if varTR in s]
    
    currentTitle = ''

    # If the document is currently public
    if (r.status_code == 200):

        # If it is not included in the catalogue
        if len(matching) == 0:
        
            # Download the document
            with open(str(first) + ".pdf", "wb") as pdf:
                pdf.write(r.content)
            
            # Get the title from the PDF file
            myPDF = open(str(first) + ".pdf", 'rb')
            try:
                currentTitle = PdfReader(myPDF).Info.Title.strip('()')
            except:
                pass

            myPDF.close()

            # Remove the local document
            os.remove(str(first) + '.pdf')

        # If it is included in the catalogue
        if len(matching) != 0:
            
            # Get the title form the catalogue
            currentTitle = ''.join(matching)

        print('<a href="http://www.netapp.com/us/media/tr-' + str(first) + '.pdf" class="TR-url" target="_blank">' + currentTitle + '</a><br />')

    first = first + 1
