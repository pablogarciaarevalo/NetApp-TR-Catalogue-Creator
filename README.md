# NetApp-TR-Catalogue-Creator
Create a NetApp Technical Report Catalogue

## Getting Started

This script index the NetApp Technical Reports which has been published and create a catalogue at [https://pablogarciaarevalo.com/NetApp_TR_Catalogue.html](https://pablogarciaarevalo.com/NetApp_TR_Catalogue.html)

## Requirements

The below python libraries are required

```
pip install lxml
pip install requests
pip install pdfrw
```

## Running

Example running the script with an output with a document which needs to be included and a document which need to be removed
```
> python .\TR-catalogue-creator.py
### The document TR-3008 needs to be removed from the catalogue ###
### The document TR-3009 needs to be included in the catalogue ###
<a href="http://www.netapp.com/us/media/tr-3009 .pdf" class="TR-url" target="_blank">TR-3009 :  Filer Deployment Strategies for Evolving LAN Topologies </a><br />
```
