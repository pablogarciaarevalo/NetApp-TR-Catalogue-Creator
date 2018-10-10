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

while first <= last:
    # Requesting the document from the public website
    varUrl = "http://www.netapp.com/us/media/tr-" + str(first) + ".pdf"
    r = requests.get(varUrl)

    # Check if the document is already in the catalogue
    varTR = "TR-" + str(first)
    matching = [s for s in currentTRs if varTR in s]

    # If the document has been published but it's not included in the catalogue
    if (r.status_code == 200) and len(matching) == 0:
        
        # Download the document
        with open(str(first) + ".pdf", "wb") as pdf:
            pdf.write(r.content)
        
        # Get the PDF title
        myPDF = open(str(first) + ".pdf", 'rb')
        title = PdfReader(myPDF).Info.Title.strip('()')
        myPDF.close()

        print("### The document TR-" + str(first) + " needs to be included in the catalogue ###")
        print('<a href="http://www.netapp.com/us/media/tr-' + str(first) + '.pdf" class="TR-url" target="_blank">TR-' + str(first) + ': ' + title + '</a><br />')

        # Remove the local file
        os.remove(str(first) + '.pdf')

    # If the document is not public anymore but it's included in the catalogue
    elif (r.status_code != 200) and len(matching) != 0:
        print("### The document TR-" + str(first) + " needs to be removed from the catalogue ###")

    first = first + 1