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

# The below list includes IDs which have URL redirection and prevent the proper operation
blacklist = [3369, 3533,3442]

first = 3000
last = 4900

print ("")

while first <= last:

    if first not in blacklist:

        # Requesting the document from the public website
        varUrl = "https://www.netapp.com/us/media/tr-" + str(first) + ".pdf"
        r = requests.get(varUrl)

        # Check if the document is already in the catalogue
        varTR = "TR-" + str(first)
        matching = [s for s in currentTRs if varTR in s]
        
        currentTitle = ''

        # If the document is currently public
        if (r.status_code == 200):

            # Check if the requested http object is a PDF file
            isPDFfile = (r.headers['content-type']=='application/pdf')
            if isPDFfile:

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
                    # os.remove(str(first) + '.pdf')

                # If it is included in the catalogue
                if len(matching) != 0:
                    
                    # Get the title form the catalogue
                    currentTitle = ''.join(matching)

                    # Download the document
                    with open(str(first) + ".pdf", "wb") as pdf:
                        pdf.write(r.content)

                print('<a href="https://www.netapp.com/us/media/tr-' + str(first) + '.pdf" class="TR-url" target="_blank">' + currentTitle + '</a><br />')

    first = first + 1
